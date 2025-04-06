# File: examples/tcp/server.py

import asyncio
from love_protocol.core.decode import decode_message
from love_protocol.core.encode import encode_message
from love_protocol.handler.handler import LoveHandler, LoveHandlerContext
from love_protocol.types.hello_ack import HELLOACK

handler = LoveHandler()


@handler.on("HELLO")
async def handle_hello(ctx: LoveHandlerContext):
    print("📥 Received HELLO:", ctx.message)

    # Beispielhafte Antwort generieren
    ctx.response = HELLOACK(
        protocol="LOVE/1.0",
        type="HELLO_ACK",
        device_id=ctx.message.device_id,
        timestamp=ctx.message.timestamp,
        session=ctx.message.session
    )


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    data = await reader.read(4096)
    message = decode_message(data.decode())

    # ✨ ctx kommt jetzt aus dispatch zurück
    ctx = await handler.dispatch(message)

    if ctx.response:
        response_json = encode_message(ctx.response)
        writer.write(response_json.encode())
        await writer.drain()

    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 8765)
    print("🚀 TCP Server running on 127.0.0.1:8765")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
