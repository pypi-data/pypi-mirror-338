# ❤️ LOVE Protocol for Python

**LOVE (Lucy Open Voice Exchange)** is a universal messaging protocol for multimodal voice interaction.  
This library is the official Python implementation based on JSON schemas.

---

## 📦 Installation

```bash
pip install love-protocol
```

Requires: Python ≥ 3.10

---

## 🚀 Quick Start

### WebSocket Demo

```bash
python examples/websocket/server.py
# In a second terminal:
python examples/websocket/client.py
```

---

## 🔧 Features

- ✅ Full validation using Pydantic (generated models)
- ✅ Message encoding / decoding (JSON ⇄ Python)
- ✅ Async handler system with middleware support
- ✅ In-memory SessionStore
- ✅ Command-line tool `love-validate`

---

## 💬 LOVE Message Format

All messages follow the same base structure with a `type` field:

```json
{
  "protocol": "LOVE/1.0",
  "type": "HELLO",
  "device_id": "test-device",
  "timestamp": 1234567890.0
}
```

Supported message types include:

- `HELLO`, `HELLO_ACK`
- `AUDIO_START`, `AUDIO_CHUNK`, `AUDIO_STOP`
- `TRANSCRIPTION`, `INTENT_DETECTED`, `TTS_OUTPUT`
- `WAKEWORD_DETECTED`, `COMMAND`
- `MEDIA_CONTROL`, `MEDIA_PLAY`
- `SENSOR_EVENT`
- `ERROR`

All types are defined in `love_protocol.types`.

---

## 🧪 Run Tests

```bash
PYTHONPATH=. pytest tests
```

Tests use `pytest` and `pytest-asyncio`.

---

## 🧰 CLI: love-validate

Validate a raw message from file:

```bash
love-validate examples/data/hello.json
```

Output:

```
✅ Valid message of type HELLO
```

If invalid:

```
❌ Invalid message:
- protocol: expected format LOVE/X.Y
- type: unknown message type 'FOO'
```

---

## 🧠 Handler Example

```python
from love_protocol.handler.handler import LoveHandler

handler = LoveHandler()

@handler.on("HELLO")
async def handle_hello(ctx):
    print("📥 Message:", ctx.message)
    ctx.response = HELLOACK(
        protocol="LOVE/1.0",
        type="HELLO_ACK",
        device_id=ctx.message.device_id,
        timestamp=ctx.message.timestamp,
        session=ctx.message.session
    )
```

With middleware:

```python
from love_protocol.session.middleware import create_session_middleware

handler.use(create_session_middleware(session_store))
```

---

## 📁 Project Structure (Excerpt)

```
love_protocol/
├── core/         # encode / decode / validate
├── handler/      # dispatch + middleware
├── types/        # generated message types
├── session/      # SessionStore + lifecycle middleware
├── cli/          # love-validate CLI
├── examples/     # WebSocket demos
└── tests/        # pytest coverage
```

---

## 🧠 SessionStore Example

```python
from love_protocol.session.store import SessionStore

store = SessionStore()
session_id = store.create("kitchen-dot")
session = store.get(session_id)

store.update(session_id, { "state": "active" })
```

Sessions can be managed automatically via middleware.

---

## 📄 License

This project is licensed under the Apache 2.0 License.  
You may freely use, modify, and integrate it.
