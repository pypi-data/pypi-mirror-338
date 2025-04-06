# File: examples/tcp/client.py

import asyncio
import json
from love_protocol.core.decode import decode_message
from love_protocol.core.encode import encode_message

async def main():
    reader, writer = await asyncio.open_connection("127.0.0.1", 8765)

    # 📨 Plain dictionary
    message_dict = {
        "protocol": "LOVE/1.0",
        "type": "HELLO",
        "device_id": "test-tcp-client",
        "timestamp": 1234567890.0,
        "capabilities": {
            "mic": True,
            "speaker": True
        },
        "session": "abc123"
    }

    # 💡 Decode to Pydantic model (e.g., HELLO)
    message_model = decode_message(json.dumps(message_dict))

    # 🧾 Encode to JSON string
    data = encode_message(message_model)
    print(f"📤 Sending:\n{data}")
    writer.write(data.encode())
    await writer.drain()

    # 📬 Receive response
    response_bytes = await reader.read(4096)
    response_str = response_bytes.decode()
    response = decode_message(response_str)
    print(f"📥 Received:\n{response}")

    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
