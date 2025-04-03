from forged.__exceptions__ import ConfiguredException
"""
Implements a file-based config source using YAML.
"""
import os
from omegaconf import OmegaConf, DictConfig
from .base import ConfigSource

class FileConfigSource(ConfigSource):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load(self) -> DictConfig:  # TODO: Utilise common file loader
        if not os.path.exists(self.filepath):
            # In production, you might want to warn or handle missing files differently.
            return OmegaConf.create({})
        return OmegaConf.load(self.filepath)
