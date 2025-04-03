from forged.__exceptions__ import ConfiguredException
"""
Provides a high-level ConfigManager to encapsulate the configuration lifecycle.
"""
from omegaconf import DictConfig
from forged.elements.configured.loader import load_config
from forged.elements.configured.validators import validate_config

class ConfigManager:
    def __init__(
        self,
        base_files: list[str] = None,
        env: str = None,
        use_cli: bool = False,
        use_secrets: bool = False,
        overrides: dict = None
    ):
        self.base_files = base_files or []
        self.env = env
        self.use_cli = use_cli
        self.use_secrets = use_secrets
        self.overrides = overrides or {}
        self.config: DictConfig = None

    def load(self) -> DictConfig:
        self.config = load_config(
            base_files=self.base_files,
            env=self.env,
            use_cli=self.use_cli,
            use_secrets=self.use_secrets,
            overrides=self.overrides
        )
        # Optionally, validate the config
        validate_config(self.config)
        return self.config

    def reload(self) -> DictConfig:
        return self.load()

    def save(self, path: str) -> None:
        from omegaconf import OmegaConf
        OmegaConf.save(self.config, path)

    def diff(self, other: DictConfig) -> dict:
        """
        Computes a diff between self.config and another configuration.
        (This is a placeholder; you can implement a more robust diff.)
        """
        diff = {}
        for key in self.config.keys():
            if key not in other or self.config[key] != other[key]:
                diff[key] = (self.config.get(key), other.get(key))
        return diff
