"""
This module contains the EventEncoder class
"""

from agentwire.core.events import BaseEvent

AGENTWIRE_MEDIA_TYPE = "application/vnd.agentwire.event+proto"

class EventEncoder:
    """
    Encodes Agent Wire events.
    """
    def __init__(self, accept: str = None):
        pass

    def encode(self, event: BaseEvent) -> str:
        """
        Encodes an event.
        """
        return self.encode_sse(event)

    def encode_sse(self, event: BaseEvent) -> str:
        """
        Encodes an event into an SSE string.
        """
        return f"data: {event.model_dump_json()}\n\n"
