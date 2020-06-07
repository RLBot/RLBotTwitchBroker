import random
import string

import itertools
from dataclasses import dataclass
from typing import List

from rlbot.utils.structures.game_data_struct import GameTickPacket, PlayerInfo
from rlbot_action_client.models import BotAction
from twitchbroker.action_and_server_id import AvailableActionsAndServerId, ActionAndServerId


class NumberedAction:
    def __init__(self, number: int, action: BotAction):
        self.number = number
        self.action = action


@dataclass
class CommandAcknowledgement:
    username: str
    description: str
    status: str
    id: str


def create_section(act_and_server: AvailableActionsAndServerId, counter: itertools.count):
    return CommandSection(header=act_and_server.available_actions.entity_name,
                          action_server_id=act_and_server.action_server_id,
                          actions=[NumberedAction(next(counter), a) for a in
                                   act_and_server.available_actions.available_actions])


def generate_menu_id():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(2))


def generate_menu(list: List[AvailableActionsAndServerId], menu_id: str, recent_commands: List[CommandAcknowledgement]):
    counter = itertools.count(1)
    return OverlayData(menu_id=menu_id, sections=[create_section(s, counter) for s in list],
                       recent_commands=recent_commands)


@dataclass
class CommandSection:
    header: str
    action_server_id: str
    actions: List[NumberedAction]


@dataclass
class OverlayData:
    menu_id: str
    sections: List[CommandSection]
    recent_commands: List[CommandAcknowledgement]

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


def get_highlighted_player_name(player: PlayerInfo) -> str:
    color = '#1E90FF' if player.team == 0 else '#FF8C00'
    return f'<b style="color: {color}">{player.name}</b>'


def highlight_player_names(overlay_data: OverlayData, packet: GameTickPacket):
    players = [packet.game_cars[i] for i in range(packet.num_cars)]

    for section in overlay_data.sections:
        for action in section.actions:
            for player in players:
                if player.name in action.action.description:
                    action.action.description = action.action.description.replace(
                        player.name, get_highlighted_player_name(player))
