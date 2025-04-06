# File: tests/test_encode.py

import json
from love_protocol.types.hello import HELLO
from love_protocol.core.encode import encode_message


def test_encode_hello():
    msg = HELLO(
        protocol="LOVE/1.0",
        type="HELLO",
        device_id="kitchen-dot",
        timestamp=1234567.89,
        capabilities={"mic": True, "speaker": True}
    )

    output = encode_message(msg)

    try:
        obj = json.loads(output)
    except json.JSONDecodeError as e:
        pytest.fail(f"Output is not valid JSON: {e}")

    assert isinstance(obj, dict)
    assert obj["type"] == "HELLO"
    assert obj["protocol"] == "LOVE/1.0"
    assert obj["device_id"] == "kitchen-dot"
    assert obj["timestamp"] == 1234567.89
    assert obj["capabilities"]["mic"] is True
    assert obj["capabilities"]["speaker"] is True
