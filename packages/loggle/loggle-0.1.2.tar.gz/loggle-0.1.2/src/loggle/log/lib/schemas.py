from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class JSONLogModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )


class JSONLogProcessSchema(JSONLogModel):
    name: str | None
    id: int | None


class JSONLogThreadSchema(JSONLogModel):
    name: str | None
    id: int | None
