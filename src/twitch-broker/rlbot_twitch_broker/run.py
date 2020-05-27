from dataclasses import dataclass
from threading import Thread
from typing import List, Dict

from rlbot_twitch_broker_server.client_registry import ClientData
from rlbot.agents.base_script import BaseScript
from rlbot_action_client import Configuration, ActionApi, ApiClient, AvailableActions, ActionChoice, BotAction
from rlbot_twitch_broker_server import client_registry
from rlbot_twitch_broker_server.run import find_usable_port, run_twitch_broker_server
from time import sleep


@dataclass
class ActionAndApi:
    bot_action: BotAction
    action_api: ActionApi


class AvailableActionAggregator:
    def __init__(self):
        self.action_apis: Dict[str, ActionApi] = {}

    def make_action_api(self, client_data: ClientData):
        bot_action_api_config = Configuration()
        bot_action_api_config.host = client_data.base_url
        return ActionApi(ApiClient(configuration=bot_action_api_config))

    def fetch_all_and_aggregate(self):
        registry = client_registry.CLIENT_REGISTRY
        combined_actions: List[ActionAndApi] = []
        for client in list(registry.clients.values()):
            if client.base_url not in self.action_apis:
                self.action_apis[client.base_url] = self.make_action_api(client)

            action_api = self.action_apis[client.base_url]

            # For some reason these API calls are slow as molasses
            # After stepping through, it seems like we take about 1 second to form a connection.
            # When calling the same API via Chrome, it's lightning fast.
            # (I did this by visiting http://localhost:8080/action/currentlyAvailable )
            # I tried setting the request header Connection=keep-alive, but that didn't help.
            available_actions_list: List[AvailableActions] = action_api.get_actions_currently_available()
            for available_actions in available_actions_list:
                combined_actions += [ActionAndApi(action, action_api) for action in available_actions.available_actions]

        return combined_actions


class TwitchBroker(BaseScript):

    def run_loop_with_stdin(self, desired_port: int):
        port = find_usable_port(desired_port)
        broker_server_thread = Thread(target=run_twitch_broker_server, args=(port,))
        broker_server_thread.setDaemon(True)
        broker_server_thread.start()
        client_registry.CLIENT_REGISTRY = client_registry.ClientRegistry()

        aggregator = AvailableActionAggregator()

        while True:
            combined_actions: List[ActionAndApi] = aggregator.fetch_all_and_aggregate()

            if len(combined_actions) > 0:
                action_list_string = "\n".join(
                    [f'{i + 1}. {act.bot_action.description}' for i, act in enumerate(combined_actions)])
                user_input = input("Choose an action:\n" + action_list_string + "\n")
                num = int(user_input)
                chosen_act = combined_actions[num - 1]
                choice = ActionChoice(action=chosen_act.bot_action)
                result = chosen_act.action_api.choose_action(choice)
                print(result)
            else:
                sleep(1)


def run_twitch_broker(desired_port: int):
    TwitchBroker("Twitch Broker").run_loop_with_stdin(desired_port)
