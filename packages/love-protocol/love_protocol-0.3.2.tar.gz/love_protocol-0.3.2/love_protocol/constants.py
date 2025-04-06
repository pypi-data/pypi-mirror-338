"""
Auto-generated mapping of LOVE message types to Pydantic model classes.
"""

from typing import Type, Union

from love_protocol.types.audio_chunk import AUDIOCHUNK
from love_protocol.types.audio_start import AUDIOSTART
from love_protocol.types.audio_stop import AUDIOSTOP
from love_protocol.types.command import COMMAND
from love_protocol.types.error import ERROR
from love_protocol.types.hello import HELLO
from love_protocol.types.hello_ack import HELLOACK
from love_protocol.types.intent_detected import INTENTDETECTED
from love_protocol.types.love_message import LOVEMESSAGE
from love_protocol.types.media_control import MEDIACONTROL
from love_protocol.types.media_play import MEDIAPLAY
from love_protocol.types.sensor_event import SENSOREVENT
from love_protocol.types.transcription import TRANSCRIPTION
from love_protocol.types.tts_output import TTSOUTPUT
from love_protocol.types.wakeword_detected import WAKEWORDDETECTED

MESSAGE_TYPE_TO_CLASS: dict[str, Type[LOVEMESSAGE]] = {
    "AUDIO_CHUNK": AUDIOCHUNK,
    "AUDIO_START": AUDIOSTART,
    "AUDIO_STOP": AUDIOSTOP,
    "COMMAND": COMMAND,
    "ERROR": ERROR,
    "HELLO": HELLO,
    "HELLO_ACK": HELLOACK,
    "INTENT_DETECTED": INTENTDETECTED,
    "MEDIA_CONTROL": MEDIACONTROL,
    "MEDIA_PLAY": MEDIAPLAY,
    "SENSOR_EVENT": SENSOREVENT,
    "TRANSCRIPTION": TRANSCRIPTION,
    "TTS_OUTPUT": TTSOUTPUT,
    "WAKEWORD_DETECTED": WAKEWORDDETECTED,
}

LoveMessage = Union[
    AUDIOCHUNK,
    AUDIOSTART,
    AUDIOSTOP,
    COMMAND,
    ERROR,
    HELLO,
    HELLOACK,
    INTENTDETECTED,
    MEDIACONTROL,
    MEDIAPLAY,
    SENSOREVENT,
    TRANSCRIPTION,
    TTSOUTPUT,
    WAKEWORDDETECTED,
]
