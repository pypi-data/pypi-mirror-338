from __future__ import annotations

from logging import LogRecord, Formatter
from pathlib import Path
from datetime import datetime, timezone
from typing import Self

from pydantic import field_serializer

from .lib.consts import LoggingLevel
from .lib.schemas import JSONLogModel, JSONLogProcessSchema, JSONLogThreadSchema


class Log(JSONLogModel):
    timestamp: datetime
    level: LoggingLevel
    message: str
    file_path: Path
    line_number: int
    exception: str | None
    stack: str | None
    process: JSONLogProcessSchema
    thread: JSONLogThreadSchema
    logger: str

    @field_serializer("timestamp")
    def serialize_timestamp(self, timestamp: datetime) -> str:
        return timestamp.strftime(f"%d/%m/%Y %H:%M:%S.{timestamp.microsecond:>06}")
    
    @classmethod
    def from_record(cls, record: LogRecord, *, formatter: Formatter) -> Self:
        return cls(
            timestamp=datetime.fromtimestamp(record.created, tz=timezone.utc),
            level=LoggingLevel(record.levelname),
            message=record.getMessage(),
            file_path=Path(record.pathname).resolve(),
            line_number=record.lineno,
            exception=formatter.formatException(record.exc_info) if record.exc_info else None,
            stack=formatter.formatStack(record.stack_info) if record.stack_info else None,
            process=JSONLogProcessSchema(name=record.processName, id=record.process),
            thread=JSONLogThreadSchema(name=record.threadName, id=record.thread),
            logger=record.name,
        )
