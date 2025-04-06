# File: love_protocol/session/middleware.py

"""
Session middleware for LOVE protocol handlers.

This module provides middleware that automatically manages the lifecycle of
a session within a LOVE protocol interaction. It creates, retrieves, and updates
sessions based on incoming messages.

The middleware is intended to be used with `LoveHandler.use()` and supports
injection of session data into the handler context.
"""

from love_protocol.session.store import SessionStore
from love_protocol.handler.handler import LoveHandlerContext, LoveMiddleware
from love_protocol.session.model import LoveSession


def create_session_middleware(store: SessionStore) -> LoveMiddleware:
    """
    Creates middleware to manage LOVE protocol session state.

    This middleware performs the following:
    - Creates a new session when a `WAKEWORD_DETECTED` message arrives with a new session ID.
    - Updates the `last_seen` timestamp of an existing session on each message.
    - Injects the current session into the context (`ctx.session_data` and `ctx.session_id`).

    Args:
        store (SessionStore): The session store instance to use.

    Returns:
        LoveMiddleware: A middleware function compatible with `LoveHandler.use()`.
    """

    async def middleware(ctx: LoveHandlerContext, next_middleware):
        msg = ctx.message

        session_id = getattr(msg, "session", None)
        device_id = getattr(msg, "device_id", None)

        # No session ID provided – skip session logic
        if not session_id or not isinstance(session_id, str):
            return await next_middleware()

        # New session only on WAKEWORD_DETECTED
        if msg.type == "WAKEWORD_DETECTED":
            if not store.exists(session_id):
                session = store.create(device_id=device_id, session_id=session_id)
                ctx.session_data = session
                ctx.session_id = session_id

        # Always attempt to update session timestamp
        session = store.get(session_id)
        if session:
            store.update(session_id, {"last_seen": msg.timestamp})
            ctx.session_data = session
            ctx.session_id = session_id

        await next_middleware()

    return middleware
