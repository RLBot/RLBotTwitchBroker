from threading import Thread

from rlbot_action_client import Configuration, ActionApi, ApiClient, AvailableActions
from time import sleep

from rlbot_twitch_broker_server import client_registry
from rlbot_twitch_broker_server.run import find_usable_port, run_twitch_broker_server

def run_twitch_broker(desired_port: int):
    port = find_usable_port(desired_port)
    action_server_thread = Thread(target=run_twitch_broker_server, args=(port,))
    action_server_thread.setDaemon(True)
    action_server_thread.start()
    client_registry.CLIENT_REGISTRY = client_registry.ClientRegistry()

    while True:
        sleep(3)
        registry = client_registry.CLIENT_REGISTRY
        for client in list(registry.clients.values()):
            bot_action_api_config = Configuration()
            bot_action_api_config.host = client.base_url
            action_api = ActionApi(ApiClient(configuration=bot_action_api_config))
            api_response: AvailableActions = action_api.get_actions_currently_available()
            print(f'response from {client.base_url}: {api_response}')
