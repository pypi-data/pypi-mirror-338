from love_protocol.types.transcription import TRANSCRIPTION

def valid_transcription() -> TRANSCRIPTION:
    return TRANSCRIPTION(
        protocol="LOVE/1.0",
        type="TRANSCRIPTION",
        device_id="test-device",
        timestamp=1234567890.0,
        text="Hello world",
        final=True
    )
