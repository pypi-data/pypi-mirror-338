"""
Optional configuration validation logic.
"""
from omegaconf import DictConfig
from forged.__exceptions__ import ConfiguredException

def validate_config(cfg: DictConfig) -> None:
    # Example: check that if debug is true, logging.level is set to DEBUG
    if cfg.get("debug", False) and cfg.get("logging", {}).get("level", "").upper() != "DEBUG":
        print("Warning: debug mode is enabled but logging.level is not set to DEBUG.")
    # Extend with more validation rules as needed.

