from love_protocol.types.audio_chunk import AUDIOCHUNK

def valid_audio_chunk() -> AUDIOCHUNK:
    return AUDIOCHUNK(
        protocol="LOVE/1.0",
        type="AUDIO_CHUNK",
        device_id="dot-mic",
        timestamp=1234567890.0,
        data="UklGRlgAAABXQVZFZm10IBAAAAABAAEAIlYAAESsAAACABAAZGF0YQAAAAA="  # fake base64
    )
