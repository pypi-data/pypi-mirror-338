from logging import Formatter, LogRecord
from typing import override
from dataclasses import dataclass
from json import dumps

from ..log import Log


@dataclass(slots=True)
class JSONFormatter(Formatter):
    @override
    def format(self, record: LogRecord) -> str:
        return dumps(
            Log.from_record(record, formatter=self)
            .model_dump(mode="json", exclude_none=True)
        )
