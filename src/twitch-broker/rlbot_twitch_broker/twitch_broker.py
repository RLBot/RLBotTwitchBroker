import json
import re
from pathlib import Path
from threading import Thread
from typing import List, Dict

from dataclasses import dataclass
from rlbot_action_client import Configuration, ActionApi, ApiClient, ActionChoice
from rlbot_twitch_broker.action_and_server_id import AvailableActionsAndServerId
from rlbot_twitch_broker.overlay_data import OverlayData, serialize_for_overlay, generate_menu_id, generate_menu
from rlbot_twitch_broker.twitch_chat_bot import TwitchChatBot
from rlbot_twitch_broker_client.models.chat_line import ChatLine
from rlbot_twitch_broker_server import chat_buffer
from rlbot_twitch_broker_server import client_registry
from rlbot_twitch_broker_server.client_registry import ActionServerData
from rlbot_twitch_broker_server.run import find_usable_port, run_twitch_broker_server
from time import sleep


class AvailableActionAggregator:
    def __init__(self):
        self.action_apis: Dict[str, ActionApi] = {}

    def make_action_api(self, client_data: ActionServerData):
        bot_action_api_config = Configuration()
        bot_action_api_config.host = client_data.base_url
        return ActionApi(ApiClient(configuration=bot_action_api_config))

    def fetch_all(self) -> List[AvailableActionsAndServerId]:
        registry = client_registry.CLIENT_REGISTRY
        request_threads = []
        for client in list(registry.clients.values()):
            if client.base_url not in self.action_apis:
                self.action_apis[client.get_key()] = self.make_action_api(client)

            action_api = self.action_apis[client.get_key()]

            # For some reason these API calls are slow as molasses
            # After stepping through, it seems like we take about 1 second to form a connection.
            # When calling the same API via Chrome, it's lightning fast.
            # (I did this by visiting http://127.0.0.1:8080/action/currentlyAvailable )
            # I tried setting the request header Connection=keep-alive, but that didn't help.
            request_threads.append((client.get_key(), action_api.get_actions_currently_available(
                async_req=True, _request_timeout=0.2)))

        combined_actions: List[AvailableActionsAndServerId] = []
        for (client_key, req) in request_threads:
            avail_actions_list = req.get()
            combined_actions += [AvailableActionsAndServerId(a, client_key) for a in avail_actions_list]

        return combined_actions

    def get_action_api(self, action_server_id):
        return self.action_apis[action_server_id]

@dataclass
class TwitchAuth:
    username: str
    oauth: str
    channel: str


class TwitchChatAdapter(TwitchChatBot):
    def __init__(self, twitch_auth: TwitchAuth):
        super().__init__(twitch_auth.username, twitch_auth.oauth, twitch_auth.channel)

    def on_message(self, sender, message):
        chat_buffer.CHAT_BUFFER.enqueue_chat(ChatLine(username=sender, message=message))


class TwitchBroker:

    def __init__(self, overlay_folder: Path, twitch_auth: TwitchAuth):
        self.json_file = overlay_folder / 'twitch_broker_overlay.json'
        self.chat_buffer = chat_buffer.CHAT_BUFFER
        self.menu_id = None
        self.twitch_chat_adapter = None
        if twitch_auth:
            self.twitch_chat_adapter = TwitchChatAdapter(twitch_auth)

    def write_json_for_overlay(self, overlay_data: OverlayData):
        json_string = json.dumps(overlay_data, default=serialize_for_overlay)
        self.json_file.write_text(json_string)

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
            self.menu_id = generate_menu_id()
            overlay_data = generate_menu(all_actions, self.menu_id)
            self.write_json_for_overlay(overlay_data)

            while not self.chat_buffer.has_chat():
                self.twitch_chat_adapter.scan()
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


def run_twitch_broker(desired_port: int, overlay_folder: Path, twitch_auth: TwitchAuth):
    # Open up http://127.0.0.1:7307/static/chat_form.html if you want to send test commands without
    # connecting to twitch.
    # Open the overlay (the html file in overlay_folder to see what actions you can enter in chat.
    # You can open it via IntelliJ's html preview, or an OBS scene, both of these start a little mini server
    # so it can access the json successfully. Opening the overlay file directly in a web browser won't work.
    TwitchBroker(overlay_folder, twitch_auth).run_loop_with_chat_buffer(desired_port)
