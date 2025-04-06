# File: tests/test_session_middleware.py

import pytest
import time
from love_protocol.handler.handler import LoveHandler, LoveHandlerContext
from love_protocol.session.middleware import create_session_middleware
from love_protocol.session.store import SessionStore
from love_protocol.types.wakeword_detected import WAKEWORDDETECTED


@pytest.mark.asyncio
async def test_session_middleware_creates_session():
    store = SessionStore()
    handler = LoveHandler()
    handler.use(create_session_middleware(store))

    captured = {}

    @handler.on("WAKEWORD_DETECTED")
    async def handle(ctx: LoveHandlerContext):
        captured["session_id"] = ctx.session_id
        captured["session_data"] = ctx.session_data

    msg = WAKEWORDDETECTED.parse_obj({
        "protocol": "LOVE/1.0",
        "type": "WAKEWORD_DETECTED",
        "device_id": "dot-kitchen",
        "timestamp": 1234.56,
        "session": "custom-session-123",
        "wakeword": "lucy"
    })

    await handler.dispatch(msg)

    assert captured["session_id"] == "custom-session-123"
    assert captured["session_data"].device_id == "dot-kitchen"
    assert captured["session_data"].buffer.audio_chunks == []
    assert captured["session_data"].buffer.transcripts == []


@pytest.mark.asyncio
async def test_session_middleware_updates_existing():
    store = SessionStore()
    session_id = store.create("test-device", session_id="test-session-456")
    session = store.get(session_id)
    handler = LoveHandler()
    handler.use(create_session_middleware(store))

    result = {}

    @handler.on("WAKEWORD_DETECTED")
    async def handle(ctx: LoveHandlerContext):
        result["session_data"] = ctx.session_data
        result["session_id"] = ctx.session_id

    msg = WAKEWORDDETECTED.parse_obj({
        "protocol": "LOVE/1.0",
        "type": "WAKEWORD_DETECTED",
        "device_id": "test-device",
        "timestamp": 1234.56,
        "session": "test-session-456", 
        "wakeword": "lucy"
    })


    await handler.dispatch(msg)

    assert result["session_id"] == "test-session-456"
    assert result["session_data"].device_id == "test-device"
    assert result["session_data"].last_seen >= session.last_seen
