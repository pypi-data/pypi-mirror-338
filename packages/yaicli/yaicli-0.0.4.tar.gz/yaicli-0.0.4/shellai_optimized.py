#!/usr/bin/env python3
"""
ShellAI - An LLM-powered command-line assistant
Provides interactive chat and shell command generation via LLM APIs
"""

import configparser
import json
import logging
import subprocess
import time
from abc import ABC, abstractmethod
from enum import StrEnum
from os import getenv
from os.path import basename, pathsep
from pathlib import Path
from typing import Annotated, Any, Dict, List, Optional, Union

import jmespath
import requests
import typer
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings, KeyPressEvent
from prompt_toolkit.keys import Keys
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown
from rich.prompt import Confirm

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("llmcli")


class ModeEnum(StrEnum):
    """Defines the operation modes for ShellAI"""

    CHAT = "chat"  # Interactive chat mode
    EXECUTE = "execute"  # Shell command generation mode
    TEMP = "temp"  # One-shot mode


class CasePreservingConfigParser(configparser.RawConfigParser):
    """Config parser that preserves case in option names"""

    def optionxform(self, optionstr):
        return optionstr


class LLMProvider(ABC):
    """Base class for LLM API providers"""

    @abstractmethod
    def call_api(self, prompt: str, stream: bool = True) -> Union[str, requests.Response]:
        """Call the LLM API with the given prompt"""
        pass

    @abstractmethod
    def process_response(self, response: requests.Response, answer_path: str) -> str:
        """Process the API response to extract the content"""
        pass


class OpenAIProvider(LLMProvider):
    """OpenAI API implementation"""

    def __init__(self, config: Dict[str, str], verbose: bool = False):
        self.config = config
        self.verbose = verbose

    def call_api(self, prompt: str, stream: bool = True) -> requests.Response:
        """Call the OpenAI API with the given prompt"""
        base_url = self.config.get("BASE_URL", "").rstrip("/")
        api_key = self.config.get("API_KEY", "")
        model = self.config.get("MODEL", "gpt-4o")
        completion_path = self.config.get("COMPLETION_PATH", "chat/completions").lstrip("/")

        if not base_url:
            raise ValueError("Base URL not configured")
        if not api_key:
            raise ValueError("API key not configured")

        url = f"{base_url}/{completion_path}"
        headers = {"Authorization": f"Bearer {api_key}"}
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": stream,
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Error calling API: {e}")
            raise

    def process_response(self, response: requests.Response, answer_path: str) -> str:
        """Process the API response to extract the content"""
        if not response:
            return ""

        try:
            content = jmespath.search(answer_path, response.json())
            return content.strip() if content else ""
        except (json.JSONDecodeError, jmespath.exceptions.JMESPathError) as e:
            logger.error(f"Error processing response: {e}")
            return ""


class CommandProcessor:
    """Handles shell command processing and execution"""

    def __init__(self, console: Console):
        self.console = console

    def filter_command(self, command: str) -> str:
        """
        Filter out unwanted characters from command

        The LLM may return commands in markdown format with code blocks.
        This method removes markdown formatting from the command.
        It handles various formats including:
        - Commands surrounded by ``` (plain code blocks)
        - Commands with language specifiers like ```bash, ```zsh, etc.
        - Commands with specific examples like ```ls -al```

        Examples:
        ```bash\nls -la\n``` ==> ls -al
        ```zsh\nls -la\n``` ==> ls -al
        ```ls -al``` ==> ls -al
        ls -al ==> ls -al
        ```\ncd /tmp\nls -la\n``` ==> cd /tmp\nls -la
        ```bash\ncd /tmp\nls -la\n``` ==> cd /tmp\nls -la
        """
        if not command or not command.strip():
            return ""

        # Handle commands that are already without code blocks
        if "```" not in command:
            return command.strip()

        # Handle code blocks with or without language specifiers
        lines = command.strip().split("\n")

        # Check if it's a single-line code block like ```ls -al```
        if len(lines) == 1 and lines[0].startswith("```") and lines[0].endswith("```"):
            return lines[0][3:-3].strip()

        # Handle multi-line code blocks
        if lines[0].startswith("```"):
            # Remove the opening ``` line (with or without language specifier)
            content_lines = lines[1:]

            # If the last line is a closing ```, remove it
            if content_lines and content_lines[-1].strip() == "```":
                content_lines = content_lines[:-1]

            # Join the remaining lines and strip any extra whitespace
            return "\n".join(line.strip() for line in content_lines if line.strip())

        return command.strip()

    def execute_command(self, command: str) -> int:
        """Execute shell command and return the return code"""
        self.console.print(f"\n[bold green]Executing command: [/bold green] {command}\n")
        result = subprocess.run(command, shell=True)

        if result.returncode != 0:
            self.console.print(
                f"\n[bold red]Command failed with return code: {result.returncode}[/bold red]"
            )

        return result.returncode


class ConfigManager:
    """Manages the ShellAI configuration"""

    # Configuration file path
    CONFIG_PATH = Path("~/.config/llmcli/config.ini").expanduser()

    # Default configuration template
    DEFAULT_CONFIG_INI = """[core]
BASE_URL=https://api.openai.com/v1
API_KEY=
MODEL=gpt-4o
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

    def __init__(self, console: Console, verbose: bool = False):
        self.console = console
        self.verbose = verbose

    def get_default_config(self) -> Dict[str, str]:
        """Get default configuration"""
        config = CasePreservingConfigParser()
        try:
            config.read_string(self.DEFAULT_CONFIG_INI)
            config_dict = {k.upper(): v for k, v in config["core"].items()}
            config_dict["STREAM"] = str(config_dict.get("STREAM", "true")).lower()
            return config_dict
        except configparser.Error as e:
            logger.error(f"Error parsing default config: {e}")
            self.console.print(f"[red]Error parsing config: {e}[/red]")
            raise typer.Exit(code=1)

    def load_config(self) -> Dict[str, str]:
        """Load LLM API configuration"""
        # Create default config if it doesn't exist
        if not self.CONFIG_PATH.exists():
            self.console.print(
                "[bold yellow]Configuration file not found. Creating default configuration file.[/bold yellow]"
            )
            self.CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
            with open(self.CONFIG_PATH, "w") as f:
                f.write(self.DEFAULT_CONFIG_INI)
            return self.get_default_config()

        # Load existing config
        config = CasePreservingConfigParser()
        config.read(self.CONFIG_PATH)

        if "core" not in config:
            logger.warning("Invalid config file format, using defaults")
            return self.get_default_config()

        config_dict = dict(config["core"])
        config_dict["STREAM"] = str(config_dict.get("STREAM", "true")).lower()

        # Override with environment variables if present
        api_key = getenv("SHELLAI_API_KEY")
        if api_key:
            config_dict["API_KEY"] = api_key

        return config_dict

    def detect_os(self, config: Dict[str, str]) -> str:
        """Detect operating system"""
        if config.get("OS_NAME") != "auto":
            return config.get("OS_NAME")

        import platform

        return platform.system()

    def detect_shell(self, config: Dict[str, str]) -> str:
        """Detect shell"""
        if config.get("SHELL_NAME") != "auto":
            return config.get("SHELL_NAME")

        import platform

        current_platform = platform.system()

        if current_platform in ("Windows", "nt"):
            is_powershell = len(getenv("PSModulePath", "").split(pathsep)) >= 3
            return "powershell.exe" if is_powershell else "cmd.exe"

        return basename(getenv("SHELL", "/bin/sh"))


class ShellAI:
    """ShellAI - An LLM-powered command-line assistant"""

    def __init__(self, verbose: bool = False):
        # Initialize components
        self.verbose = verbose
        self.console = Console()
        self.bindings = KeyBindings()
        self.session = PromptSession(key_bindings=self.bindings)
        self.current_mode = ModeEnum.CHAT.value
        self.config = {}

        # Initialize managers
        self.config_manager = ConfigManager(self.console, verbose)
        self.command_processor = CommandProcessor(self.console)

        # Set up key bindings
        self._setup_key_bindings()

    def _setup_key_bindings(self):
        """Set up keyboard shortcuts"""

        @self.bindings.add(Keys.ControlI)  # Bind Ctrl+I to switch modes
        def _(event: KeyPressEvent):
            self.current_mode = (
                ModeEnum.CHAT.value
                if self.current_mode == ModeEnum.EXECUTE.value
                else ModeEnum.EXECUTE.value
            )

    def get_llm_provider(self) -> LLMProvider:
        """Get LLM provider based on configuration"""
        return OpenAIProvider(self.config, self.verbose)

    def call_llm_api(self, prompt: str):
        """Call LLM API with streaming output"""
        try:
            provider = self.get_llm_provider()
            response = provider.call_api(
                prompt, stream=self.config.get("STREAM", "true") == "true"
            )
        except Exception as e:
            self.console.print(f"[red]Error calling API: {e}[/red]")
            return

        self.console.print("\n[bold green]Assistant:[/bold green]")

        # Handle streaming response
        if self.config.get("STREAM", "true") == "true":
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
                            self.console.print("[red]Error decoding response JSON[/red]")
                            if self.verbose:
                                self.console.print(
                                    f"[red]Error decoding JSON: {decoded_line}[/red]"
                                )
                    time.sleep(0.01)  # Reduced sleep time for better performance
        else:
            # Process non-streaming response
            answer_path = self.config.get("ANSWER_PATH", "choices[0].message.content")
            content = provider.process_response(response, answer_path)
            self.console.print(Markdown(content))

        self.console.print()  # Add a newline after the completion

    def get_command_from_llm(self, prompt: str) -> Optional[str]:
        """Request Shell command from LLM"""
        try:
            provider = self.get_llm_provider()

            # Use system message for shell command generation
            base_url = self.config.get("BASE_URL", "").rstrip("/")
            api_key = self.config.get("API_KEY", "")
            model = self.config.get("MODEL", "gpt-4o")

            url = f"{base_url}/chat/completions"
            headers = {"Authorization": f"Bearer {api_key}"}
            data = {
                "model": model,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a command line assistant, return one Linux/macOS shell commands only, without explanation and triple-backtick code blocks.",
                    },
                    {"role": "user", "content": prompt},
                ],
                "stream": False,  # Always use non-streaming for command generation
            }

            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()

            answer_path = self.config.get("ANSWER_PATH", "choices[0].message.content")
            if not answer_path:
                answer_path = "choices[0].message.content"
                if self.verbose:
                    self.console.print(
                        "[bold yellow]Answer path not set. Using default: `choices[0].message.content`[/bold yellow]"
                    )

            content = jmespath.search(answer_path, response.json())
            return content.strip() if content else None

        except Exception as e:
            logger.error(f"Error getting command from LLM: {e}")
            self.console.print(f"[red]Error calling API: {e}[/red]")
            return None

    def get_prompt_tokens(self):
        """Get prompt tokens based on current mode"""
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
        """Execute mode"""
        if user_input == "" or self.current_mode != ModeEnum.EXECUTE.value:
            return self.current_mode

        command = self.get_command_from_llm(user_input)
        if not command:
            self.console.print("[bold red]No command generated[/bold red]")
            return self.current_mode

        command = self.command_processor.filter_command(command)
        if not command:
            self.console.print("[bold red]No command generated after filtering[/bold red]")
            return self.current_mode

        self.console.print(f"\n[bold magenta]Generated command:[/bold magenta] {command}")
        confirm = Confirm.ask("Execute this command?")

        if confirm:
            self.command_processor.execute_command(command)

        return ModeEnum.EXECUTE.value

    def run_repl_loop(self):
        """Run the interactive REPL loop"""
        self.console.print("[bold]ShellAI[/bold] - LLM-powered command-line assistant")
        self.console.print("Type 'exit' or 'quit' to exit, press Ctrl+I to switch modes")

        while True:
            try:
                user_input = self.session.prompt(self.get_prompt_tokens)

                # Skip empty input
                if not user_input.strip():
                    continue

                if user_input.lower() in ("exit", "quit"):
                    break

                if self.current_mode == ModeEnum.CHAT.value:
                    self.chat_mode(user_input)
                elif self.current_mode == ModeEnum.EXECUTE.value:
                    self.execute_mode(user_input)

            except KeyboardInterrupt:
                self.console.print("\n[bold yellow]Interrupted by user[/bold yellow]")
                break
            except Exception as e:
                logger.error(f"Error in REPL loop: {e}")
                self.console.print(f"[bold red]Error: {e}[/bold red]")

        self.console.print("[bold green]Exiting...[/bold green]")

    def run_one_shot(self, prompt: str):
        """Run one-shot mode with given prompt"""
        if self.current_mode == ModeEnum.EXECUTE.value:
            self.execute_mode(prompt)  # Execute mode for one-shot prompt
        else:
            self.call_llm_api(prompt)

    def run(self, chat=False, shell=False, prompt: Optional[str] = None):
        """Run the CLI application"""
        # Load configuration
        self.config = self.config_manager.load_config()
        if not self.config.get("API_KEY", None):
            self.console.print(
                "[red]API key not found. Please set it in the configuration file or use SHELLAI_API_KEY environment variable.[/red]"
            )
            return

        # Set initial mode
        self.current_mode = self.config.get("DEFAULT_MODE", ModeEnum.TEMP.value)

        # Check run mode from command line arguments
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
            self.console.print(
                f"[bold yellow]Using model: {self.config.get('MODEL', 'unknown')}[/bold yellow]"
            )

        if self.current_mode in (ModeEnum.TEMP.value, ModeEnum.EXECUTE.value) and prompt:
            self.run_one_shot(prompt)
        elif self.current_mode == ModeEnum.CHAT.value:
            self.run_repl_loop()


# CLI application setup
CONTEXT_SETTINGS = {
    "help_option_names": ["-h", "--help"],
    "show_default": True,
}

app = typer.Typer(
    name="ShellAI",
    context_settings=CONTEXT_SETTINGS,
    pretty_exceptions_enable=False,
    short_help="ShellAI Command Line Tool",
    no_args_is_help=True,
    invoke_without_command=True,
)


@app.command()
def main(
    prompt: Annotated[str, typer.Argument(show_default=False, help="The prompt send to the LLM")],
    verbose: Annotated[
        bool, typer.Option("--verbose", "-V", help="Show verbose information")
    ] = False,
    chat: Annotated[bool, typer.Option("--chat", "-c", help="Start in chat mode")] = False,
    shell: Annotated[
        bool, typer.Option("--shell", "-s", help="Generate and execute shell command")
    ] = False,
):
    """LLM-powered CLI Tool for chat and shell command generation"""
    cli = ShellAI(verbose=verbose)
    cli.run(chat=chat, shell=shell, prompt=prompt)


if __name__ == "__main__":
    app()
