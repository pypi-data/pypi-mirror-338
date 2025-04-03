from enum import StrEnum
from pathlib import Path


MEBI = 1_024 * 1_024
DEFAULT_MAXIMUM_LOG_FILE_BYTES = 10 * MEBI
DEFAULT_LOG_FILE_BACKUPS = 3
DEFAULT_LOG_FILE_EXTENSION = "jsonl"
DEFAULT_LOG_FILE_PATH = Path(f"./logging/logs/log.{DEFAULT_LOG_FILE_EXTENSION}")


class LoggingStream(StrEnum):
    STANDARD_OUT = "ext://sys.stdout"
    STANDARD_ERROR = "ext://sys.stderr"


class AtomicHandlerName(StrEnum):
    pass


class CompositeHandlerName(StrEnum):
    pass
