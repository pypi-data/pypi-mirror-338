from logging import Formatter, LogRecord
from typing import override
from dataclasses import dataclass

from ..log import Log


@dataclass(slots=True)
class StandardFormatter(Formatter):
    @override
    def format(self, record: LogRecord) -> str:
        log = Log.from_record(record, formatter=self)
        return f"{log.serialize_timestamp(log.timestamp)} [{log.level}]:\t{log.message}"
