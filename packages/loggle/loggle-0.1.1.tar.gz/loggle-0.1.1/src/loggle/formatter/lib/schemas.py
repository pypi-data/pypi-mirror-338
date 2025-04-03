from __future__ import annotations

from logging import LogRecord, Formatter
from pathlib import Path
from datetime import datetime, timezone
from typing import Self

from pydantic import BaseModel, ConfigDict, field_serializer, Field
from pydantic.alias_generators import to_camel

from ...filter.lib.consts import FilterName
from ...log.lib.consts import LoggingLevel
from ...lib import Factory


class FormatterModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
    )


class FormatterSchema(FormatterModel):
    format: str | None = None
    datefmt: str | None = None
    formatter_factory: Factory[Formatter] | None = Field(serialization_alias="()", default=None)
