from logging.handlers import QueueHandler as DefaultQueueHandler, QueueListener
from logging import LogRecord
from atexit import register as at_exit_register
from typing import ClassVar
from multiprocessing.queues import Queue as TQueue
from dataclasses import dataclass


@dataclass(slots=True, init=False)
class QueueHandler(DefaultQueueHandler):
    AUTOMATICALLY_SET_LISTENER: ClassVar[bool] = True

    queue: TQueue[LogRecord | None]
    _listener: QueueListener | None

    def __init__(self, queue: TQueue[LogRecord | None]) -> None:
        self.queue = queue
        self._listener = None
        super(QueueHandler, self).__init__(queue)
    
    @property
    def listener(self) -> QueueListener | None:
        return self._listener
    
    @listener.setter
    def listener(self, value: QueueListener | None) -> None:
        self._listener = value
        if isinstance(value, QueueListener):
            self.start_listener()
    
    def start_listener(self) -> None:
        if self.listener:
            self.listener.start()
            at_exit_register(self.listener.stop)
    
    def __hash__(self) -> int:
        return super(QueueHandler, self).__hash__()
