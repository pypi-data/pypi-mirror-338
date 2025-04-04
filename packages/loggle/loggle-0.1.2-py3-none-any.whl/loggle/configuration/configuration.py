from __future__ import annotations

from typing import Literal, Self, Any, cast
from logging.config import dictConfig as dict_config
from pydantic import BaseModel

from ..filter import FilterName, FilterSchema
from ..formatter import FormatterSchema, FormatterName
from ..handler import HandlersDict, AtomicHandlerSchema, CompositeHandlerSchema, AtomicHandlerName, CompositeHandlerName
from ..logger import LoggerName, LoggerSchema, LoggersSchema


class Configuration[T_FilterName: FilterName, T_FormatterName: FormatterName, T_AtomicHandlerName: AtomicHandlerName, T_CompositeHandlerName: CompositeHandlerName, T_LoggerName: LoggerName](BaseModel):
    version: Literal[1]
    disable_existing_loggers: bool
    filters: dict[T_FilterName, FilterSchema]
    formatters: dict[T_FormatterName, FormatterSchema]
    handlers: HandlersDict[T_AtomicHandlerName | T_CompositeHandlerName, AtomicHandlerSchema[T_FilterName, T_FormatterName], CompositeHandlerSchema[T_AtomicHandlerName, T_FilterName]]
    loggers: dict[T_LoggerName, LoggerSchema[T_AtomicHandlerName | T_CompositeHandlerName]]

    def set_configuration(self) -> None:
        dict_config(self.to_configuration_dictionary())
    
    def to_configuration_dictionary(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True, by_alias=True)

    @classmethod
    def create(
        cls,
        *,
        filters: dict[T_FilterName, FilterSchema],
        formatters: dict[T_FormatterName, FormatterSchema],
        handlers: HandlersDict[T_AtomicHandlerName | T_CompositeHandlerName, AtomicHandlerSchema[T_FilterName, T_FormatterName], CompositeHandlerSchema[T_AtomicHandlerName, T_FilterName]],
        loggers: LoggersSchema[T_LoggerName, T_AtomicHandlerName | T_CompositeHandlerName] | dict[T_LoggerName, LoggerSchema[T_AtomicHandlerName | T_CompositeHandlerName]],
    ) -> Self:
        return cls(
            version=1,
            disable_existing_loggers=True,
            filters=filters,
            formatters=formatters,
            handlers=handlers,
            loggers=cast(dict[T_LoggerName, LoggerSchema[T_AtomicHandlerName | T_CompositeHandlerName]], loggers.to_loggers_dictionary()) if isinstance(loggers, LoggersSchema) else loggers,
        )
