from __future__ import annotations

from pathlib import Path
from logging import Handler

from pydantic import ConfigDict, Field, field_serializer, field_validator, ValidationError, BaseModel
from pydantic.alias_generators import to_camel

from ...formatter.lib.consts import FormatterName
from .consts import AtomicHandlerName, LoggingStream, DEFAULT_LOG_FILE_BACKUPS, DEFAULT_MAXIMUM_LOG_FILE_BYTES, DEFAULT_LOG_FILE_PATH
from ...log.lib.consts import LoggingLevel
from ...filter.lib.consts import FilterName
from .utils import import_qualified_name


class HandlerModel[T: FilterName](BaseModel):
    handler_class: type[Handler] = Field(serialization_alias="class")
    filters: list[T] | None = None

    @field_serializer("handler_class")
    def serialize_handler(self, handler_class: type[Handler]) -> str:
        return f"{handler_class.__module__}.{handler_class.__name__}"
    
    @field_validator("handler_class", mode="before")
    @classmethod
    def resolve_handler_class(cls, value: object) -> type[Handler]:
        if value is None:
            return Handler
        if isinstance(value, type) and issubclass(value, Handler):
            return value
        if not isinstance(value, str):
            raise ValidationError("Field 'class' must be given a string or None.")
        handler_class = import_qualified_name(value)
        if isinstance(handler_class, type) and issubclass(handler_class, Handler):
            return handler_class
        raise ValidationError(f"Could not resolve {value!r} to handler class.")
    
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        alias_generator=to_camel,
    )


class AtomicHandlerSchema[T_FilterName: FilterName, T_FormatterName: FormatterName](HandlerModel[T_FilterName]):
    formatter: T_FormatterName
    level: LoggingLevel


class CompositeHandlerSchema[T_AtomicHandlerName: AtomicHandlerName, T_FilterName: FilterName](HandlerModel[T_FilterName]):
    handlers: list[T_AtomicHandlerName]


class StreamHandlerSchema[T_FilterName: FilterName, T_FormatterName: FormatterName](AtomicHandlerSchema[T_FilterName, T_FormatterName]):
    stream: LoggingStream


class FileHandlerSchema[T_FilterName: FilterName, T_FormatterName: FormatterName](AtomicHandlerSchema[T_FilterName, T_FormatterName]):
    file_name: Path = Field(serialization_alias="filename", default=DEFAULT_LOG_FILE_PATH)
    max_bytes: int = DEFAULT_MAXIMUM_LOG_FILE_BYTES
    backup_count: int = DEFAULT_LOG_FILE_BACKUPS


class QueueHandlerSchema[T_AtomicHandlerName: AtomicHandlerName, T_FilterName: FilterName](CompositeHandlerSchema[T_AtomicHandlerName, T_FilterName]):
    respect_handler_level: bool = True

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        alias_generator=None,
    )
