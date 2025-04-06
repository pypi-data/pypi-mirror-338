# File: tests/test_examples.py

import pytest
from examples.messages.registry import EXAMPLE_MESSAGES
from love_protocol.core.validate import validate_message_dict


@pytest.mark.parametrize("type_name,message", EXAMPLE_MESSAGES.items())
def test_example_message_is_valid(type_name, message):
    """
    Validates that each example message passes full schema + version checks.
    """
    raw = message.dict()
    result = validate_message_dict(raw, strict=False)

    assert result["valid"], f"Message of type '{type_name}' is invalid: {result.get('errors')}"
