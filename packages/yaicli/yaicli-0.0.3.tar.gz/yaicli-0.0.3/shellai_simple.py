#!/usr/bin/env python3
"""
ShellAI - An LLM-powered command-line assistant
Provides interactive chat and shell command generation
"""

import json
import platform
import subprocess
import time
from enum import StrEnum
from os import environ
from pathlib import Path
from typing import Annotated, Dict, List, Optional, Tuple, cast

import jmespath
import requests
import typer
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings, KeyPressEvent
from prompt_toolkit.keys import Keys
from pydantic import Field
from pydantic_settings import BaseSettings
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown
from rich.prompt import Confirm

DEFAULT_CONFIG_STR = """BASE_URL=https://api.openai.com/v1
API_KEY=
MODEL=gpt-4o

# default run mode, default: temp
# chat: interactive chat mode
# exec: shell command generation mode
# temp: one-shot mode
DEFAULT_MODE=temp

# auto detect shell and os
SHELL_NAME=auto
OS_NAME=auto

# if you want to use custom completions path, you can set it here
COMPLETION_PATH=/chat/completions
# if you want to use custom answer path, you can set it here
ANSWER_PATH=choices[0].message.content

# true: streaming response
# false: non-streaming response
STREAM=true"""


class ModeEnum(StrEnum):
    """Defines the operation modes for ShellAI"""

    CHAT = "chat"  # Interactive chat mode
    EXECUTE = "exec"  # Shell command generation mode
    TEMP = "temp"  # One-shot mode


class ShellAIConfig(BaseSettings):
    """ShellAI configuration settings"""
    BASE_URL: str = "https://api.openai.com/v1"
    API_KEY: str = Field(default="", validation_alias='OPENAI_API_KEY')
    MODEL: str = "gpt-4o"
    DEFAULT_MODE: ModeEnum = ModeEnum.TEMP
    OS_NAME: str = "auto"
    SHELL_NAME: str = "auto"
    COMPLETION_PATH: str = "/chat/completions"
    ANSWER_PATH: str = "choices[0].message.content"
    STREAM: bool = True

    class Config:
        env_file = "~/.config/llmcli/.llmcli"
        env_file_encoding = "utf-8"


class ConfigManager:
    """Manages configuration loading and validation"""
    def __init__(self):
        self._config = None

    @property
    def config(self) -> ShellAIConfig:
        if not self._config:
            self._load_config()
        return self._config

    def _load_config(self):
        config_path = Path(ShellAIConfig.Config.env_file).expanduser()
        if not config_path.exists():
            config_path.parent.mkdir(parents=True, exist_ok=True)
            config_path.touch()
        self._config = ShellAIConfig()


class ShellAI:
    """ShellAI - An LLM-powered command-line assistant"""

    def __init__(self, verbose: bool = False):
        # Initialize components
        self.verbose = verbose
        self.console = Console()
        self.bindings = KeyBindings()
        self.session = PromptSession(key_bindings=self.bindings)
        self.current_mode = ModeEnum.TEMP.value
        self.config_manager = ConfigManager()

        # Set up key bindings
        self._setup_key_bindings()

    @property
    def config(self) -> ShellAIConfig:
        if self._config is None:
            # Check if config file exists
            config_path = Path(ShellAIConfig.Config.env_file).expanduser()
            if not config_path.exists():
                # Create parent directories if they don't exist
                config_path.parent.mkdir(parents=True, exist_ok=True)
                # Write default config
                with open(config_path, "w") as f:
                    f.write(DEFAULT_CONFIG_STR)
                self.console.print(f"[yellow]Config file created at {config_path}. Please edit it to set your API key.[/yellow]")
                raise typer.Exit(0)

            self._config = ShellAIConfig()

        return self._config

    def detect_os(self) -> str:
        """Detects the operating system"""
        if self.config_manager.config.OS_NAME != "auto":
            return self.config_manager.config.OS_NAME
        return platform.system()

    def detect_shell(self) -> str:
        """Detects the shell"""
        if self.config_manager.config.SHELL_NAME != "auto":
            return self.config_manager.config.SHELL_NAME
        current_platform = platform.system()
        if current_platform in ("Windows", "nt"):
            is_powershell = len(environ.get("PSModulePath", "").split(":")) >= 3
            return "powershell.exe" if is_powershell else "cmd.exe"
        return Path(environ.get("SHELL", "/bin/sh")).name

    def _setup_key_bindings(self):
        """Sets up keyboard shortcuts"""

        @self.bindings.add(Keys.ControlI)  # Bind Ctrl+I to toggle mode
        def _(event: KeyPressEvent):
            self.current_mode = (
                ModeEnum.CHAT.value
                if self.current_mode == ModeEnum.EXECUTE.value
                else ModeEnum.EXECUTE.value
            )

    def call_api(
        self, url: str, headers: Dict[str, str], data: Dict, method: str = "POST"
    ) -> requests.Response:
        """Generic API call method with better error handling

        Args:
            url: The URL to call
            headers: HTTP headers to include
            data: JSON data to send
            method: HTTP method to use (default: POST)

        Returns:
            Response object from the API call

        Raises:
            requests.exceptions.RequestException: If the request fails
        """
        try:
            if method.upper() == "POST":
                response = requests.post(url, headers=headers, json=data)
            elif method.upper() == "GET":
                response = requests.get(url, headers=headers, params=data)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            self.console.print(f"[red]API call error: {e}[/red]")
            raise

    def _prepare_llm_request(self, prompt: str) -> Optional[Tuple[str, Dict[str, str], Dict]]:
        """Prepare the request data for the LLM API call"""
        base_url = self.config_manager.config.BASE_URL.rstrip("/")
        if not base_url:
            self.console.print(
                "[red]No base URL found, please set it in the configuration file. Default value: https://api.openai.com/v1[/red]"
            )
            return None

        api_key = self.config_manager.config.API_KEY
        if not api_key:
            self.console.print(
                "[red]No API key found, please set it in the configuration file.[/red]"
            )
            return None

        completion_path = self.config_manager.config.COMPLETION_PATH.lstrip("/")
        url = f"{base_url}/{completion_path}"
        headers = {"Authorization": f"Bearer {api_key}"}
        data = {
            "model": self.config_manager.config.MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": self.config_manager.config.STREAM,
        }

        return url, headers, data

    def _handle_streaming_response(self, response: requests.Response) -> str:
        """Process a streaming response from the LLM API"""
        full_completion = ""
        with Live(console=self.console) as live:
            for line in response.iter_lines():
                if not line:
                    continue
                decoded_line = line.decode("utf-8")
                if decoded_line.startswith("data: "):
                    decoded_line = decoded_line[6:]
                    if decoded_line == "[DONE]":
                        break
                    try:
                        json_data = json.loads(decoded_line)
                        content = json_data["choices"][0]["delta"].get("content", "")
                        full_completion += content
                        markdown = Markdown(markup=full_completion)
                        live.update(markdown, refresh=True)
                    except json.JSONDecodeError:
                        self.console.print("[red]JSON parsing error[/red]")
                        if self.verbose:
                            self.console.print(f"[red]JSON parsing error: {decoded_line}[/red]")
                time.sleep(0.01)
        return full_completion

    def _handle_non_streaming_response(self, response: requests.Response) -> str:
        """Process a non-streaming response from the LLM API"""
        answer_path = self.config.ANSWER_PATH
        try:
            content = jmespath.search(answer_path, response.json())
            if content:
                self.console.print(Markdown(content.strip()))
                return content
            return ""
        except Exception as e:
            self.console.print(f"[red]Error parsing response: {e}[/red]")
            return ""

    def call_llm_api(self, prompt: str) -> str:
        """Calls the LLM API and handles streaming responses"""
        request_data = self._prepare_llm_request(prompt)
        if not request_data:
            return ""  # Return empty string if request preparation failed

        url, headers, data = request_data

        try:
            response = self.call_api(url, headers, data)
        except requests.exceptions.RequestException:
            # Error already logged in call_api
            return ""

        self.console.print("\n[bold green]Assistant:[/bold green]")

        # Handle streaming/non-streaming responses
        result = ""
        if self.config.STREAM:
            result = self._handle_streaming_response(response)
        else:
            result = self._handle_non_streaming_response(response)

        self.console.print()  # Add an empty line after completion
        return result

    def _api_request(self, messages: list) -> str:
        """通用API请求方法"""
        base_url = self.config.BASE_URL.rstrip('/')
        url = f"{base_url}{self.config.COMPLETION_PATH}"
        headers = {"Authorization": f"Bearer {self.config.API_KEY}"}
        data = {
            "model": self.config.MODEL,
            "messages": messages,
            "stream": self.config.STREAM
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return self._handle_response(response)
        except Exception as e:
            self.console.print(f"[red]API错误: {e}[/red]")
            return ""

    def _handle_response(self, response) -> str:
        """Handle API response"""
        match self.config.STREAM:
            case True:
                return self._handle_streaming_response(response)
            case _:
                return jmespath.search(self.config.ANSWER_PATH, response.json()) or ""

    def get_command_from_llm(self, prompt: str) -> Optional[str]:
        """获取shell命令"""
        messages = [
            {"role": "system", "content": "Return only Linux/macOS commands without explanations"},
            {"role": "user", "content": prompt}
        ]
        return self._api_request(messages)

    def filter_command(self, command: str) -> str:
        """Filters out unnecessary characters from the command

        The LLM may return commands with Markdown formatting, this method removes the formatting.
        It handles various formats, including:
        - Commands surrounded by triple backticks (ordinary code blocks)
        - Code blocks with language specification, such as ```bash, ```zsh, etc.
        - Specific example code blocks, such as ```ls -al```

        Examples:
        ```bash\nls -la\n``` ==> ls -al
        ```zsh\nls -la\n``` ==> ls -al
        ```ls -al``` ==> ls -al
        ls -al ==> ls -al
        ```\ncd /tmp\nls -la\n``` ==> cd /tmp\nls -la
        ```bash\ncd /tmp\nls -la\n``` ==> cd /tmp\nls -la
        """
        import re

        if not command or not command.strip():
            return ""

        # Simple case - no code blocks
        if "```" not in command:
            return command.strip()

        # Handle single-line code blocks: ```command```
        single_line_match = re.match(r"^```(.+?)```$", command.strip())
        if single_line_match:
            return single_line_match.group(1).strip()

        # Handle multi-line code blocks with or without language specification
        # Pattern: ```[language]
        multi_line_match = re.match(
            r"^```(?:[a-zA-Z]*)?\s*\n(.+?)\s*```\s*$", command.strip(), re.DOTALL
        )
        if multi_line_match:
            content = multi_line_match.group(1).strip()
            # Preserve newlines in the actual command
            return content

        # Fallback for any other patterns
        return command.strip()

    def execute_shell_command(self, command: str) -> int:
        """Executes a shell command"""
        self.console.print(f"\n[bold green]Executing command: [/bold green] {command}\n")
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            self.console.print(
                f"\n[bold red]Command execution failed, return code: {result.returncode}[/bold red]"
            )
        return result.returncode

    def get_prompt_tokens(self) -> List[Tuple[str, str]]:
        """Gets the prompt tokens based on the current mode"""
        if self.current_mode == ModeEnum.CHAT.value:
            qmark = "💬"
        elif self.current_mode == ModeEnum.EXECUTE.value:
            qmark = "🚀"
        else:
            qmark = ""
        return [("class:qmark", qmark), ("class:question", " {} ".format(">"))]

    def chat_mode(self, user_input: str) -> str:
        """Interactive chat mode"""
        if self.current_mode != ModeEnum.CHAT.value:
            return self.current_mode

        self.call_llm_api(user_input)
        return ModeEnum.CHAT.value

    def execute_mode(self, user_input: str) -> str:
        """Execution mode"""
        if user_input == "" or self.current_mode != ModeEnum.EXECUTE.value:
            return self.current_mode

        command = self.get_command_from_llm(user_input)
        if not command:
            self.console.print("[bold red]No command generated[/bold red]")
            return self.current_mode

        command = self.filter_command(command)
        if not command:
            self.console.print("[bold red]Filtered command is empty[/bold red]")
            return self.current_mode

        self.console.print(f"\n[bold magenta]Generated command:[/bold magenta] {command}")
        confirm = Confirm.ask("Execute this command?")

        if confirm:
            self.execute_shell_command(command)

        return ModeEnum.EXECUTE.value

    def run_repl_loop(self):
        """运行REPL主循环"""
        while True:
            try:
                user_input = self.session.prompt(self.get_prompt_tokens)
                if user_input.lower() in ('exit', 'quit'):
                    break

                match self.current_mode:
                    case ModeEnum.CHAT.value:
                        self._api_request([{'role':'user','content':user_input}])
                    case ModeEnum.EXECUTE.value:
                        self.get_command_from_llm(user_input)
                    case ModeEnum.TEMP.value:
                        self.run_one_shot(user_input)
            except (KeyboardInterrupt, EOFError):
                break

    def run_one_shot(self, prompt: str):
        """Runs the one-shot mode with the given prompt"""
        if self.current_mode == ModeEnum.EXECUTE.value:
            self.execute_mode(prompt)  # Execution mode with a one-shot prompt
        else:
            self.call_llm_api(prompt)

    def run(self, chat: bool = False, shell: bool = False, prompt: str = ""):
        """Runs the CLI application"""
        # Set the initial mode
        self.current_mode = self.config.DEFAULT_MODE

        # Check command-line arguments for the running mode
        if all([chat, shell]):
            self.console.print("[red]Cannot use both --chat and --shell[/red]")
            return
        elif chat:
            self.current_mode = ModeEnum.CHAT.value
        elif shell:
            self.current_mode = ModeEnum.EXECUTE.value

        if self.verbose:
            self.console.print("[bold yellow]Verbose mode enabled[/bold yellow]")
            self.console.print(f"[bold yellow]Current mode: {self.current_mode}[/bold yellow]")
            self.console.print(f"[bold yellow]Using model: {self.config.MODEL}[/bold yellow]")

        # Run the application based on the mode and prompt
        if self.current_mode in (ModeEnum.TEMP.value, ModeEnum.EXECUTE.value):
            if not prompt:
                self.console.print("[red]Please provide a prompt like `ai 'Hello'`[/red]")
                return
            self.run_one_shot(prompt)
        elif self.current_mode == ModeEnum.CHAT.value or not prompt:
            self.run_repl_loop()


# CLI application settings
CONTEXT_SETTINGS = {
    "help_option_names": ["-h", "--help"],
}

app = typer.Typer(
    name="ShellAI",
    context_settings=CONTEXT_SETTINGS,
    pretty_exceptions_enable=False,
    short_help="ShellAI command-line tool",
    no_args_is_help=True,
    invoke_without_command=True,
)


@app.command()
def main(
    prompt: Annotated[
        str, typer.Argument(show_default=False, help="Prompt to send to the LLM")
    ] = "",
    verbose: Annotated[
        bool, typer.Option("--verbose", "-V", help="Show detailed information")
    ] = False,
    chat: Annotated[bool, typer.Option("--chat", "-c", help="Start in chat mode")] = False,
    shell: Annotated[
        bool, typer.Option("--shell", "-s", help="Generate and execute shell commands")
    ] = False,
):
    """LLM-powered CLI tool for chat and shell command generation"""
    cli = ShellAI(verbose=verbose)
    cli.run(chat=chat, shell=shell, prompt=prompt)


if __name__ == "__main__":
    app()
