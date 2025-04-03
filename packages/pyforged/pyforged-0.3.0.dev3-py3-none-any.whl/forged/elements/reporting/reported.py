import sys
from datetime import datetime

from forged.elements.reporting.logged import logger, setup_logger, default_format as def_log_format
from forged.commons.utilities.host import get_temp_dir, get_home_dir

setup_logger([
        {
            "sink": sys.stdout,
            "level": "DEBUG",
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                      "<level>{level:<8}</level> | "
                      "<level>{message}</level>"
                      "{exception}",
            "colorize": True,
        },
        {
            "sink": f"{get_temp_dir()}/pyforged-{datetime.today().date()}.logs",  # TODO: Dynamic log folder
            "level": "DEBUG",
            "format": def_log_format,
            "rotation": "5 MB",
            "retention": "7 days",
            "compression": "zip",
            "enqueue": True,
        }
    ])

logger.success("Logging active")