import connexion
from rlbot_twitch_broker_server import client_registry
from rlbot_twitch_broker_server.client_registry import ActionServerData
from rlbot_twitch_broker_server.models.action_server_registration import ActionServerRegistration  # noqa: E501
from rlbot_twitch_broker_server.models.api_response import ApiResponse  # noqa: E501


def register_action_server(body):  # noqa: E501
    body = ActionServerRegistration.from_dict(connexion.request.get_json())  # noqa: E501

    registry = client_registry.CLIENT_REGISTRY
    if registry:
        client_data = ActionServerData(base_url=body.base_url)
        registry.register_client(client_data)
        message = f"Successfully registered {client_data.base_url}."
        print(message)
        return ApiResponse(200, message)
