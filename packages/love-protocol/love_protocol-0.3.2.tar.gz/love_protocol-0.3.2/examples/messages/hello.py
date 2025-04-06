from love_protocol.types.hello import HELLO, Capabilities

def valid_hello() -> HELLO:
    return HELLO(
        protocol="LOVE/1.0",
        type="HELLO",
        device_id="dot-kitchen",
        timestamp=1711972643.42,
        capabilities=Capabilities(
            mic=True,
            speaker=True,
            tts=False,
            wakeword=True
        )
    )
