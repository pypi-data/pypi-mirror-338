# File: tests/test_handler.py

import pytest
from love_protocol.handler.handler import LoveHandler, LoveHandlerContext
from love_protocol.types.hello import HELLO


@pytest.mark.asyncio
async def test_dispatch_hello_handler():
    handler = LoveHandler()
    called = {}

    @handler.on("HELLO")
    async def handle_hello(ctx: LoveHandlerContext):
        called["hello"] = True
        assert isinstance(ctx.message, HELLO)

    msg = HELLO(
        protocol="LOVE/1.0",
        type="HELLO",
        device_id="dot-test",
        timestamp=1234567890.0,
        capabilities={"mic": True, "speaker": True}
    )

    ctx = await handler.dispatch(msg)
    assert called.get("hello") is True
    assert ctx.response is None


@pytest.mark.asyncio
async def test_global_middleware_called_in_order():
    handler = LoveHandler()
    steps = []

    async def mw1(ctx: LoveHandlerContext, next_fn):
        steps.append("mw1")
        await next_fn()

    async def mw2(ctx: LoveHandlerContext, next_fn):
        steps.append("mw2")
        await next_fn()

    handler.use(mw1)
    handler.use(mw2)

    @handler.on("HELLO")
    async def handle_hello(ctx: LoveHandlerContext):
        steps.append("handler")

    msg = HELLO(
        protocol="LOVE/1.0",
        type="HELLO",
        device_id="dot-test",
        timestamp=1234567890.0,
        capabilities={"mic": True, "speaker": True}
    )

    ctx = await handler.dispatch(msg)

    assert steps == ["mw1", "mw2", "handler"]
    assert ctx.message.device_id == "dot-test"
