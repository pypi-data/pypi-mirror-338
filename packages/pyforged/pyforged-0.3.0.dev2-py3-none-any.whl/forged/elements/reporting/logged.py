import sys
import os
import json
import logging
import warnings
from loguru import logger
from pathlib import Path
from datetime import datetime
from typing import Any, Callable, Union, Dict, List
from logging import LogRecord


def default_format(record: Dict[str, Any]) -> str:
    return (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level:<8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>\n"
        "{exception}"
    )


def json_format(record: Dict[str, Any]) -> str:
    record_dict = {
        "time": record["time"].isoformat(),
        "level": record["level"].name,
        "name": record["name"],
        "function": record["function"],
        "line": record["line"],
        "message": record["message"],
        "exception": str(record["exception"]) if record["exception"] else None,
    }
    return json.dumps(record_dict)


class InterceptHandler(logging.Handler):
    def emit(self, record: LogRecord):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        frame, depth = logging.currentframe(), 2
        while frame and frame.f_globals["__name__"] == __name__:
            frame = frame.f_back
            depth += 1
        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup_logger(  # TODO: Add source alternative to method/module name?
    sinks: List[Dict[str, Any]],
    override_std: bool = True,
    catch_exceptions: bool = True,
):
    """
    Initialize loguru logger with multiple custom sink configurations.

    Each sink config is a dict containing:
      - sink: destination (file path, sys.stdout, function, etc.)
      - level: log level
      - format: string or callable (will be wrapped correctly)
      - rotation, retention, compression, etc. (optional)
    """
    logger.remove()

    for config in sinks:
        config = config.copy()  # so we don't mutate caller's dict

        sink = config.pop("sink")

        fmt = config.get("format")
        if callable(fmt):
            # Wrap callable formatter for Loguru
            config["format"] = lambda record, f=fmt: f(record)

        logger.add(sink, **config)

    if override_std:
        logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
        warnings.showwarning = lambda *args, **kwargs: logger.warning(
            warnings.formatwarning(*args, **kwargs)
        )

    if catch_exceptions:
        def handle_exception(exc_type, exc_value, exc_traceback):
            if issubclass(exc_type, KeyboardInterrupt):
                sys.__excepthook__(exc_type, exc_value, exc_traceback)
                return
            logger.opt(exception=(exc_type, exc_value, exc_traceback)).critical("Uncaught exception")
        sys.excepthook = handle_exception

    logger.debug("Logger initialized with arbitrary sinks")


if __name__ == '__main__':
    setup_logger([
        {
            "sink": sys.stdout,
            "level": "INFO",
            "format": "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
                      "<level>{level:<8}</level> | "
                      "<level>{message}</level>"
                      "{exception}",
            "colorize": True,
        },
        {
            "sink": f"logs/pyforged-{datetime.today().date()}.logs",
            "level": "DEBUG",
            "format": default_format,
            "rotation": "5 MB",
            "retention": "7 days",
            "compression": "zip",
            "enqueue": True,
        }
    ])

