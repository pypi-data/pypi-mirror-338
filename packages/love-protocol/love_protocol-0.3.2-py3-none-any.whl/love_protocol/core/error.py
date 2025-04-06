# File: love_protocol/core/error.py

"""
Module for generating structured ERROR messages in the LOVE protocol.

This module is responsible for creating and serializing validation or
runtime error messages that conform to the LOVE protocol format.
"""

import time
from love_protocol.types.error import ERROR

__all__ = ["encode_error"]


def encode_error(errors: list[str] | str) -> str:
    """
    Creates a serialized ERROR message from one or more validation issues.

    This function wraps a list of errors (or a single string) into a
    LOVE protocol-compliant `ERROR` message and returns the serialized JSON.

    Args:
        errors: A list of error strings or a single error string.

    Returns:
        A JSON string representing the structured ERROR message.
    """
    from love_protocol.core.encode import encode_message  # Lazy-import to avoid circular dependency

    if isinstance(errors, str):
        errors = [errors]

    msg = ERROR(
        protocol="LOVE/1.0",
        type="ERROR",
        device_id="system",
        timestamp=time.time(),
        message="Validation failed",
        details=errors,
    )
    return encode_message(msg)
