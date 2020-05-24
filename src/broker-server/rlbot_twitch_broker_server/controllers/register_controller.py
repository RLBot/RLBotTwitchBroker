import connexion
import six

from rlbot_twitch_broker_server.models.action_server_registration import ActionServerRegistration  # noqa: E501
from rlbot_twitch_broker_server.models.api_response import ApiResponse  # noqa: E501
from rlbot_twitch_broker_server import util


def register_action_server(body):  # noqa: E501
    """register_action_server

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = ActionServerRegistration.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
