from ..lib.schemas import FilterSchema
from ..error_filter import ErrorFilter
from ...lib import Factory


class Filters:
    ERROR = FilterSchema(filter_factory=Factory(lambda: ErrorFilter()))
