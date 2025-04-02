from functools import total_ordering
from enum import StrEnum
from logging import CRITICAL, FATAL, ERROR, WARN, WARNING, INFO, DEBUG, NOTSET, _levelToName, _nameToLevel


@total_ordering
class LoggingLevel(StrEnum):
    CRITICAL = _levelToName[CRITICAL]
    FATAL = _levelToName[FATAL]
    ERROR = _levelToName[ERROR]
    WARN = _levelToName[WARN]
    WARNING = _levelToName[WARNING]
    INFO = _levelToName[INFO]
    DEBUG = _levelToName[DEBUG]
    NOTSET = _levelToName[NOTSET]

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, LoggingLevel):
            return NotImplemented
        return _nameToLevel[self.value] < _nameToLevel[other.value]
