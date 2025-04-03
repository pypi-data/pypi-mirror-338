from enum import StrEnum

# Default configuration template
DEFAULT_CONFIG_INI = """[core]
BASE_URL=https://api.openai.com/v1
API_KEY=
MODEL=gpt-4o

# auto detect shell and os
SHELL_NAME=auto
OS_NAME=auto

# true: streaming response
# false: non-streaming response
STREAM=true"""

class ModeEnum(StrEnum):
    CHAT = "chat"
    EXECUTE = "exec"
    TEMP = "temp"
