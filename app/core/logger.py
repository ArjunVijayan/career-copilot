import logging
from logging import Logger


def get_logger(name: str | None = None, level: int = logging.INFO) -> Logger:
    """Return a configured logger for the given name."""
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(level)

        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s [%(name)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False

    return logger
