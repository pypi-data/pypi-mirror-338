from enum import Enum, auto

class Severity(str, Enum):  # TODO: dynamically load custom
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

class Kind(str, Enum):  # TODO: dynamically load custom
    GENERAL = "general"
    VALIDATION = "validation"
    CONFIG = "config"
    RUNTIME = "runtime"
    DEPENDENCY = "dependency"
