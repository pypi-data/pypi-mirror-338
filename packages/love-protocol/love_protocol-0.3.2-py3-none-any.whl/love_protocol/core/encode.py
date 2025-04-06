# File: love_protocol/core/encode.py

"""
Module for encoding LOVE protocol messages into JSON strings.

This module provides utilities to serialize `LoveMessage` objects
into JSON format for transmission over the wire. It also supports
generating and encoding structured error messages.
"""

import json
import time
from love_protocol.constants import LoveMessage
from love_protocol.types.error import ERROR as LoveError

__all__ = ["encode_message", "encode_error"]

def encode_message(message: LoveMessage, pretty: bool = False) -> str:
    """
    Serializes a LOVE message into a JSON string.

    Args:
        message: A `LoveMessage` instance to encode.
        pretty: If True, the JSON is pretty-printed with indentation.

    Returns:
        A string containing the JSON-encoded message.
    """
    data = message.dict()

    if pretty:
        return json.dumps(data, indent=2, sort_keys=True)
    return json.dumps(data)


def encode_error(e: Exception, device_id: str = "", session: str = "") -> str:
    """
    Creates and encodes a structured LOVE error message.

    Args:
        e: The original exception to include in the error message.
        device_id: The ID of the device reporting the error (optional).
        session: The session ID associated with the error (optional).

    Returns:
        A JSON string representing the encoded LOVE error message.
    """
    err = LoveError(
        reason=str(e),
        timestamp=time.time(),
        device_id=device_id,
        session=session
    )
    return encode_message(err)
