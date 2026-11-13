"""
Structured Logging
==================
Configure the application's logging so that every log line is structured
(JSON, or at least a consistent key=value format).

You should implement here:
- setup_logging(): configures the root logger with the level from
  settings.LOG_LEVEL and a structured formatter
- Call setup_logging() once at application startup (app/main.py)

Then, in your modules, use the standard library logger:

    import logging
    logger = logging.getLogger(__name__)
    logger.info("task_created", extra={"task_id": str(task.id)})

Example of an expected log line:
    {"timestamp": "2026-01-01T12:00:00Z", "level": "INFO",
     "logger": "app.services.task_service", "message": "task_created",
     "task_id": "..."}

Tip: you can write a small `logging.Formatter` subclass that returns
`json.dumps(...)`, or use a library such as `python-json-logger` or `structlog`.
"""
