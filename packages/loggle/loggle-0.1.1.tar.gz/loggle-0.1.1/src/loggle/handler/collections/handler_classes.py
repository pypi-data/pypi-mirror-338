from logging import StreamHandler

from ..json_file_handler import JSONFileHandler
from ..queue_handler import QueueHandler


class HandlerClasses:
    STREAM = StreamHandler
    JSON_FILE = JSONFileHandler
    QUEUE = QueueHandler
