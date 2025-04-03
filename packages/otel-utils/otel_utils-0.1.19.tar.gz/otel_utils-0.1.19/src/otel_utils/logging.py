import json
import logging
from contextlib import contextmanager
from datetime import datetime
from typing import Any, Dict, Optional

from opentelemetry import trace


class JsonFormatter(logging.Formatter):

    def format(self, record):
        log_record = {"timestamp": datetime.utcnow().isoformat(), "level": record.levelname, "logger": record.name,
                      "message": record.getMessage()}

        if hasattr(record, "otelTraceID"):
            log_record["trace_id"] = getattr(record, "otelTraceID")
        if hasattr(record, "otelSpanID"):
            log_record["span_id"] = getattr(record, "otelSpanID")

        if hasattr(record, "context") and record.context:
            log_record["context"] = record.context

        if hasattr(record, "operation"):
            log_record["operation"] = record.operation

        for attr in ["service_name", "status", "error_type", "error_message"]:
            if hasattr(record, attr):
                log_record[attr] = getattr(record, attr)

        return json.dumps(log_record)


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
        self.service_name = service_name
        self.default_attributes = default_attributes or {}

        if not self.logger.handlers:
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
        operation = kwargs.pop("operation", None)
        status = kwargs.pop("status", None)

        context = kwargs.copy() if kwargs else None

        extra_data = {
            "service_name": self.service_name
        }

        if operation:
            extra_data["operation"] = operation

        if status:
            extra_data["status"] = status

        if context:
            extra_data["context"] = context

        trace_ctx = self._get_trace_context()
        if trace_ctx:
            extra_data["otelTraceID"] = trace_ctx.get("trace_id")
            extra_data["otelSpanID"] = trace_ctx.get("span_id")

        self.logger.log(level, message, extra=extra_data)

    def debug(self, message: str, *args, **kwargs):
        self._log(logging.DEBUG, message, *args, **kwargs)

    def info(self, message: str, *args, **kwargs):
        self._log(logging.INFO, message, *args, **kwargs)

    def warning(self, message: str, *args, **kwargs):
        self._log(logging.WARN, message, *args, **kwargs)

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
