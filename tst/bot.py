from threading import Thread

from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot_action_server.bot_action_broker import BotActionBroker, run_action_server
from rlbot_action_server.bot_holder import set_bot_action_broker
from rlbot_action_server.models import BotAction, AvailableActions

from models.action_choice import ActionChoice


class MyActionBroker(BotActionBroker):
    def __init__(self, bot):
        self.bot = bot
        self.current_action: BotAction = None

    def get_actions_currently_available(self) -> AvailableActions:
        return self.bot.get_actions_currently_available()

    def set_action(self, choice: ActionChoice):
        self.current_action = choice.action

class MyBot(BaseAgent):

    def __init__(self, name, team, index):
        super().__init__(name, team, index)
        self.current_action: BotAction = None
        self.action_broker = MyActionBroker(self)

    def start_server(self):
        run_action_server(preferred_port=8080)

    def initialize_agent(self):
        action_server_thread = Thread(target=self.start_server)
        action_server_thread.setDaemon(True)
        action_server_thread.start()
        set_bot_action_broker(self.action_broker)  # This now works on initial load


    def get_actions_currently_available(self) -> AvailableActions:
        return AvailableActions(self.current_action, [
            BotAction(description="Turn left", action_type="turn", data={'value': -1}),
            BotAction(description="Turn right", action_type="turn", data={'value': 1})
        ])

    def get_output(self, packet: GameTickPacket) -> SimpleControllerState:
        steer = 0
        if self.current_action:
            steer = self.current_action['value']
        return SimpleControllerState(throttle=True, steer=steer)
