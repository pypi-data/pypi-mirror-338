from typing import Callable, Any
from pickle import PickleError

from dill import loads, dumps  # type: ignore[attr-defined]
from pydantic_core import CoreSchema, core_schema
from pydantic import GetCoreSchemaHandler


class Factory[T]:
    def __init__(self, factory: Callable[[], T]) -> None:
        self.factory = factory

    def __call__(self) -> T:
        return self.factory()

    def __getstate__(self) -> bytes:
        return dumps(self.factory)  # type: ignore[no-any-return, no-untyped-call]
    
    def __setstate__(self, state: object) -> None:
        if not isinstance(state, bytes):
            raise PickleError(f"Cannot unpickle {self.__class__.__name__!r} object from non-bytes state.")
        self.factory = loads(state)  # type: ignore[no-untyped-call]

    @classmethod
    def __get_pydantic_core_schema__(cls, _: Any, handler: GetCoreSchemaHandler) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls, handler(Callable))
