from threading import Thread
from typing import List

from time import sleep

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot_action_client import ApiClient, Configuration
from rlbot_action_server.bot_action_broker import BotActionBroker, run_action_server, find_usable_port
from rlbot_action_server.bot_holder import set_bot_action_broker
from rlbot_action_server.models import BotAction, AvailableActions, ActionChoice
from rlbot_twitch_broker_client import ActionServerRegistration
from rlbot_twitch_broker_client.api.register_api import RegisterApi
from rlbot_twitch_broker_client.defaults import STANDARD_TWITCH_BROKER_PORT
from urllib3.exceptions import MaxRetryError


class MyActionBroker(BotActionBroker):
    def __init__(self, bot):
        self.bot = bot
        self.current_action: BotAction = None

    def get_actions_currently_available(self) -> List[AvailableActions]:
        return self.bot.get_actions_currently_available()

    def set_action(self, choice: ActionChoice):
        self.current_action = choice.action


class MyBot(BaseAgent):

    def __init__(self, name, team, index):
        super().__init__(name, team, index)
        self.action_broker = MyActionBroker(self)

    def initialize_agent(self):
        port = find_usable_port(8080)
        Thread(target=run_action_server, args=(port,), daemon=True).start()
        set_bot_action_broker(self.action_broker)  # This now works on initial load

        Thread(target=self.stay_connected_to_twitch_broker, args=(port,), daemon=True).start()

    def stay_connected_to_twitch_broker(self, port):
        register_api_config = Configuration()
        register_api_config.host = f"http://127.0.0.1:{STANDARD_TWITCH_BROKER_PORT}"
        twitch_broker_register = RegisterApi(ApiClient(configuration=register_api_config))
        while True:
            try:
                twitch_broker_register.register_action_server(
                    ActionServerRegistration(base_url=f"http://127.0.0.1:{port}"))
            except MaxRetryError:
                self.logger.warning('Failed to register with twitch broker, will try again...')
            sleep(10)

    def get_actions_currently_available(self) -> List[AvailableActions]:
        actions = AvailableActions(entity_name="ActionBot", current_action=self.action_broker.current_action,
                                   available_actions=[
                                       BotAction(description="Turn left", action_type="turn", data={'value': -1}),
                                       BotAction(description="Drive straight", action_type="turn", data={'value': 0}),
                                       BotAction(description="Turn right", action_type="turn", data={'value': 1}),
                                       BotAction(description="Stop", action_type="throttle", data={'value': 0}),
                                       BotAction(description="Go", action_type="throttle", data={'value': 1}),
                                       BotAction(description="Boost", action_type="boost", data={'value': True}),
                                       BotAction(description="Unboost", action_type="boost", data={'value': False}),
                                   ])
        return [actions]

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        controls = SimpleControllerState()
        if self.action_broker.current_action:
            if self.action_broker.current_action.action_type == 'turn':
                controls.steer = self.action_broker.current_action.data['value']
            if self.action_broker.current_action.action_type == 'throttle':
                controls.throttle = self.action_broker.current_action.data['value']
            if self.action_broker.current_action.action_type == 'boost':
                controls.boost = self.action_broker.current_action.data['value']
        return controls
