# File: examples/websocket/server.py

import asyncio
import websockets
from love_protocol.core.decode import decode_message
from love_protocol.core.encode import encode_message
from love_protocol.handler.handler import LoveHandler, LoveHandlerContext
from love_protocol.types.hello_ack import HELLOACK

handler = LoveHandler()

@handler.on("HELLO")
async def handle_hello(ctx: LoveHandlerContext):
    print("📥 Received HELLO:", ctx.message)
    ctx.response = HELLOACK(
        protocol="LOVE/1.0",
        type="HELLO_ACK",
        device_id=ctx.message.device_id,
        timestamp=ctx.message.timestamp,
        session=ctx.message.session
    )

async def handle_ws(websocket):
    async for raw in websocket:
        try:
            message = decode_message(raw)
            ctx = await handler.dispatch(message)

            if ctx.response:
                response = encode_message(ctx.response)
                await websocket.send(response)
        except Exception as e:
            print("❌ Error:", e)

async def main():
    print("🚀 WebSocket Server running on ws://localhost:8766")
    async with websockets.serve(handle_ws, "localhost", 8766):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
