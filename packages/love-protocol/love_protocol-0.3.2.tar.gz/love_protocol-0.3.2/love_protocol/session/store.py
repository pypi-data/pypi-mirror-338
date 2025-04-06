# File: love_protocol/session/store.py

"""
Provides an in-memory session store for managing LOVE protocol sessions.

This class handles creation, retrieval, updating, deletion und Ablaufkontrolle
von Session-Daten basierend auf Zeit und Kontext. Sessions enthalten Metainformationen
wie den Zustand, das zugehörige Gerät und temporäre Pufferdaten.
"""

from typing import Dict, Optional
import time
import uuid
from love_protocol.session.model import LoveSession

__all__ = ["SessionStore"]

class SessionStore:
    """
    In-memory store for managing LOVE protocol sessions.

    Methods:
        create(device_id, session_id): Create a new session.
        create_or_replace(data): Insert or replace a session object.
        update(session_id, patch): Patch an existing session.
        get(session_id): Retrieve a session by ID.
        exists(session_id): Check if a session exists.
        delete(session_id): Remove a session by ID.
        list(): Return a list of all active sessions.
        cleanup(ttl_seconds): Delete expired sessions based on last_seen timestamp.
    """

    def __init__(self):
        """Initialize an empty session store."""
        self._sessions: Dict[str, LoveSession] = {}

    def create(self, device_id: str, session_id: Optional[str] = None) -> str:
        """
        Create a new session entry with a unique or provided session ID.

        Args:
            device_id: ID of the device that starts the session.
            session_id: Optional custom session ID.

        Returns:
            The session ID of the newly created session.
        """
        session_id = session_id or str(uuid.uuid4())
        now = time.time()

        session = LoveSession(
            session_id=session_id,
            device_id=device_id,
            start_time=now,
            last_seen=now,
            state="idle"
        )
        self._sessions[session_id] = session
        return session.session_id

    def create_or_replace(self, data: LoveSession) -> LoveSession:
        """
        Insert or replace a session using a complete LoveSession object.

        Args:
            data: A valid LoveSession instance.

        Returns:
            The inserted or replaced LoveSession object.
        """
        self._sessions[data.session_id] = data
        return data

    def update(self, session_id: str, patch: dict) -> None:
        """
        Update a session by applying a patch dictionary.

        Args:
            session_id: ID of the session to update.
            patch: Dict of fields to overwrite.

        Notes:
            Automatically updates `last_seen` timestamp.
        """
        existing = self._sessions.get(session_id)
        if not existing:
            return

        updated = existing.copy(update=patch)
        updated.last_seen = time.time()
        self._sessions[session_id] = updated

    def get(self, session_id: str) -> Optional[LoveSession]:
        """
        Retrieve a session by ID.

        Args:
            session_id: The session ID to look up.

        Returns:
            The corresponding LoveSession or None.
        """
        return self._sessions.get(session_id)

    def exists(self, session_id: str) -> bool:
        """
        Check if a session ID is currently stored.

        Args:
            session_id: Session ID to check.

        Returns:
            True if session exists, else False.
        """
        return session_id in self._sessions

    def delete(self, session_id: str) -> None:
        """
        Remove a session by ID.

        Args:
            session_id: Session ID to remove.
        """
        self._sessions.pop(session_id, None)

    def list(self) -> list[LoveSession]:
        """
        List all currently active sessions.

        Returns:
            A list of LoveSession objects.
        """
        return list(self._sessions.values())

    def cleanup(self, ttl_seconds: int) -> None:
        """
        Remove sessions whose `last_seen` is older than the TTL threshold.

        Args:
            ttl_seconds: Time-to-live duration in seconds.
        """
        now = time.time()
        expired = [sid for sid, s in self._sessions.items()
                   if now - s.last_seen > ttl_seconds]
        for sid in expired:
            self.delete(sid)
