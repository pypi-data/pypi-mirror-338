# File: love_protocol/session/model.py

"""
Session models for LOVE protocol.

Defines structured models for representing session state and audio buffer content.
These models are used for in-memory session tracking and management within middleware
and other context-aware components.
"""

from pydantic import BaseModel, Field
from typing import List, Literal
import time

__all__ = ["LoveSession", "SessionBuffer"]

class SessionBuffer(BaseModel):
    """
    Holds temporary session data such as audio and transcripts.

    Attributes:
        audio_chunks (List[dict]): A list of raw audio chunks (typically dicts with metadata).
        transcripts (List[str]): A list of transcribed text segments.
    """
    audio_chunks: List[dict] = Field(default_factory=list)
    transcripts: List[str] = Field(default_factory=list)


class LoveSession(BaseModel):
    """
    Represents the state and metadata of an active or historical LOVE session.

    Attributes:
        session_id (str): Unique identifier for the session.
        device_id (str): The device that initiated or owns the session.
        start_time (float): Timestamp when the session was created (seconds since epoch).
        last_seen (float): Timestamp of the last activity within the session.
        state (Literal): Session state: 'idle', 'active', or 'ended'.
        buffer (SessionBuffer): Temporary data collected during the session.
    """
    session_id: str
    device_id: str
    start_time: float = Field(default_factory=lambda: time.time())
    last_seen: float = Field(default_factory=lambda: time.time())
    state: Literal["idle", "active", "ended"] = "idle"
    buffer: SessionBuffer = Field(default_factory=SessionBuffer)
