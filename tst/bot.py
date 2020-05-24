import math
import os

from threading import Thread

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket

from rlbot_action_server import encoder
from rlbot_action_server import bot_holder
from rlbot_action_server.bot_holder import BaseAgentWithActionSupport, set_bot
from rlbot_action_server.models import BotAction, AvailableActions, ActionChoice
from rlbot_action_server import swagger


class MyBot(BaseAgentWithActionSupport):

    def __init__(self, name, team, index):
        super().__init__(name, team, index)
        self.current_action: ActionChoice = None

    def initialize_agent(self):
        action_server_thread = Thread(target=self.run_action_server)
        action_server_thread.setDaemon(True)
        action_server_thread.start()
        set_bot(self) # This seems to only work after the bot hot reloads once, weird.


    def get_actions_currently_available(self) -> AvailableActions:
        return AvailableActions(self.current_action, [
            BotAction('getBoost'), 
            BotAction('shoot')
        ])
    
    def set_action(self, action: ActionChoice):
        self.current_action = action

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        return SimpleControllerState(throttle=True)