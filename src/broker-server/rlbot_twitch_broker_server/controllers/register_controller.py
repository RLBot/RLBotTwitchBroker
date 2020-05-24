import connexion
import six

from rlbot_twitch_broker_server.models.action_server_registration import ActionServerRegistration  # noqa: E501
from rlbot_twitch_broker_server.models.api_response import ApiResponse  # noqa: E501
from rlbot_twitch_broker_server import util

KNOWN_ACTION_SERVERS = {}

def register_action_server(body):  # noqa: E501
    body = ActionServerRegistration.from_dict(connexion.request.get_json())  # noqa: E501
    server_key = connexion.request.remote_addr()
    KNOWN_ACTION_SERVERS[server_key] = body
    return ApiResponse(200, f"Successfully registered {server_key}.").to_dict()
