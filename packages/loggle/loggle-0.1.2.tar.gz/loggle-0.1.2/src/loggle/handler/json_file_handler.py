from logging.handlers import RotatingFileHandler
from typing import ClassVar


class JSONFileHandler(RotatingFileHandler):
    FILE_EXTENSION: ClassVar[str] = "jsonl"
    
    def namer(self, default: str) -> str:
        parts = default.rsplit(".", maxsplit=1)
        base_name = parts[0]
        index = parts[-1]
        if not index.isnumeric():
            return default
        return f"{base_name.removesuffix(f".{self.FILE_EXTENSION}")}-backup-{index:>03}.{self.FILE_EXTENSION}"
