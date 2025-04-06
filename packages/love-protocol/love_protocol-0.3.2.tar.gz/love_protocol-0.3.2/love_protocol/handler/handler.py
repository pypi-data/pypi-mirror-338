# File: love_protocol/handler/handler.py

"""
Handler system for LOVE protocol messages.

This module provides the `LoveHandler` class, which allows you to register
message-specific handlers, apply global middleware, and process both structured
and raw LOVE messages. It supports validation, error handling, and response emission.
"""

import json
from typing import Awaitable, Callable, Dict, Generic, List, Optional, TypeVar
from love_protocol.constants import LoveMessage
from love_protocol.core.validate import validate_message_dict
from love_protocol.core.error import encode_error

__all__ = ["LoveHandler", "LoveHandlerContext", "LoveMiddleware", "LoveMessageHandler"]

T = TypeVar("T", bound=LoveMessage)

LoveMiddleware = Callable[[ "LoveHandlerContext", Callable[[], Awaitable[None]]], Awaitable[None]]
LoveMessageHandler = Callable[[ "LoveHandlerContext[T]"], Awaitable[None]]


class LoveHandlerContext(Generic[T]):
    """
    Context object passed to all middleware and handlers during message processing.

    Attributes:
        message (LoveMessage): The original decoded message object.
        session_data (Optional[dict]): Optional session data injected by middleware.
        session_id (Optional[str]): Optional session ID, typically set by middleware.
        response (Optional[LoveMessage]): Optional message to be sent back as a response.
        error (Optional[str]): Optional error string set by middleware or handlers.
    """

    def __init__(self, message: T):
        self.message = message
        self.session_data: Optional[dict] = None
        self.session_id: Optional[str] = None
        self.response: Optional[LoveMessage] = None
        self.error: Optional[str] = None


class LoveHandler:
    """
    Central dispatcher and middleware engine for processing LOVE protocol messages.

    Use `.on(type_name)` to register handlers for specific message types.
    Use `.use(middleware)` to attach global middleware functions.
    Use `.dispatch(message)` for structured processing.
    Use `.handle_raw(raw)` for processing raw JSON input (e.g., over WebSocket).
    """

    def __init__(self):
        self.global_middleware: List[LoveMiddleware] = []
        self.handlers: Dict[str, LoveMessageHandler] = {}

    def use(self, middleware: LoveMiddleware) -> None:
        """
        Register a global middleware function.

        Middleware will run in the order registered before the handler is invoked.

        Args:
            middleware: A coroutine function with signature (ctx, next) -> awaitable
        """
        self.global_middleware.append(middleware)

    def on(self, type_name: str, handler: Optional[LoveMessageHandler] = None):
        """
        Register a handler for a specific message type.

        This can be used as either a decorator or a direct method call.

        Args:
            type_name: The string name of the LOVE message type (e.g., "HELLO").
            handler: The async function to be called when this type is received.

        Returns:
            The decorator if used as such, or None.
        """
        if handler is not None:
            self.handlers[type_name] = handler
            return

        def decorator(func: LoveMessageHandler):
            self.handlers[type_name] = func
            return func

        return decorator

    async def dispatch(self, message: LoveMessage) -> LoveHandlerContext:
        """
        Processes a structured LOVE message through middleware and type handlers.

        Args:
            message: A pre-decoded LOVE message object.

        Returns:
            LoveHandlerContext: The context after processing, including response if any.
        """
        ctx = LoveHandlerContext(message)

        async def run_middleware(index: int):
            if index < len(self.global_middleware):
                middleware = self.global_middleware[index]
                await middleware(ctx, lambda: run_middleware(index + 1))
            else:
                handler = self.handlers.get(message.type)
                if handler:
                    await handler(ctx)

        await run_middleware(0)
        return ctx

    async def handle_raw(self, raw: str) -> Optional[str]:
        """
        Handles raw JSON input from e.g. a WebSocket or TCP stream.

        This method:
        - Parses JSON
        - Validates the message against schemas
        - Dispatches to the appropriate handler
        - Returns the encoded response or error JSON

        Args:
            raw: The raw JSON string to handle.

        Returns:
            The JSON-encoded response (if any), or an error message.
        """
        try:
            data = json.loads(raw)

            result = validate_message_dict(data, strict=False)
            if not result["valid"]:
                return encode_error(result["errors"])

            # Safe to decode to message class
            from love_protocol.core.decode import decode_message
            message = decode_message(raw)

            ctx = await self.dispatch(message)
            if ctx.response:
                from love_protocol.core.encode import encode_message
                return encode_message(ctx.response)

        except Exception as e:
            return encode_error(str(e))

        return None
