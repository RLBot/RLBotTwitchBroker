import socket
from pathlib import Path

import connexion
from rlbot_action_server import encoder
from rlbot_action_server.models import AvailableActions

from models.action_choice import ActionChoice


class BotActionBroker:
    def get_actions_currently_available(self) -> AvailableActions:
        raise NotImplementedError()

    def set_action(self, action: ActionChoice):
        raise NotImplementedError()


def run_action_server(preferred_port: int):
    port = find_usable_port(preferred_port)
    spec_dir = Path(__file__).parent / 'swagger'
    app = connexion.App(__name__, specification_dir=spec_dir)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'BotActionServer'}, pythonic_params=True)
    app.run(port=port)


def find_usable_port(desired_port: int):
    for port_to_test in range(desired_port, 65535):
        if is_port_accessible(port_to_test):
            return port_to_test
    raise PermissionError('Unable to find a usable port for running an action server! Is your antivirus messing you up? '
                          'Check https://github.com/RLBot/RLBot/wiki/Antivirus-Notes')


def is_port_accessible(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind(('127.0.0.1', port))
            return True
        except:
            return False
