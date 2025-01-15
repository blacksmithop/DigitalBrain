import logging
import sys
from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel


class LoggerConfig(BaseModel):
    handlers: list
    format: str
    date_format: str | None = None
    logger_file: Path | None = None
    level: int = logging.INFO


LOGGER_FILE = Path("fastapi.log")  # where log is stored
DATE_FORMAT = "%d %b %Y | %H:%M:%S"
LOGGER_FORMAT = "%(asctime)s | %(message)s"

@lru_cache
def get_logger_config():
    """Installs RichHandler (Rich library) if not in production
    environment, or use the production log configuration.
    """

    from rich.logging import RichHandler

    output_file_handler = logging.FileHandler(LOGGER_FILE)
    handler_format = logging.Formatter(
        LOGGER_FORMAT, datefmt=DATE_FORMAT)
    output_file_handler.setFormatter(handler_format)

    return LoggerConfig(
        handlers=[
            RichHandler(
                rich_tracebacks=True,
                tracebacks_show_locals=True,
                show_time=False
            ),
            output_file_handler
        ],
        format="%(levelname)s: %(asctime)s \t%(message)s",
        date_format=DATE_FORMAT,
        logger_file=LOGGER_FILE,
    )



def setup_rich_logger():
    """Cycles through uvicorn root loggers to
    remove handler, then runs `get_logger_config()`
    to populate the `LoggerConfig` class with Rich
    logger parameters.
    """

    # Remove all handlers from root logger
    # and proprogate to root logger.
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True
    
    logger_config = get_logger_config()  # get Rich logging config

    logging.basicConfig(
        level=logger_config.level,
        format=logger_config.format,
        datefmt=logger_config.date_format,
        handlers=logger_config.handlers,
    )