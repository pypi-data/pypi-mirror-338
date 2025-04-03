from forged.__exceptions__ import ConfiguredException
"""
Provides a simple hook mechanism to run callbacks before and after config load.
"""
from typing import Callable, List
from omegaconf import DictConfig

# Define hook registries
_on_before_load: List[Callable[[], None]] = []
_on_after_load: List[Callable[[DictConfig], None]] = []

def register_hook(hook_name: str, callback: Callable):
    if hook_name == "on_before_load":
        _on_before_load.append(callback)
    elif hook_name == "on_after_load":
        _on_after_load.append(callback)
    else:
        raise ValueError(f"Unknown hook: {hook_name}")

def run_hooks(hook_name: str, *args, **kwargs):
    if hook_name == "on_before_load":
        for callback in _on_before_load:
            callback()
    elif hook_name == "on_after_load":
        for callback in _on_after_load:
            callback(*args, **kwargs)
