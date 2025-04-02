<a id="readme-top"></a> 



<!-- PROJECT SUMMARY -->
<br />
<div align="center">
  <img src="https://i.imgur.com/LlNYjX4.gif/" alt="Logo">
  <p align="center">
    Type-safe, customizable logging configuration for Python
    <br />
    <a href="https://github.com/Kieran-Lock/loggle/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#about-the-project">About the Project</a>
    ·
    <a href="#getting-started">Getting Started</a>
    ·
    <a href="#basic-usage">Basic Usage</a>
    ·
    <a href="https://github.com/Kieran-Lock/loggle/">Documentation</a>
    ·
    <a href="#contributing">Contributing</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About the Project

Loggle is a Python logging library that provides a type-safe interface for logging configuration, allowing you to define and configure your logging setup for projects of any size. It provides schemas for logging configuration, pre-built filters and formatters you can use, and integrates with popular libraries including **Uvicorn** and **SQLALchemy**.

All of this makes it much easier to maintain complex logging configurations, and customize loggers in your application. No more poring over Python's outdated `logging` documentation!



<!-- GETTING STARTED -->
## Getting Started

Loggle is available on PyPI, so you can use `pip` (or another package manager) to install it:
```bash
pip install loggle
```



<!-- BASIC USAGE -->
## Basic Usage

#### Declarations

First, you must declare the names of the filters, formatters, handlers, and loggers your configuration contains:
```python
from loggle import FilterName, FormatterName, AtomicHandlerName, CompositeHandlerName, LoggerName
from loggle.collections import UvicornLoggerName, SQLAlchemyLoggerName


class AppFilterName(FilterName):
    ERROR = "error"


class AppFormatterName(FormatterName):
    STANDARD = "standard"
    JSON = "json"


class AppAtomicHandlerName(AtomicHandlerName):
    STANDARD = "standard"
    ERROR = "error"
    JSON_FILE = "json_file"


class AppCompositeHandlerName(CompositeHandlerName):
    QUEUE = "queue"


class AppLoggerName(LoggerName):
    APP = "app"
    UVICORN = UvicornLoggerName.ROOT
    UVICORN_ACCESS = UvicornLoggerName.ACCESS
    UVICORN_ERROR = UvicornLoggerName.ERROR
    UVICORN_ASGI = UvicornLoggerName.ASGI
    SQLALCHEMY_ENGINE = SQLAlchemyLoggerName.ENGINE
    SQLALCHEMY_POOL = SQLAlchemyLoggerName.POOL
    SQLALCHEMY_DIALECTS = SQLAlchemyLoggerName.DIALECTS
    SQLALCHEMY_ORM = SQLAlchemyLoggerName.ORM
```

#### Implementations

Now, you can define the actual implementations in your logging configuration:
```python
from pathlib import Path

from loggle import StreamHandlerSchema, LoggingLevel, LoggingStream, FileHandlerSchema, CompositeHandlerSchema, LoggersSchema
from loggle.collections import Filters, Formatters, HandlerClasses


FILTERS = {
    AppFilterName.ERROR: Filters.ERROR,
}

FORMATTERS = {
    AppFormatterName.STANDARD: Formatters.STANDARD,
    AppFormatterName.JSON: Formatters.JSON,
}

HANDLERS = {
    AppAtomicHandlerName.STANDARD: StreamHandlerSchema(
        handler_class=HandlerClasses.STREAM,
        filters=[AppFilterName.ERROR],
        formatter=AppFormatterName.STANDARD,
        level=LoggingLevel.DEBUG,
        stream=LoggingStream.STANDARD_OUT,
    ),
    AppAtomicHandlerName.ERROR: StreamHandlerSchema(
        handler_class=HandlerClasses.STREAM,
        formatter=AppFormatterName.STANDARD,
        level=LoggingLevel.ERROR,
        stream=LoggingStream.STANDARD_ERROR,
    ),
    AppAtomicHandlerName.JSON_FILE: FileHandlerSchema(
        handler_class=HandlerClasses.JSON_FILE,
        formatter=AppFormatterName.JSON,
        level=LoggingLevel.DEBUG,
    ),
    AppCompositeHandlerName.QUEUE: CompositeHandlerSchema(
        handler_class=HandlerClasses.QUEUE,
        handlers=list(AppAtomicHandlerName),
    ),
}

LOGGERS = (
    LoggersSchema[AppLoggerName, AppAtomicHandlerName | AppCompositeHandlerName]
    .from_json(Path(f"./path/to/loggers/configuration.json"))
)
```

#### Configuration

Now, define the actual configuration. This follows the same structure as Python's `logging.dictConfig` input:
```python
from loggle import LoggingConfiguration, Logger


LOGGING_CONFIGURATION = (
    LoggingConfiguration[AppFilterName, AppFormatterName, AppAtomicHandlerName, AppCompositeHandlerName, AppLoggerName].create(
        filters=FILTERS,
        formatters=FORMATTERS,
        handlers=HANDLERS,
        loggers=LOGGERS,
    )
)

APP_LOGGER = Logger(name=AppLoggerName.APP)
```

#### Usage

Finally, you can apply the configuration, and use loggers:
```python
LOGGING_CONFIGURATION.set_configuration()

APP_LOGGER.debug("This is a debug message.")
APP_LOGGER.info("This is an informational message.")
APP_LOGGER.error("This is an error message.")
```

You can also get the underlying configuration dictionary that is passed into `logging.dictConfig`, which can be useful in Uvicorn applications:
```python
LOGGING_CONFIGURATION.to_configuration_dictionary()
```



<!-- CONTRIBUTING -->
## Contributing

Distributed under the MIT License. Feel free to contribute to the project by opening issues or submitting pull requests. For any questions or suggestions, don't hesitate to reach out. Enjoy better, more type-safe logging with **Loggle**!
