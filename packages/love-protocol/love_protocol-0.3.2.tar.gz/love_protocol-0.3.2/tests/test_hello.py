# File: tests/test_decode_hello.py

import json
import pytest
from love_protocol.core.decode import decode_message
from love_protocol.core.validate import validate_message_dict
from love_protocol.types.hello import HELLO


def test_decode_valid_hello():
    raw = {
        "protocol": "LOVE/1.0",
        "type": "HELLO",
        "device_id": "test-device",
        "timestamp": 1234567890.0,
        "capabilities": {
            "mic": True,
            "speaker": True
        }
    }

    # Validate dict before decoding
    result = validate_message_dict(raw)
    assert result["valid"], f"Validation failed: {result.get('errors')}"

    msg = decode_message(json.dumps(raw))
    assert isinstance(msg, HELLO)
    assert msg.device_id == "test-device"
    assert msg.capabilities.mic is True
    assert msg.capabilities.speaker is True


def test_decode_invalid_hello_missing_device_id():
    raw = {
        "protocol": "LOVE/1.0",
        "type": "HELLO",
        "timestamp": 1234567890.0
    }

    result = validate_message_dict(raw)
    assert not result["valid"]
    assert any("device_id" in err for err in result["errors"])
