from sparse_transform.qsft import qsft
import logging

# Package-level logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)  # Default to WARNING

# Default logging setup
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def set_logging_level(level):
    """Set the logging level for the entire package."""
    level = level.upper() if isinstance(level, str) else level
    logger.setLevel(level)

    for handler in logger.handlers:
        handler.setLevel(level)

    logger.info(f"Logging level set to {logger.getEffectiveLevel()}")

__all__ = [
    "qsft",
    "set_logging_level",
]