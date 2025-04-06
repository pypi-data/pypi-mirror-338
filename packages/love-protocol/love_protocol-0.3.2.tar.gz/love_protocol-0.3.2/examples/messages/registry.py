from love_protocol.types.love_message import LOVEMESSAGE

from examples.messages.hello import valid_hello
from examples.messages.transcription import valid_transcription
from examples.messages.audio_chunk import valid_audio_chunk

EXAMPLE_MESSAGES: dict[str, LOVEMESSAGE] = {
    "HELLO": valid_hello(),
    # "TRANSCRIPTION": valid_transcription(),
    # "AUDIO_CHUNK": valid_audio_chunk(),
}
