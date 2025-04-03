import json
import logging
import platform
from contextlib import contextmanager
from datetime import datetime
from typing import Any, Dict, Optional

from opentelemetry import trace


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_data = {}

        if hasattr(record, 'structured') and record.structured:
            for key, value in record.__dict__.items():
                if key not in (
                        'args', 'exc_info', 'exc_text', 'msg', 'message', 'levelname', 'levelno', 'pathname',
                        'filename',
                        'module', 'stack_info', 'lineno', 'funcName', 'created', 'msecs', 'relativeCreated', 'name',
                        'thread',
                        'threadName', 'processName', 'process'):
                    log_data[key] = value

            if 'attributes' in log_data:
                for key, value in log_data['attributes'].items():
                    log_data[key] = value
                del log_data['attributes']

        log_data['message'] = record.getMessage()

        return json.dumps(log_data)


class StructuredLogger:
    """
    Logger that produces structured logs with tracing context.
    """

    def __init__(
            self,
            service_name: str,
            default_attributes: Optional[Dict[str, Any]] = None
    ):
        self.logger = logging.getLogger(service_name)
        self.default_attributes = {
            "service.name": service_name,
            "host.name": platform.node(),
            **(default_attributes or {})
        }

        if not self.logger.handlers or not any(isinstance(h.formatter, JsonFormatter) for h in self.logger.handlers):
            handler = logging.StreamHandler()
            handler.setFormatter(JsonFormatter())
            self.logger.addHandler(handler)

    def _get_trace_context(self) -> Dict[str, str]:
        """
        Gets the current tracing context if it exists.
        """
        span = trace.get_current_span()
        if span.is_recording():
            ctx = span.get_span_context()
            return {
                "trace_id": format(ctx.trace_id, "032x"),
                "span_id": format(ctx.span_id, "016x")
            }
        return {}

    def _log(
            self,
            level: int,
            message: str,
            *args,
            **kwargs
    ):
        trace_context = self._get_trace_context()

        log_attributes = {
            **self.default_attributes,
            **trace_context,
            "timestamp": datetime.utcnow().isoformat(),
            "severity": logging.getLevelName(level),
            "logger.name": self.logger.name
        }

        for key, value in kwargs.items():
            log_attributes[key] = value

        self.logger.log(
            level,
            message,
            extra={
                "structured": True,
                "otel.name": "log",
                "otel.kind": "event",
                **log_attributes
            }
        )

    def debug(self, message: str, *args, **kwargs):
        self._log(logging.DEBUG, message, *args, **kwargs)

    def info(self, message: str, *args, **kwargs):
        self._log(logging.INFO, message, *args, **kwargs)

    def error(self, message: str, *args, **kwargs):
        self._log(logging.ERROR, message, *args, **kwargs)

    @contextmanager
    def operation_context(
            self,
            operation_name: str,
            **context
    ):
        """
        Provides context for an operation, recording its beginning and end.
        """
        try:
            self.info(
                f"Iniciando {operation_name}",
                operation=operation_name,
                status="started",
                **context
            )
            yield
            self.info(
                f"Completado {operation_name}",
                operation=operation_name,
                status="completed",
                **context
            )
        except Exception as e:
            self.error(
                f"Error en {operation_name}: {str(e)}",
                operation=operation_name,
                status="failed",
                error=str(e),
                **context
            )
            raise
