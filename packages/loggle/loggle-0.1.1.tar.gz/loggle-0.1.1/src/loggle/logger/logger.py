from __future__ import annotations

from logging import Logger as DefaultLogger, getLogger as get_logger, _levelToName as level_to_name
from dataclasses import dataclass, field
from typing import Self

from ..log.lib.consts import LoggingLevel


@dataclass(slots=True, init=False)
class Logger:
    name: str | None
    _logger: DefaultLogger = field(repr=False, compare=False)

    def __init__(self, *, name: str | None, level: LoggingLevel = LoggingLevel.INFO) -> None:
        self.name = name
        self._logger = get_logger(name)
        self.set_level(level)
    
    @classmethod
    def root(cls) -> Self:
        return cls(name=None)
    
    @property
    def level(self) -> LoggingLevel:
        return LoggingLevel(level_to_name[self._logger.level])

    def set_level(self, level: LoggingLevel) -> Self:
        self._logger.setLevel(level)
        return self

    def debug(self, message: object, **extra: object) -> Self:
        self._logger.debug(message, extra=extra)
        return self

    def info(self, message: object, **extra: object) -> Self:
        self._logger.info(message, extra=extra)
        return self

    def warning(self, message: object, **extra: object) -> Self:
        self._logger.warning(message, extra=extra)
        return self

    def error(self, message: object, **extra: object) -> Self:
        self._logger.error(message, extra=extra)
        return self

    def exception(self, message: object, **extra: object) -> Self:
        self._logger.exception(message, extra=extra)
        return self
    
    def critical(self, message: object, **extra: object) -> Self:
        self._logger.critical(message, extra=extra)
        return self
