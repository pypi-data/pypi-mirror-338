"""
Defines structured configuration schemas using dataclasses.
"""
from dataclasses import dataclass
from typing import Optional
from forged.__exceptions__ import ConfiguredException

@dataclass
class LoggingConfig:
    level: str = "INFO"
    file: Optional[str] = None
