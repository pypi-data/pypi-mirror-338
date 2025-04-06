# File: examples/handler_echo_with_session.py

import asyncio
import json
from love_protocol.core.decode import decode_message
from love_protocol.handler.handler import LoveHandler, LoveHandlerContext
from love_protocol.session.store import SessionStore
from love_protocol.session.middleware import create_session_middleware

# Init session store and handler
store = SessionStore()
store.create("kitchen-dot", session_id="abc123")

handler = LoveHandler()
handler.use(create_session_middleware(store))

# Register echo handler
@handler.on("HELLO")
async def handle_hello(ctx: LoveHandlerContext):
    print("📥 Received HELLO:", ctx.message)
    print("🧠 Session data:", ctx.session_data)


async def main():
    raw = json.dumps({
        "protocol": "LOVE/1.0",
        "type": "HELLO",
        "device_id": "kitchen-dot",
        "timestamp": 1234567.89,
        "capabilities": {
            "mic": True,
            "speaker": True
        },
        "session": "abc123"
    })

    msg = decode_message(raw)
    await handler.dispatch(msg)

if __name__ == "__main__":
    asyncio.run(main())
