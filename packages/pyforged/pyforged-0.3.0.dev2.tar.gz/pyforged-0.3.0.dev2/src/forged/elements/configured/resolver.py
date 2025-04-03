"""
Registers custom resolvers for OmegaConf.
"""
import os
from forged.__exceptions__ import ConfiguredException
from omegaconf import OmegaConf, DictConfig
from loguru import logger


def register_resolvers():  # TODO: add more resolvers
    # Environment variable resolver: ${env:VAR_NAME}
    logger.debug("Registering custom 'env' resolver.")
    if not OmegaConf.has_resolver("env"):
        OmegaConf.register_new_resolver("env", lambda key: os.getenv(key, ""))
    # OmegaConf.register_new_resolver("secret", lambda key: fetch_secret(key))


def resolve_env_vars(config: dict) -> dict | DictConfig:
    """
    Resolve environment variables in the configuration dictionary.
    """
    config = OmegaConf.create(config)
    resolved_config = DictConfig({})
    for key, value in config.items():
        if isinstance(value, str) and value.startswith("$"):
            env_var = value[1:]
            resolved_config[key] = os.getenv(env_var, value)
        else:
            resolved_config[key] = value
    return resolved_config

def resolve_secrets(config: dict, secrets: dict) -> dict:
    """
    Resolve secrets in the configuration dictionary.
    """
    resolved_config = config.copy()
    for key, value in secrets.items():
        if key in resolved_config:
            resolved_config[key] = value
    return resolved_config


if __name__ == '__main__':
    # Register the custom resolvers
    register_resolvers()

    # Example configuration dictionary with environment variable placeholders
    example_config = {
        "api_key": "${env:API_KEY}",
        "db_host": "${env:DB_HOST}",
        "db_port": "${env:DB_PORT}"
    }

    # Set some environment variables for testing
    os.environ["API_KEY"] = "test_api_key"
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_PORT"] = "5432"

    # Resolve the environment variables in the configuration
    resolved_config = resolve_env_vars(example_config)

    # Print the resolved configuration
    print(OmegaConf.to_yaml(resolved_config))