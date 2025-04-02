from logging import Filter, LogRecord
from typing import override
from dataclasses import dataclass

from ..log.lib.consts import LoggingLevel


@dataclass(slots=True)
class ErrorFilter(Filter):
    @override
    def filter(self, record: LogRecord) -> bool:
        return LoggingLevel(record.levelname) < LoggingLevel.ERROR
