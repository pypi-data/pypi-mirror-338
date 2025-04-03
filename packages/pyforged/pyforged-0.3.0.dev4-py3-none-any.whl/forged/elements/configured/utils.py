"""
Utility functions for working with configurations.
"""
from forged.__exceptions__ import ConfiguredException

def redact_secrets(cfg, secret_keys=("password", "api_key", "secret")):
    """
    Walk through a config dictionary and replace sensitive values with a placeholder.
    """
    if isinstance(cfg, dict):
        return {k: ("***" if any(sk in k.lower() for sk in secret_keys) else redact_secrets(v, secret_keys))
                for k, v in cfg.items()}
    elif isinstance(cfg, list):
        return [redact_secrets(item, secret_keys) for item in cfg]
    else:
        return cfg
