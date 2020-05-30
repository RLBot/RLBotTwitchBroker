from pathlib import Path

import connexion
import flask
from rlbot_twitch_broker_server import chat_buffer
from rlbot_twitch_broker_server.models.api_response import ApiResponse  # noqa: E501
from rlbot_twitch_broker_server.models.chat_line import ChatLine  # noqa: E501


def send_chat(body):  # noqa: E501
    if connexion.request.form:
        chat_line = ChatLine.from_dict(connexion.request.form)
        chat_buffer.CHAT_BUFFER.enqueue_chat(chat_line)
        return ApiResponse(200, 'Chat received')
    return ApiResponse(400, 'Malformed request')
