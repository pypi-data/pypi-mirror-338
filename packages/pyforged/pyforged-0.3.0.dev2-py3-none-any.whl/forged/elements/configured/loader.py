"""
loader.py
----------
Defines the core function to load and merge configuration from different sources.
"""

import os
from omegaconf import OmegaConf, DictConfig
from forged.elements.configured.sources.file import FileConfigSource
from forged.elements.configured.sources.env import EnvConfigSource
from forged.elements.configured.sources.cli import CliConfigSource
from forged.elements.configured.resolver import register_resolvers
from forged.elements.configured.hooks import run_hooks

def load_config(
    base_files: list[str] = None,
    env: str = None,
    use_cli: bool = False,
    use_secrets: bool = False,  # placeholder, not implemented in this minimal
    overrides: dict = None
) -> DictConfig:
    """
    Load configuration by merging multiple sources:
    - Base config files
    - Environment-specific config
    - Environment variables
    - CLI arguments
    - Additional overrides
    """
    # First, register any custom resolvers (e.g., env, secrets)
    register_resolvers()

    # Pre-load hook
    run_hooks("on_before_load")  # TODO: Integrarte with native hook element

    config_sources = []

    # Load base files from disk
    if base_files:
        for file_path in base_files:
            file_source = FileConfigSource(file_path)
            cfg = file_source.load()
            config_sources.append(cfg)

    # Merge all file-based configs
    if config_sources:
        cfg = OmegaConf.merge(*config_sources)
    else:
        cfg = OmegaConf.create({})

    # Environment-specific config: e.g., load file based on provided env
    if env:
        env_file = f"{env}.yaml"
        file_source = FileConfigSource(env_file)
        cfg = OmegaConf.merge(cfg, file_source.load())

    # Load environment variables (optional filtering by prefix could be added)
    env_source = EnvConfigSource(prefix="APP_")
    cfg = OmegaConf.merge(cfg, env_source.load())

    # Load CLI arguments if desired
    if use_cli:
        cli_source = CliConfigSource()
        cli_cfg = cli_source.load()
        cfg = OmegaConf.merge(cfg, cli_cfg)

    # Additional overrides passed as a dict
    if overrides:
        override_cfg = OmegaConf.create(overrides)
        cfg = OmegaConf.merge(cfg, override_cfg)

    # Post-load hook
    run_hooks("on_after_load", cfg)

    return cfg
