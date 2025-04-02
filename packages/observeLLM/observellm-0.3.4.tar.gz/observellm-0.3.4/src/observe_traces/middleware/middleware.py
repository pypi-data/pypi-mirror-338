import uuid
from typing import Optional, Dict, Any

from fastapi import Request

from observe_traces.config.context_util import (
    request_context,
    tracer_context,
    request_metadata_context,
)
from observe_traces.config.langfuse_init import LangfuseInitializer


async def unified_middleware(
    request: Request, call_next, metadata: Optional[Dict[str, Any]] = None
):
    # Set request context
    session_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    request_token = None
    metadata_token = None

    # Create unified trace
    trace_id = str(uuid.uuid4())
    langfuse_client = LangfuseInitializer.get_instance().langfuse_client

    if request_context.get() is None:
        request_token = request_context.set(trace_id)

    # Set metadata if provided
    if metadata is not None:
        metadata_token = request_metadata_context.set(metadata)

    if not trace_id:
        trace = langfuse_client.trace(
            id=trace_id,
            name=metadata.get("apiEndpoint", trace_id),
            session_id=session_id,
            metadata=metadata,
            user_id=metadata.get("user"),
        )
        trace_id = trace.id
    else:
        trace = langfuse_client.trace(
            id=trace_id,
            session_id=session_id,
            name=metadata.get("apiEndpoint", trace_id),
            metadata=metadata or {},
            user_id=metadata.get("user"),
        )

    trace_token = tracer_context.set(trace)

    try:
        # Process the request
        response = await call_next(request)

        # Set response headers
        response.headers["X-Request-ID"] = session_id
        response.headers["X-Trace-ID"] = trace_id

        return response
    finally:
        # Clean up context tokens
        if request_token is not None:
            request_context.reset(request_token)
        if metadata_token is not None:
            request_metadata_context.reset(metadata_token)
        if trace_token is not None:
            tracer_context.reset(trace_token)
