import connexion
import six

from rlbot_action_server.models.action_choice import ActionChoice  # noqa: E501
from rlbot_action_server.models.api_response import ApiResponse  # noqa: E501
from rlbot_action_server.models.available_actions import AvailableActions  # noqa: E501
from rlbot_action_server import util

from rlbot_action_server import bot_holder


def choose_action(body):
    if connexion.request.is_json:
        body = ActionChoice.from_dict(connexion.request.get_json())
        bot = bot_holder.get_bot_action_broker()
        if bot is not None:
            bot.set_action(body)
            return f'set action on {bot.name}!'
        
        return 'oh no bot is none'
        
    return 'do some magic, but request is not json!'


def get_actions_currently_available():
    bot = bot_holder.get_bot_action_broker()
    if bot is not None:
        return bot.get_actions_currently_available().to_dict()
    return 'do some magic but bot is none!'
