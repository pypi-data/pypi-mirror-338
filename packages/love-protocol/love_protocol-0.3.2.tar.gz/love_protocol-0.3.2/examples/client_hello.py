"""
Beispiel-Client für HELLO-Message: decode + validate
"""

from love_protocol.core.decode import decode_message
from love_protocol.core.validate import validate_message
from pydantic import ValidationError

example_json = """
{
  "protocol": "LOVE/1.0",
  "type": "HELLO",
  "device_id": "dot-kitchen",
  "timestamp": 1711972643.42,
  "capabilities": {
    "mic": true,
    "speaker": true,
    "wakeword": true,
    "tts": false
  }
}
"""

if __name__ == "__main__":
    try:
        msg = decode_message(example_json)
        validate_message(msg)
        print("✅ Valid message decoded as:", type(msg).__name__)
        print(msg.dict())
    except ValidationError as e:
        print("❌ Validation failed:")
        print(e.json())
    except Exception as e:
        print("❌ Error during decoding:")
        print(e)