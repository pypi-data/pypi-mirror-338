from configparser import RawConfigParser
from pathlib import Path

from yaiclipy.const import DEFAULT_CONFIG_INI


class CasePreservingConfigParser(RawConfigParser):
    def optionxform(self, optionstr):
        return optionstr



class ConfigManager(dict):
    """Manage configuration for YAICLI"""

    # Configuration file path
    CONFIG_PATH = Path("~/.config/yaicli/config.ini").expanduser()

    def __init__(self):
        self.load()

    def _ensure_config_file_exists(self):
        """Ensure the configuration file exists, creating it if necessary."""
        if not self.CONFIG_PATH.exists():
            self.CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
            with open(self.CONFIG_PATH, "w") as f:
                f.write(DEFAULT_CONFIG_INI)

    def load(self) -> dict[str, str]:
        """Load configuration from the INI file and update the config dict."""
        self._ensure_config_file_exists()
        config_parser = CasePreservingConfigParser()
        config_parser.read(self.CONFIG_PATH)
        if "core" in config_parser:
            for key, value in config_parser["core"].items():
                if value.strip():  # Only use non-empty values
                    self[key] = value
        return self
