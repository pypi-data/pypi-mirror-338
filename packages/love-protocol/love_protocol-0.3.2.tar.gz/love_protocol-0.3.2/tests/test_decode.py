# File: tests/test_decode.py

import json
import pytest

from love_protocol.core.decode import decode_message
from love_protocol.core.validate import validate_message_dict
from love_protocol.types.transcription import TRANSCRIPTION


def test_decode_valid_transcription():
    raw_dict = {
        "protocol": "LOVE/1.0",
        "type": "TRANSCRIPTION",
        "device_id": "test-device",
        "timestamp": 1234567890.0,
        "text": "Hello world",
        "final": True
    }

    # Validate dict first (pre-decode)
    result = validate_message_dict(raw_dict)
    assert result["valid"], f"Validation failed: {result.get('errors')}"

    # Decode to typed model
    msg = decode_message(json.dumps(raw_dict))
    assert isinstance(msg, TRANSCRIPTION)
    assert msg.text == "Hello world"
    assert msg.final is True


def test_decode_invalid_type():
    raw_dict = {
        "protocol": "LOVE/1.0",
        "type": "NOT_A_REAL_TYPE",
        "device_id": "dot-kitchen",
        "timestamp": 1234567890.0
    }

    # Validation fails cleanly
    result = validate_message_dict(raw_dict)
    assert not result["valid"]
    assert any("not a valid enumeration member" in e for e in result["errors"])


    # decode_message will raise hard
    with pytest.raises(ValueError, match="Unknown message type"):
        decode_message(json.dumps(raw_dict))
