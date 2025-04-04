import importlib.metadata

from .models import ResponseError

from aio_pika import IncomingMessage
from prometheus_client import Counter, Gauge, Histogram, Info, Summary
from typing import Optional


application_info = Info("application", "Application info")


def set_application_info(**kwargs: str) -> None:
    mertics_package = __package__.split(".")[0]
    application_info.info(
        {
            "mertics_package": mertics_package,
            "mertics_package_version": importlib.metadata.version(mertics_package),
            **kwargs,
        }
    )


set_application_info()


messages_published_count = Counter(
    name="queue_rpc_messages_published_total",
    documentation="Total number of published messages",
    labelnames=["exchange", "routing_key", "type", "priority"],
)

messages_published_payload_size = Summary(
    name="queue_rpc_messages_published_payload_size_bytes",
    documentation="Payload size of published messages",
    labelnames=["exchange", "routing_key", "type"],
)


def message_published(
    *, exchange: str, routing_key: str, type: str, priority: int, payload_size: int
) -> None:
    labels = dict(
        exchange=exchange,
        routing_key=routing_key,
        type=type,
    )
    messages_published_count.labels(priority=priority, **labels).inc()
    messages_published_payload_size.labels(**labels).observe(payload_size)


messages_consumed_count = Counter(
    name="queue_rpc_messages_consumed_total",
    documentation="Total number of consumed messages",
    labelnames=["exchange", "routing_key", "redelivered", "type", "priority", "error"],
)

messages_consumed_payload_size = Summary(
    name="queue_rpc_messages_consumed_payload_size_bytes",
    documentation="Payload size of consumed messages",
    labelnames=["exchange", "routing_key", "redelivered", "type"],
)


def message_consumed(
    message: IncomingMessage,
    *,
    routing_key: Optional[str] = None,
    error: Optional[str] = None,
) -> None:
    labels = dict(
        exchange=message.exchange,
        routing_key=routing_key or "",
        redelivered=message.redelivered,
        type=message.type,
    )
    messages_consumed_count.labels(
        priority=message.priority, error=error or "", **labels
    ).inc()
    messages_consumed_payload_size.labels(**labels).observe(message.body_size)


server_requests_count = Counter(
    name="queue_rpc_server_requests_total",
    documentation="Total number of requests",
    labelnames=["priority", "method", "error"],
)

server_requests_in_progress = Gauge(
    name="queue_rpc_server_requests_in_progress",
    documentation="Number of requests in progress",
    labelnames=["method"],
)

server_request_waiting_time = Histogram(
    name="queue_rpc_server_request_waiting_seconds",
    documentation="Time request spent in queue",
    labelnames=["priority", "method"],
    buckets=(
        0.1,
        0.3,
        0.5,
        1,
        3,
        5,
        10,
        30,
        1 * 60,
        3 * 60,
        5 * 60,
        10 * 60,
        30 * 60,
        1 * 3600,
        3 * 3600,
        5 * 3600,
        10 * 3600,
        30 * 3600,
    ),
)

server_request_processing_time = Histogram(
    name="queue_rpc_server_request_processing_seconds",
    documentation="Time spent processing request",
    labelnames=["method"],
    buckets=(
        0.1,
        0.25,
        0.5,
        0.75,
        1.0,
        2.5,
        5.0,
        7.5,
        10,
        25,
        50,
        75,
        100,
        250,
        500,
        750,
        1000,
        2500,
    ),
)


def server_request_processed(
    priority: int,
    method: str,
    error: Optional[ResponseError],
    queued_for: float,
    elapsed: float,
) -> None:
    server_requests_count.labels(
        priority=priority,
        method=method,
        error=error and error.type or "",
    ).inc()

    if queued_for is not None:
        server_request_waiting_time.labels(
            priority=priority,
            method=method,
        ).observe(queued_for)

    server_request_processing_time.labels(
        method=method,
    ).observe(elapsed)


client_requests_count = Counter(
    name="queue_rpc_client_requests_total",
    documentation="Total number of requests",
    labelnames=["priority", "service", "method"],
)

client_requests_in_progress = Gauge(
    name="queue_rpc_client_requests_in_progress",
    documentation="Number of requests in progress",
    labelnames=["service", "method"],
)

client_request_time = Histogram(
    name="queue_rpc_client_request_seconds",
    documentation="Time request took",
    labelnames=["priority", "service", "method"],
    buckets=(
        0.1,
        0.3,
        0.5,
        1,
        3,
        5,
        10,
        30,
        1 * 60,
        3 * 60,
        5 * 60,
        10 * 60,
        30 * 60,
        1 * 3600,
        3 * 3600,
        5 * 3600,
        10 * 3600,
        30 * 3600,
    ),
)


def client_request_processed(
    priority: int, service: str, method: str, elapsed: float
) -> None:
    labels = dict(
        priority=int(priority or 0),
        service=service,
        method=method,
    )

    client_requests_count.labels(**labels).inc()

    client_request_time.labels(**labels).observe(elapsed)
