# File: examples/websocket/client.py

import asyncio
import websockets
from love_protocol.core.decode import decode_message
from love_protocol.core.encode import encode_message
from love_protocol.types.hello import HELLO, Capabilities

async def main():
    uri = "ws://localhost:8766"
    async with websockets.connect(uri) as websocket:
        message = HELLO(
            protocol="LOVE/1.0",
            type="HELLO",
            device_id="test-ws-client",
            timestamp=1234567890.0,
            session="abc123",
            capabilities=Capabilities(  # <-- FIX
                mic=True,
                speaker=True
            )
        )

        payload = encode_message(message)
        print(f"📤 Sending:\n{payload}")
        await websocket.send(payload)

        response = await websocket.recv()
        msg = decode_message(response)
        print(f"📥 Received:\n{msg}")

if __name__ == "__main__":
    asyncio.run(main())
