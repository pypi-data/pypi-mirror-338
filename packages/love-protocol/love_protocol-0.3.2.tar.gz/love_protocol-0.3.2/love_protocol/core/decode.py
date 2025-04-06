# File: love_protocol/core/decode.py

"""
Module for decoding LOVE protocol messages from JSON strings.

This module provides a utility function to parse and validate
a LOVE protocol message by dispatching it to the correct Pydantic model
based on its "type" field.
"""

import json
from typing import Any
from love_protocol.constants import MESSAGE_TYPE_TO_CLASS, LoveMessage

__all__ = ["decode_message"]

def decode_message(json_str: str) -> LoveMessage:
    """
    Decodes a JSON string into the appropriate LOVE message class.

    This function parses a JSON string, inspects the "type" field,
    and returns an instance of the corresponding Pydantic model class
    from `MESSAGE_TYPE_TO_CLASS`.

    Args:
        json_str: The JSON string representing a LOVE protocol message.

    Returns:
        An instance of a subclass of `LoveMessage` corresponding to the type.

    Raises:
        ValueError: If the "type" field is missing or not recognized.
        json.JSONDecodeError: If the input string is not valid JSON.
    """
    data: dict[str, Any] = json.loads(json_str)

    message_type = data.get("type")
    if not message_type:
        raise ValueError("Missing 'type' field in message.")

    message_cls = MESSAGE_TYPE_TO_CLASS.get(message_type)
    if not message_cls:
        raise ValueError(f"Unknown message type: {message_type}")

    return message_cls(**data)
