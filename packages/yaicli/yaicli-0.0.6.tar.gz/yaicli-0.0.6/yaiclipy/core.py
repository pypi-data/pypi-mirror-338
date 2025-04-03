import platform
from os import getenv
from os.path import basename, pathsep
from typing import Optional

from distro import name as distro_name
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings, KeyPressEvent
from prompt_toolkit.keys import Keys
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown
from rich.prompt import Confirm

from yaicli.config import ConfigManager
from yaicli.const import ModeEnum


class YAICLI:
    """Main class for YAICLI
    Chat mode: interactive chat mode
    One-shot mode:
        Temp: ask a question and get a response once
        Execute: generate and execute shell commands
    """

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.console = Console()
        self.bindings = KeyBindings()
        self.session = PromptSession(key_bindings=self.bindings)
        self.current_mode = ModeEnum.TEMP.value
        self.config = ConfigManager()
        self.history = []
        self.max_history_length = 25

        # Setup key bindings
        self._setup_key_bindings()

    def _setup_key_bindings(self):
        """Setup keyboard shortcuts"""

        @self.bindings.add(Keys.ControlI)  # Bind Ctrl+I to switch modes
        def _(event: KeyPressEvent):
            self.current_mode = (
                ModeEnum.CHAT.value
                if self.current_mode == ModeEnum.EXECUTE.value
                else ModeEnum.EXECUTE.value
            )

    def clear_history(self):
        """Clear chat history"""
        self.history = []

    def detect_os(self) -> str:
        """Detect operating system
        Returns:
            str: operating system name
        Raises:
            typer.Exit: if there is an error with the request
        """
        if self.config.get("OS_NAME") != "auto":
            return self.config["OS_NAME"]
        current_platform = platform.system()
        if current_platform == "Linux":
            return "Linux/" + distro_name(pretty=True)
        if current_platform == "Windows":
            return "Windows " + platform.release()
        if current_platform == "Darwin":
            return "Darwin/MacOS " + platform.mac_ver()[0]
        return current_platform

    def detect_shell(self) -> str:
        """Detect shell
        Returns:
            str: shell name
        Raises:
            typer.Exit: if there is an error with the request
        """
        if self.config["SHELL_NAME"] != "auto":
            return self.config["SHELL_NAME"]
        import platform

        current_platform = platform.system()
        if current_platform in ("Windows", "nt"):
            is_powershell = len(getenv("PSModulePath", "").split(pathsep)) >= 3
            return "powershell.exe" if is_powershell else "cmd.exe"
        return basename(getenv("SHELL", "/bin/sh"))

    def build_cmd_prompt(self) -> str:
        """Build command prompt
        Returns:
            str: command prompt
        Raises:
            typer.Exit: if there is an error with the request
        """
        _os = self.detect_os()
        _shell = self.detect_shell()
        return f"""Your are a Shell Command Generator.
Generate a command EXCLUSIVELY for {_os} OS with {_shell} shell.
Rules:
1. Use ONLY {_shell}-specific syntax and connectors (&&, ||, |, etc)
2. Output STRICTLY in plain text format
3. NEVER use markdown, code blocks or explanations
4. Chain multi-step commands in SINGLE LINE
5. Return NOTHING except the ready-to-run command"""

    def build_default_prompt(self) -> str:
        """Build default prompt
        Returns:
            str: default prompt
        Raises:
            typer.Exit: if there is an error with the request
        """
        _os = self.detect_os()
        _shell = self.detect_shell()
        return (
            "You are yaili, a system management and programing assistant, "
            f"You are managing {_os} operating system with {_shell} shell. "
            "Your responses should be concise and use Markdown format, "
            "unless the user explicitly requests more details."
        )

    def get_default_config(self) -> dict[str, str]:
        """Get default configuration
        Returns:
            dict: default configuration with lowest priority
        """
        return DEFAULT_CONFIG.copy()

    def _ensure_config_file_exists(self):
        """Ensure the configuration file exists, creating it if necessary."""
        if not self.CONFIG_PATH.exists():
            self.console.print(
                "[bold yellow]Configuration file not found. Creating default configuration file.[/bold yellow]"
            )
            self.CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
            with open(self.CONFIG_PATH, "w") as f:
                f.write(self.DEFAULT_CONFIG_INI)

    def _load_config_from_file(self, config: dict):
        """Load configuration from the INI file and update the config dict."""
        config_parser = CasePreservingConfigParser()
        config_parser.read(self.CONFIG_PATH)
        if "core" in config_parser:
            for key, value in config_parser["core"].items():
                if value.strip():  # Only use non-empty values
                    config[key] = value

    def _override_config_with_env(self, config: dict):
        """Override configuration with environment variables."""
        for config_key, env_var in ENV_VAR_MAPPING.items():
            env_value = getenv(env_var)
            if env_value is not None:
                config[config_key] = env_value

    def _setup_api_key(self, config: dict):
        """Set the litellm API key based on config or environment variables."""
        api_key = config.get("API_KEY")
        if api_key:
            litellm.api_key = api_key
            return

        # Try common environment variables if not in config
        env_keys = ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "COHERE_API_KEY", "GEMINI_API_KEY"]
        for key in env_keys:
            env_value = getenv(key)
            if env_value:
                litellm.api_key = env_value
                config["API_KEY"] = env_value # Store the found key back in config for potential reuse
                return

        self.console.print(
            "[red]API Key not found. Please set it in the configuration file or environment variables (e.g., OPENAI_API_KEY).[/red]"
        )
        raise typer.Exit(code=1)

    def load_config(self) -> dict[str, str]:
        """Load LLM API configuration with priority:
        1. Environment variables (highest priority)
        2. Configuration file
        3. Default values (lowest priority)

        Returns:
            dict: merged configuration
        """
        # Start with default configuration (lowest priority)
        merged_config = self.get_default_config()

        # Ensure config file exists and load from it (middle priority)
        self._ensure_config_file_exists()
        self._load_config_from_file(merged_config)

        # Override with environment variables (highest priority)
        self._override_config_with_env(merged_config)

        # Ensure STREAM is lowercase string
        merged_config["STREAM"] = str(merged_config.get("STREAM", "true")).lower()

        # Set up the API key for litellm
        self._setup_api_key(merged_config)

        self.config = merged_config
        return self.config

    def build_data(self, prompt: str, mode: str = ModeEnum.TEMP.value) -> list[dict]:
        """Build request messages for litellm
        Args:
            prompt: user input
            mode: chat or execute mode
        Returns:
            list[dict]: List of messages for litellm completion
        """
        if mode == ModeEnum.EXECUTE.value:
            system_prompt = self.build_cmd_prompt()
        else:
            system_prompt = self.build_default_prompt()

        # Build messages list, first add system prompt
        messages = [{"role": "system", "content": system_prompt}]

        # Add history records in chat mode
        if mode == ModeEnum.CHAT.value and self.history:
            messages.extend(self.history)

        # Add current user message
        messages.append({"role": "user", "content": prompt})

        return messages  # Return list of messages directly

    def stream_response(self, response_stream) -> str:
        """Stream response from LLM API using litellm stream
        Args:
            response_stream: litellm completion stream iterator
        Returns:
            str: full completion text
        """
        full_completion = ""
        # Streaming response loop
        with Live(console=self.console) as live:
            for chunk in response_stream:
                # Refined check for litellm stream chunk structure
                try:
                    content = chunk.choices[0].delta.content
                    if content is not None:  # Explicitly check for None
                        full_completion += content
                        markdown = Markdown(markup=full_completion)
                        live.update(markdown, refresh=True)
                except (AttributeError, IndexError, TypeError):
                     # Ignore chunks that don't match the expected structure
                     if self.verbose:
                         self.console.print(f"[yellow]Skipping unexpected stream chunk: {chunk}[/yellow]")
                     continue
                time.sleep(0.01)  # Small delay for smoother streaming

        return full_completion

    def call_llm_api(self, prompt: str) -> str:
        """Call LLM API using litellm, return streaming output
        Args:
            prompt: user input
        Returns:
            str: streaming output
        """
        messages = self.build_data(prompt)
        stream = self.config.get("STREAM", "true") == "true"

        try:
            response = litellm.completion(
                model=self.config["MODEL"],
                messages=messages,
                stream=stream,
                api_base=self.config.get("BASE_URL"),
                temperature=0.7,
                top_p=0.7,
                max_tokens=2000,  # Increased max_tokens for potentially longer responses
            )
        except Exception as e:  # Catch broader exceptions from litellm
            self.console.print(f"[red]Error calling LiteLLM API: {e}[/red]")
            if self.verbose:
                self.console.print(f"LiteLLM Error Details: {e}")  # Print more details if verbose
            raise typer.Exit(code=1) from None

        self.console.print("[bold green]Assistant:[/bold green]")
        if stream:
            assistant_response = self.stream_response(response)  # Stream the response
        else:
            # Handle non-streaming response with refined checks
            try:
                assistant_response = response.choices[0].message.content or "" # Ensure it's a string
            except (AttributeError, IndexError, TypeError):
                 assistant_response = "" # Default to empty string if structure is unexpected
            self.console.print(Markdown(markup=assistant_response))

        self.console.print()  # Add a newline after the completion

        return assistant_response

    def get_command_from_llm(self, prompt: str) -> Optional[str]:
        """Request Shell command from LLM using litellm
        Args:
            prompt: user input
        Returns:
            str: shell command or None if error
        """
        messages = self.build_data(prompt, mode=ModeEnum.EXECUTE.value)

        try:
            response = litellm.completion(
                model=self.config["MODEL"],
                messages=messages,
                stream=False,  # Always non-streaming for command generation
                api_base=self.config.get("BASE_URL"),
                temperature=0.2,  # Lower temperature for more deterministic command output
                top_p=0.5,
                max_tokens=150,
            )
        except Exception as e:
            self.console.print(f"[red]Error calling LiteLLM API for command: {e}[/red]")
            return None

        # Ensure response structure is as expected before accessing content
        try:
            content = response.choices[0].message.content
            return content.strip() if content else None
        except (AttributeError, IndexError, TypeError):
            self.console.print("[red]Failed to get command from LLM (unexpected response structure).[/red]")
            return None

    def execute_shell_command(self, command: str) -> int:
        """Execute shell command
        Args:
            command: shell command
        Returns:
            int: return code
        """
        self.console.print(f"\n[bold green]Executing command: [/bold green] {command}\n")
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            self.console.print(
                f"\n[bold red]Command failed with return code: {result.returncode}[/bold red]"
            )
        return result.returncode

    def get_prompt_tokens(self):
        """Get prompt tokens based on current mode
        Returns:
            list: prompt tokens for prompt_toolkit
        """
        if self.current_mode == ModeEnum.CHAT.value:
            qmark = "💬"
        elif self.current_mode == ModeEnum.EXECUTE.value:
            qmark = "🚀"
        else:
            qmark = ""
        return [("class:qmark", qmark), ("class:question", " {} ".format(">"))]

    def chat_mode(self, user_input: str):
        """
        This method handles the chat mode.
        It adds the user input to the history and calls the API to get a response.
        It then adds the response to the history and manages the history length.
        Args:
            user_input: user input
        Returns:
            ModeEnum: current mode
        """
        if self.current_mode != ModeEnum.CHAT.value:
            return self.current_mode

        # Add user message to history
        self.history.append({"role": "user", "content": user_input})

        # Call API and get response
        assistant_response = self.call_llm_api(user_input)

        # Add assistant response to history
        if assistant_response:
            self.history.append({"role": "assistant", "content": assistant_response})

        # Manage history length, keep recent conversations
        if (
            len(self.history) > self.max_history_length * 2
        ):  # Each conversation has user and assistant messages
            self.history = self.history[-self.max_history_length * 2 :]

        return ModeEnum.CHAT.value

    def _filter_command(self, command: str) -> Optional[str]:
        """Filter out unwanted characters from command

        The LLM may return commands in markdown format with code blocks.
        This method removes markdown formatting from the command.
        It handles various formats including:
        - Commands surrounded by ``` (plain code blocks)
        - Commands with language specifiers like ```bash, ```zsh, etc.
        - Commands with specific examples like ```ls -al```

        example:
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

    def execute_mode(self, user_input: str):
        """
        This method generates a shell command from the user input and executes it.
        If the user confirms the command, it is executed.
        Args:
            user_input: user input
        Returns:
            ModeEnum: current mode
        """
        if user_input == "" or self.current_mode != ModeEnum.EXECUTE.value:
            return self.current_mode

        command = self.get_command_from_llm(user_input)
        if not command:
            self.console.print("[bold red]No command generated[/bold red]")
            return self.current_mode
        command = self._filter_command(command)
        if not command:
            self.console.print("[bold red]No command generated[/bold red]")
            return self.current_mode
        self.console.print(f"\n[bold magenta]Generated command:[/bold magenta] {command}")
        confirm = Confirm.ask("Execute this command?")
        if confirm:
            self.execute_shell_command(command)
        return ModeEnum.EXECUTE.value

    def run_repl_loop(self):
        while True:
            user_input = self.session.prompt(self.get_prompt_tokens)
            # Skip empty input
            if not user_input.strip():
                continue

            if user_input.lower() in ("/exit", "/quit", "/q"):
                break

            # Handle special commands
            if self.current_mode == ModeEnum.CHAT.value:
                if user_input.lower() == "/clear":
                    self.clear_history()
                    self.console.print("[bold yellow]Chat history cleared[/bold yellow]\n")
                    continue
                else:
                    self.chat_mode(user_input)
            elif self.current_mode == ModeEnum.EXECUTE.value:
                self.execute_mode(user_input)

        self.console.print("[bold green]Exiting...[/bold green]")

    def run_one_shot(self, prompt: str):
        """Run one-shot mode with given prompt
        Args:
            prompt (str): Prompt to send to LLM
        Returns:
            None
        """
        if self.current_mode == ModeEnum.EXECUTE.value:
            self.execute_mode(prompt)  # Execute mode for one-shot prompt
        else:
            self.call_llm_api(prompt)

    def run(self, chat=False, shell=False, prompt: Optional[str] = None):
        """Run the CLI application
        Args:
            chat (bool): Whether to run in chat mode
            shell (bool): Whether to run in shell mode
            prompt (Optional[str]): Prompt send to LLM

        Returns:
            None
        """
        # Load configuration
        self.config = self.load_config()
        if not self.config.get("API_KEY", None):
            self.console.print(
                "[red]API key not found. Please set it in the configuration file.[/red]"
            )
            return

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
            self.console.print(f"[bold yellow]Using model: {self.config['MODEL']}[/bold yellow]")

        if self.current_mode in (ModeEnum.TEMP.value, ModeEnum.EXECUTE.value) and prompt:
            self.run_one_shot(prompt)
        elif self.current_mode == ModeEnum.CHAT.value:
            self.run_repl_loop()
