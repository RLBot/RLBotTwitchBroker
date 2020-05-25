import random
from threading import Thread

from rlbot_action_client import Configuration, ActionApi, ApiClient, AvailableActions, ActionChoice
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
            available_actions: AvailableActions = action_api.get_actions_currently_available()

            if len(available_actions.available_actions) > 0:
                chosen_action = random.choice(available_actions.available_actions)
                choice = ActionChoice(action=chosen_action)
                result = action_api.choose_action(choice)
                print(result)
