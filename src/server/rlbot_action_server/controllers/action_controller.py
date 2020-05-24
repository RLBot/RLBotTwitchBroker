import connexion
import six

from rlbot_action_server.models.action_choice import ActionChoice  # noqa: E501
from rlbot_action_server.models.api_response import ApiResponse  # noqa: E501
from rlbot_action_server.models.available_actions import AvailableActions  # noqa: E501
from rlbot_action_server import util


def choose_action(body):  # noqa: E501
    """choose_action

     # noqa: E501

    :param body: Action to choose
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = ActionChoice.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_actions_currently_available():  # noqa: E501
    """get_actions_currently_available

     # noqa: E501


    :rtype: AvailableActions
    """
    return 'do some magic!'
