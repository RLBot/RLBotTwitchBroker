from rlbot.agents.base_agent import BaseAgent
from rlbot_action_server import encoder
from rlbot_action_server.models import AvailableActions
from pathlib import Path


class BaseAgentWithActionSupport(BaseAgent):
    def get_actions_currently_available(self) -> AvailableActions:
        raise NotImplementedError()
    
    def set_action(self, action):
        raise NotImplementedError()

    def run_action_server(self):
        import connexion
        spec_dir = Path(__file__).parent / 'swagger'
        app = connexion.App(__name__, specification_dir=spec_dir)
        app.app.json_encoder = encoder.JSONEncoder
        app.add_api('swagger.yaml', arguments={'title': 'Bot Action Server'}, pythonic_params=True)
        app.run(port=8080)
        


print('initializing _bot as None')
_bot: BaseAgentWithActionSupport = None

def set_bot(bot: BaseAgentWithActionSupport):
    global _bot
    _bot = bot

def get_bot() -> BaseAgentWithActionSupport:
    return _bot