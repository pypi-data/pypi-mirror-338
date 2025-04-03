"""
Defines the abstract base class for all configuration sources.
"""

from abc import ABC, abstractmethod
from omegaconf import DictConfig

class ConfigSource(ABC):
    @abstractmethod
    def load(self) -> DictConfig:
        """
        Load the configuration and return it as an OmegaConf DictConfig.
        """
        pass
