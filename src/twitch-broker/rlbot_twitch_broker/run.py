import json
import random
import re
import string
from dataclasses import dataclass
from pathlib import Path
from threading import Thread
from typing import List, Dict

import itertools
from rlbot_action_client import Configuration, ActionApi, ApiClient, AvailableActions, ActionChoice, BotAction
from rlbot_twitch_broker_server import chat_buffer
from rlbot_twitch_broker_server import client_registry
from rlbot_twitch_broker_server.client_registry import ActionServerData
from rlbot_twitch_broker_server.run import find_usable_port, run_twitch_broker_server
from time import sleep


@dataclass
class ActionAndServerId:
    bot_action: BotAction
    action_server_id: str


@dataclass
class AvailableActionsAndServerId:
    available_actions: AvailableActions
    action_server_id: str


class AvailableActionAggregator:
    def __init__(self):
        self.action_apis: Dict[str, ActionApi] = {}

    def make_action_api(self, client_data: ActionServerData):
        bot_action_api_config = Configuration()
        bot_action_api_config.host = client_data.base_url
        return ActionApi(ApiClient(configuration=bot_action_api_config))

    def fetch_all(self) -> List[AvailableActionsAndServerId]:
        registry = client_registry.CLIENT_REGISTRY
        combined_actions: List[AvailableActionsAndServerId] = []
        for client in list(registry.clients.values()):
            if client.base_url not in self.action_apis:
                self.action_apis[client.get_key()] = self.make_action_api(client)

            action_api = self.action_apis[client.get_key()]

            # For some reason these API calls are slow as molasses
            # After stepping through, it seems like we take about 1 second to form a connection.
            # When calling the same API via Chrome, it's lightning fast.
            # (I did this by visiting http://localhost:8080/action/currentlyAvailable )
            # I tried setting the request header Connection=keep-alive, but that didn't help.
            combined_actions += [AvailableActionsAndServerId(a, client.get_key()) for a in
                                 action_api.get_actions_currently_available()]

        return combined_actions

    def get_action_api(self, action_server_id):
        return self.action_apis[action_server_id]


class NumberedAction:
    def __init__(self, number: int, action: BotAction):
        self.number = number
        self.action = action


@dataclass
class CommandSection:
    header: str
    action_server_id: str
    actions: List[NumberedAction]


@dataclass
class OverlayData:
    menu_id: str
    sections: List[CommandSection]

    def retrieve_choice(self, choice_num: int) -> ActionAndServerId:
        for section in self.sections:
            for action in section.actions:
                if action.number == choice_num:
                    return ActionAndServerId(action.action, section.action_server_id)
        return None


def serialize_for_overlay(o):
    if hasattr(o, 'to_dict'):
        return o.to_dict()
    return o.__dict__


class TwitchBroker:

    def __init__(self, name, overlay_folder: Path):
        self.json_file = overlay_folder / 'twitch_broker_overlay.json'
        self.chat_buffer = chat_buffer.CHAT_BUFFER
        self.menu_id = None

    def create_section(self, act_and_server: AvailableActionsAndServerId, counter: itertools.count):
        return CommandSection(header=act_and_server.available_actions.entity_name,
                              action_server_id=act_and_server.action_server_id,
                              actions=[NumberedAction(next(counter), a) for a in
                                       act_and_server.available_actions.available_actions])

    def generate_menu(self, list: List[AvailableActionsAndServerId], menu_id: str):
        counter = itertools.count(1)
        return OverlayData(menu_id=menu_id, sections=[self.create_section(s, counter) for s in list])

    def write_json_for_overlay(self, overlay_data: OverlayData):
        json_string = json.dumps(overlay_data, default=serialize_for_overlay)
        self.json_file.write_text(json_string)

    def flatten_actions_response(self, act_and_server_list: List[AvailableActionsAndServerId]):
        combined_actions: List[ActionAndServerId] = []
        for act_and_server in act_and_server_list:
            combined_actions += [ActionAndServerId(action, act_and_server.action_server_id) for action in
                                 act_and_server.available_actions.available_actions]
        return combined_actions

    def generate_menu_id(self):
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(2))

    def run_loop_with_stdin(self, desired_port: int):
        port = find_usable_port(desired_port)
        broker_server_thread = Thread(target=run_twitch_broker_server, args=(port,))
        broker_server_thread.setDaemon(True)
        broker_server_thread.start()
        client_registry.CLIENT_REGISTRY = client_registry.ActionServerRegistry()

        aggregator = AvailableActionAggregator()

        while True:
            all_actions = aggregator.fetch_all()
            self.menu_id = self.generate_menu_id()
            overlay_data = self.generate_menu(all_actions, self.menu_id)
            self.write_json_for_overlay(overlay_data)
            combined_actions: List[ActionAndServerId] = self.flatten_actions_response(all_actions)

            if len(combined_actions) > 0:
                action_list_string = "\n".join(
                    [f'{i + 1}. {act.bot_action.description}' for i, act in enumerate(combined_actions)])
                user_input = input("Choose an action:\n" + action_list_string + "\n")
                num = int(user_input)
                chosen_act = combined_actions[num - 1]
                choice = ActionChoice(action=chosen_act.bot_action)
                action_api = aggregator.get_action_api(chosen_act.action_server_id)
                result = action_api.choose_action(choice)
                print(result)
            else:
                sleep(1)

    def run_loop_with_chat_buffer(self, desired_port: int):
        port = find_usable_port(desired_port)
        broker_server_thread = Thread(target=run_twitch_broker_server, args=(port,))
        broker_server_thread.setDaemon(True)
        broker_server_thread.start()
        client_registry.CLIENT_REGISTRY = client_registry.ActionServerRegistry()

        aggregator = AvailableActionAggregator()

        while True:
            all_actions = aggregator.fetch_all()
            if len(all_actions) == 0:
                sleep(0.1)
                continue
            self.menu_id = self.generate_menu_id()
            overlay_data = self.generate_menu(all_actions, self.menu_id)
            self.write_json_for_overlay(overlay_data)

            while not self.chat_buffer.has_chat():
                sleep(0.1)

            while self.chat_buffer.has_chat():
                chat_line = self.chat_buffer.dequeue_chat()
                text = chat_line.message
                match = re.search(self.menu_id + '([0-9]+)', text)
                if match is not None:
                    choice_num = int(match.group(1))
                    choice = overlay_data.retrieve_choice(choice_num)
                    if choice is None:
                        print(f"Invalid choice number {choice_num}")
                        continue
                    action_api = aggregator.get_action_api(choice.action_server_id)
                    result = action_api.choose_action(ActionChoice(action=choice.bot_action))
                    # TODO: lionize chat_line.username
                    print(result)


def run_twitch_broker(desired_port: int, overlay_folder: Path):
    # Open up http://localhost:7307/static/chat_form.html if you want to send test commands without
    # connecting to twitch.
    # Open the overlay (the html file in overlay_folder to see what actions you can enter in chat.
    # You can open it via IntelliJ's html preview, or an OBS scene, both of these start a little mini server
    # so it can access the json successfully. Opening the overlay file directly in a web browser won't work.
    TwitchBroker("Twitch Broker", overlay_folder).run_loop_with_chat_buffer(desired_port)
