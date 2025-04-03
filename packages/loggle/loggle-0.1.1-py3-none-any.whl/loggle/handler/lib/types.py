from typing import overload, Any, override

from pydantic_core import CoreSchema, core_schema
from pydantic import GetCoreSchemaHandler

from .consts import AtomicHandlerName, AtomicHandlerName, CompositeHandlerName, CompositeHandlerName
from .schemas import HandlerModel
from ...filter import FilterName


class HandlersDict[K: AtomicHandlerName | CompositeHandlerName, V_AtomicHandler: HandlerModel, V_CompositeHandler: HandlerModel](dict[K, V_AtomicHandler | V_CompositeHandler]):  # type: ignore[type-arg]
    @overload  # type: ignore[override]
    def __getitem__(self, key: AtomicHandlerName, /) -> V_AtomicHandler:
        ...
    
    @overload
    def __getitem__(self, key: CompositeHandlerName, /) -> V_CompositeHandler:
        ...

    @override  # type: ignore[misc]
    def __getitem__(self, key: K, /) -> V_AtomicHandler | V_CompositeHandler:
        return super(HandlersDict, self).__getitem__(key)
    
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler: GetCoreSchemaHandler) -> CoreSchema:
        return core_schema.no_info_after_validator_function(cls, handler(dict))
