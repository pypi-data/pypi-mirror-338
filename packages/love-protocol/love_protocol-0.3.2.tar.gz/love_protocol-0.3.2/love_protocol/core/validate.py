# File: love_protocol/core/validate.py

"""
Validation utilities for the LOVE protocol.

This module provides functions to validate raw LOVE protocol message dictionaries
against the base schema and message-type-specific models. It performs structural,
version, and semantic validation of incoming messages.
"""

from pydantic import ValidationError
from love_protocol.constants import MESSAGE_TYPE_TO_CLASS
from love_protocol.types.love_message import LOVEMESSAGE

__all__ = ["_check_protocol_version", "validate_message_dict"]


PROTOCOL_VERSION = "LOVE/1.0"


def _check_protocol_version(actual: str, strict: bool) -> str | None:
    """
    Compares the protocol version of a message to the expected version.

    Only the major.minor components are compared (e.g., '1.0' vs '2.0').

    Args:
        actual: The protocol version string from the message (e.g., 'LOVE/1.0').
        strict: If True, raises ValueError on version mismatch.

    Returns:
        An error message string if the versions are incompatible, otherwise None.

    Raises:
        ValueError: If strict is True and version mismatch occurs.
    """
    expected = PROTOCOL_VERSION.split("/")[1].rsplit(".", 1)[0]
    got = actual.split("/")[1].rsplit(".", 1)[0]

    if expected != got:
        msg = f"Incompatible protocol version: expected {PROTOCOL_VERSION}, got {actual}"
        if strict:
            raise ValueError(msg)
        return msg
    return None


def validate_message_dict(obj: dict, strict: bool = False) -> dict:
    """
    Validates a decoded LOVE message dictionary against the schema.

    This includes:
    - Base validation of required fields (e.g., protocol, type, timestamp)
    - Protocol version check (major.minor)
    - Type-specific payload validation based on message `type`

    Args:
        obj: The message dictionary to validate.
        strict: If True, raises exceptions on errors.

    Returns:
        A dictionary indicating the result:
            {
                "valid": bool,
                "errors": list[str]  # only if invalid
            }

    Raises:
        ValidationError: If base or type-specific model validation fails and `strict` is True.
        ValueError: If message type is unknown or protocol version is invalid in strict mode.
    """
    errors = []

    # Step 1: Validate base fields using LOVEMESSAGE
    try:
        base = LOVEMESSAGE(**obj)
    except ValidationError as e:
        errors.extend([f"{'.'.join(str(loc) for loc in err['loc'])}: {err['msg']}" for err in e.errors()])
        if strict:
            raise
        return {"valid": False, "errors": errors}

    # Step 2: Validate protocol version
    version_error = _check_protocol_version(base.protocol, strict)
    if version_error:
        return {"valid": False, "errors": [version_error]}

    # Step 3: Validate full payload based on type
    type_name = base.type.value if hasattr(base.type, "value") else str(base.type)
    model_class = MESSAGE_TYPE_TO_CLASS.get(type_name)

    if model_class is None:
        msg = f"Unknown type '{type_name}' – no model registered"
        if strict:
            raise ValueError(msg)
        return {"valid": False, "errors": [msg]}

    try:
        model_class(**obj)  # perform full model validation
    except ValidationError as e:
        errors.extend([f"{'.'.join(str(loc) for loc in err['loc'])}: {err['msg']}" for err in e.errors()])
        if strict:
            raise
        return {"valid": False, "errors": errors}

    return {"valid": True}
