# examples/handler_echo.py

import asyncio
from love_protocol.constants import HELLO
from love_protocol.handler.handler import LoveHandler, LoveHandlerContext

# Create the handler
handler = LoveHandler()

# Optional: add a middleware for logging
@handler.use
async def logger(ctx: LoveHandlerContext):
    print(f"🛜 Received message of type: {ctx.message.type}")

# Register a handler using decorator syntax
@handler.on("HELLO")
async def handle_hello(ctx: LoveHandlerContext[HELLO]):
    print("👋 Echo handler triggered!")
    print("🔁 Full message object:", ctx.message)
    print("📦 Device ID:", ctx.message.device_id)
    print("📦 Capabilities:", ctx.message.capabilities)

# Simulate dispatching a HELLO message
async def main():
    msg = HELLO(
        protocol="LOVE/1.0",
        type="HELLO",
        device_id="dot-kitchen",
        timestamp=1234567890.0,
        capabilities={"mic": True, "speaker": True}
    )

    await handler.dispatch(msg)

if __name__ == "__main__":
    asyncio.run(main())
