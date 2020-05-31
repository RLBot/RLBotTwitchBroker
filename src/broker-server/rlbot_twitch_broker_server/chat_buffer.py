from dataclasses import dataclass
from typing import Dict, List

from rlbot_twitch_broker_server.models import ChatLine


class ChatBuffer:

    def __init__(self):
        self.chat_lines: List[ChatLine] = []

    def enqueue_chat(self, chat: ChatLine):
        self.chat_lines.append(chat)

    def dequeue_chat(self) -> ChatLine:
        return self.chat_lines.pop(0)

    def has_chat(self):
        return len(self.chat_lines) > 0


CHAT_BUFFER: ChatBuffer = ChatBuffer()
