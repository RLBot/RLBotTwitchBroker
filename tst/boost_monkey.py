from threading import Thread
from typing import List

from rlbot.agents.base_script import BaseScript
from rlbot.utils.game_state_util import CarState, GameState
from rlbot.utils.structures.game_data_struct import PlayerInfo
from rlbot_action_server.bot_action_broker import BotActionBroker, run_action_server, find_usable_port
from rlbot_action_server.bot_holder import set_bot_action_broker
from rlbot_action_server.models import BotAction, AvailableActions, ActionChoice
from rlbot_twitch_broker_client import Configuration, RegisterApi, ApiClient, ActionServerRegistration
from rlbot_twitch_broker_client.defaults import STANDARD_TWITCH_BROKER_PORT
from time import sleep
from urllib3.exceptions import MaxRetryError

GIVE_FULL_BOOST = 'giveFullBoost'
REMOVE_BOOST = 'removeBoost'
PLAYER_NAME = 'playerName'


class MyActionBroker(BotActionBroker):
    def __init__(self, script):
        self.script = script
        self.current_action: BotAction = None

    def get_actions_currently_available(self) -> List[AvailableActions]:
        return self.script.get_actions_currently_available()

    def set_action(self, choice: ActionChoice):
        self.current_action = choice.action


class BoostMonkey(BaseScript):

    def __init__(self):
        super().__init__("Boost Monkey")
        self.action_broker = MyActionBroker(self)
        self.known_players: List[PlayerInfo] = []

    def heartbeat_connection_attempts_to_twitch_broker(self, port):
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

    def start(self):
        port = find_usable_port(9097)
        Thread(target=run_action_server, args=(port,), daemon=True).start()
        set_bot_action_broker(self.action_broker)  # This seems to only work after the bot hot reloads once, weird.

        Thread(target=self.heartbeat_connection_attempts_to_twitch_broker, args=(port,), daemon=True).start()

        while True:
            packet = self.get_game_tick_packet()
            raw_players = [self.game_tick_packet.game_cars[i]
                           for i in range(packet.num_cars)]
            self.known_players = [p for p in raw_players if p.name]

            current_action: BotAction = self.action_broker.current_action
            if current_action:
                boost_amount = 0
                if current_action.action_type == GIVE_FULL_BOOST:
                    boost_amount = 100
                player_index = self.get_player_index_by_name(current_action.data[PLAYER_NAME])
                if player_index is not None:
                    self.set_game_state(
                        GameState(cars={player_index: CarState(boost_amount=boost_amount)}))
                self.action_broker.current_action = None

            sleep(0.5)

    def get_player_index_by_name(self, name: str):
        for i in range(self.game_tick_packet.num_cars):
            car = self.game_tick_packet.game_cars[i]
            if car.name == name:
                return i
        return None

    def get_actions_currently_available(self) -> List[AvailableActions]:
        actions = []
        for player in self.known_players:
            actions.append(BotAction(description=f'Give {player.name} full boost', action_type=GIVE_FULL_BOOST,
                                     data={PLAYER_NAME: player.name}))
            actions.append(BotAction(description=f'Take boost away from {player.name}', action_type=REMOVE_BOOST,
                                     data={PLAYER_NAME: player.name}))

        return [AvailableActions("Boost Monkey", None, actions)]


if __name__ == '__main__':
    boost_monkey = BoostMonkey()
    boost_monkey.start()
