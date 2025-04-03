from forged.__exceptions__ import ConfiguredException
"""
Loads configuration from environment variables.
Optionally, it can filter variables by a prefix (default "APP_").
"""
import os
from omegaconf import OmegaConf, DictConfig
from loguru import logger
from forged.elements.configured.sources.base import ConfigSource

class EnvConfigSource(ConfigSource):
    """
    Loads configuration from environment variables by filtering those with a prefix.

    :param prefix: The prefix to filter environment variables. Defaults to **"APP_"**


    """
    def __init__(self, prefix: str | None = "APP_"):
        self.prefix = prefix

    def load(self) -> DictConfig:
        env_cfg = {}  # TODO: Rename to avoid the name shadowing
        logger.debug(f"Pulling {len(os.environ)} environment variables.{' No prefix filtering.' if not self.prefix else ' Prefix filtering with '} {self.prefix if self.prefix else ''}")
        for key, value in os.environ.items():
            if self.prefix:
                if key.startswith(self.prefix):
                    logger.debug(f"Env Var. Prefix Matched: {key}={value}")
                    # Remove the prefix for the config key
                    cfg_key = key[len(self.prefix):].lower()
                    env_cfg[cfg_key] = value
            else:
                env_cfg[key] = value
        logger.success(f"Loaded {len(env_cfg)} environment variables{'.' if not self.prefix else ' with the prefix'} {self.prefix if self.prefix else ''}")
        return OmegaConf.create(env_cfg)

if __name__ == '__main__':
    os.environ.update({
        "FORGED_TEST_KEY": "test_value",
        "FORGED_ANOTHER_KEY": "another_value"
    })
    test = EnvConfigSource('FORGED_')
    env_cfg = test.load()
    print(env_cfg)