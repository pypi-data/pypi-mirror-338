from ..lib.consts import LoggerName


class UvicornLoggerName(LoggerName):
    ROOT = "uvicorn"
    ACCESS = "uvicorn.access"
    ERROR = "uvicorn.error"
    ASGI = "uvicorn.asgi"


class SQLAlchemyLoggerName(LoggerName):
    ENGINE = "sqlalchemy.engine"
    POOL = "sqlalchemy.pool"
    DIALECTS = "sqlalchemy.dialects"
    ORM = "sqlalchemy.orm"
