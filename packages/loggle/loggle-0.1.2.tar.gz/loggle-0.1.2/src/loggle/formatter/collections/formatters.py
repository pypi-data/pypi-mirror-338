from typing import ClassVar

from ..lib.schemas import FormatterSchema
from ..json_formatter import JSONFormatter
from ..standard_formatter import StandardFormatter
from ...lib import Factory


class Formatters:
    STANDARD: ClassVar[FormatterSchema] = FormatterSchema(formatter_factory=Factory(lambda: StandardFormatter()))
    JSON: ClassVar[FormatterSchema] = FormatterSchema(formatter_factory=Factory(lambda: JSONFormatter()))
