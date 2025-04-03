from forged.__exceptions__ import ConfiguredException
"""
Loads configuration overrides from command-line arguments using OmegaConf.
"""
from omegaconf import OmegaConf, DictConfig
from .base import ConfigSource

class CliConfigSource(ConfigSource):
    def load(self) -> DictConfig:
        # OmegaConf.from_cli() parses sys.argv for overrides like "key=value"
        # This is a basic implementation; you might want to integrate with argparse or click.
        return OmegaConf.from_cli()
