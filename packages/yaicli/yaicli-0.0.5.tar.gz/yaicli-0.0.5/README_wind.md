# YAICLI - Your AI Command Line Interface

YAICLI is a powerful command-line AI assistant tool that allows you to interact with Large Language Models (LLMs) through your terminal. It provides multiple operation modes for daily conversations, generating and executing shell commands, and quick one-time queries.

## Features

### Multiple Operation Modes

1. **Chat Mode**
   - Interactive conversation interface
   - Markdown-formatted responses
   - Streaming output display

2. **Execute Mode**
   - Automatically generates shell commands from natural language descriptions
   - Detects current operating system and shell environment to generate appropriate commands
   - Automatically filters unnecessary Markdown formatting from command output
   - Confirmation mechanism before execution for safety

3. **Temp Mode (One-shot)**
   - Quick single queries without maintaining a session

### Intelligent Environment Detection

- Automatically detects operating system (Windows, MacOS, Linux and its distributions)
- Automatically detects shell type (bash, zsh, PowerShell, cmd, etc.)
- Customizes prompts and commands based on your environment

### User Experience

- Streaming response display for real-time AI output viewing
- Keyboard shortcuts (e.g., Ctrl+I to switch modes)
- Command confirmation mechanism to prevent accidental execution

## Requirements

- Python 3.9+
- Supported operating systems: Windows, MacOS, Linux

## Dependencies

```
configparser
json
platform
subprocess
time
jmespath
requests
typer
distro
prompt_toolkit
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yaicli.git
   cd yaicli
   ```

2. Create virtual environment and install dependencies:
   ```bash
   uv sync
   ```


## Configuration

The first time you run YAICLI, it will create a default configuration file at `~/.config/yaicli/config.ini`. You'll need to edit this file and add your API key.

Example configuration file:

```ini
[core]
BASE_URL=https://api.openai.com/v1
API_KEY=your-api-key-here
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
STREAM=true
```

## Usage

### Basic Usage

```bash
# One-shot mode (default): Send a prompt and get a response
ai "How do I check memory usage on a Linux system?"

# Chat mode: Start an interactive chat session
ai --chat

# Execute mode: Generate and execute shell commands
ai --shell "Create a directory named project and create src and docs subdirectories in it"

# Enable verbose output
ai --verbose "Explain how Docker works"
```

### Interactive Commands

In chat or execute mode:

- Press `Ctrl+I` to switch between chat and execute modes
- Type `exit` or `quit` to exit the application

### Mode Descriptions

1. **Chat Mode (--chat)**
   ```bash
   ai --chat
   ```
   Starts an interactive session where you can converse with the AI. Responses will be displayed in Markdown format.

2. **Execute Mode (--shell)**
   ```bash
   ai --shell "Find all files larger than 100MB"
   ```
   The AI will generate appropriate shell commands and execute them after your confirmation.

3. **One-shot Mode (default)**
   ```bash
   ai "Explain the difference between TCP and UDP"
   ```
   Sends a single query, provides the response, and exits.

## Advanced Usage

### Custom System Recognition

If you want to specify a particular operating system or shell, you can modify the configuration file:

```ini
[core]
# ...other configuration...
SHELL_NAME=bash  # Force bash shell command syntax
OS_NAME=Ubuntu   # Force commands targeting Ubuntu
```

### Custom API Endpoint

YAICLI uses the OpenAI API by default, but you can use compatible APIs by modifying the configuration:

```ini
[core]
BASE_URL=https://your-api-endpoint/v1
COMPLETION_PATH=/chat/completions
ANSWER_PATH=custom.json.path.to.content
```

## Technical Implementation

YAICLI is built using several Python libraries:

- **Typer**: Provides the command-line interface
- **prompt_toolkit**: Provides interactive command-line input experience
- **requests**: Handles API requests
- **jmespath**: Parses JSON responses

## Limitations and Notes

- Requires a valid OpenAI API key or compatible API
- Commands generated in execute mode should be carefully reviewed before execution
- API calls may incur charges depending on your service provider and model

## Contributing

Contributions of code, issue reports, or feature suggestions are welcome.

## License

Apache License 2.0

---

*YAICLI - Making your terminal smarter*
