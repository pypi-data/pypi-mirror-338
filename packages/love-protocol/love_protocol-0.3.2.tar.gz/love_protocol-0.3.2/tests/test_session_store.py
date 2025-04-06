# File: tests/test_session_store.py

import time
from love_protocol.session.store import SessionStore


def test_create_and_get_session():
    store = SessionStore()
    session_id = store.create("test-device")
    session = store.get(session_id)
    assert session is not None
    assert session.device_id == "test-device"
    assert session.state == "idle"
    assert session.buffer.audio_chunks == []
    assert session.buffer.transcripts == []


def test_update_session():
    store = SessionStore()
    session_id = store.create("test-device")
    store.update(session_id, {"state": "active"})
    updated = store.get(session_id)
    assert updated is not None
    assert updated.state == "active"


def test_delete_session():
    store = SessionStore()
    session_id = store.create("test-device")
    store.delete(session_id)
    assert store.get(session_id) is None


def test_session_expiry():
    store = SessionStore()
    session_id = store.create("test-device")
    assert store.get(session_id) is not None

    # Cleanup should not remove session yet
    store.cleanup(ttl_seconds=1)
    assert store.get(session_id) is not None

    # Wait until TTL expires
    time.sleep(1.5)
    store.cleanup(ttl_seconds=1)
    assert store.get(session_id) is None
