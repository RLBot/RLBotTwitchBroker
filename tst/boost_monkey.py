from threading import Thread
from typing import List

from rlbot.utils.game_state_util import CarState, GameState
from rlbot.utils.logging_utils import get_logger
from rlbot.utils.structures.game_data_struct import GameTickPacket, PlayerInfo
from rlbot.utils.structures.game_interface import GameInterface
from rlbot_action_server.bot_action_broker import BotActionBroker, run_action_server
from rlbot_action_server.bot_holder import set_bot_action_broker
from rlbot_action_server.models import BotAction, AvailableActions, ActionChoice
from time import sleep

GIVE_FULL_BOOST = 'giveFullBoost'
REMOVE_BOOST = 'removeBoost'
PLAYER_NAME = 'playerName'

class MyActionBroker(BotActionBroker):
    def __init__(self, bot):
        self.bot = bot
        self.current_action: BotAction

    def get_actions_currently_available(self) -> AvailableActions:
        return self.bot.get_actions_currently_available()

    def set_action(self, choice: ActionChoice):
        self.current_action = choice.action


class BoostMonkey():

    def __init__(self):
        self.logger = get_logger('bstmnk')
        self.game_interface = GameInterface(self.logger)
        self.game_tick_packet = GameTickPacket()
        self.action_broker = MyActionBroker(self)
        self.known_players: List[PlayerInfo] = []

    def start(self):
        self.game_interface.load_interface()
        action_server_thread = Thread(target=run_action_server, args=(9097,))
        action_server_thread.setDaemon(True)
        action_server_thread.start()
        set_bot_action_broker(self.action_broker)  # This seems to only work after the bot hot reloads once, weird.
        while True:
            self.game_interface.update_live_data_packet(self.game_tick_packet)
            raw_players = [self.game_tick_packet.game_cars[i]
                           for i in range(self.game_tick_packet.num_cars)]
            self.known_players = [p for p in raw_players if p.name]

            current_action: BotAction = self.action_broker.current_action
            if current_action:
                boost_amount = 0
                if current_action.action_type == GIVE_FULL_BOOST:
                    boost_amount = 100
                player_index = self.get_player_index_by_name(current_action.data[PLAYER_NAME])
                if player_index is not None:
                    self.game_interface.set_game_state(GameState(cars={player_index: CarState(boost_amount=boost_amount)}))
                self.action_broker.current_action = None

            sleep(0.5)

    def get_player_index_by_name(self, name: str):
        for i in range(self.game_tick_packet.num_cars):
            car = self.game_tick_packet.game_cars[i]
            if car.name == name:
                return i
        return None


    def get_actions_currently_available(self) -> AvailableActions:
        actions = []
        for player in self.known_players:
            actions.append(BotAction(description=f'Give {player.name} full boost', action_type=GIVE_FULL_BOOST, data={PLAYER_NAME: player.name}))
            actions.append(BotAction(description=f'Take boost away from {player.name}', action_type=REMOVE_BOOST, data={PLAYER_NAME: player.name}))

        return AvailableActions(None, actions)


if __name__ == '__main__':
    boost_monkey = BoostMonkey()
    boost_monkey.start()
