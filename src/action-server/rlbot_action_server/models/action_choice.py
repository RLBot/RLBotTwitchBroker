# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rlbot_action_server.models.base_model_ import Model
from rlbot_action_server.models.bot_action import BotAction  # noqa: F401,E501
from rlbot_action_server import util


class ActionChoice(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, action: BotAction=None):  # noqa: E501
        """ActionChoice - a model defined in Swagger

        :param action: The action of this ActionChoice.  # noqa: E501
        :type action: BotAction
        """
        self.swagger_types = {
            'action': BotAction
        }

        self.attribute_map = {
            'action': 'action'
        }
        self._action = action

    @classmethod
    def from_dict(cls, dikt) -> 'ActionChoice':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ActionChoice of this ActionChoice.  # noqa: E501
        :rtype: ActionChoice
        """
        return util.deserialize_model(dikt, cls)

    @property
    def action(self) -> BotAction:
        """Gets the action of this ActionChoice.


        :return: The action of this ActionChoice.
        :rtype: BotAction
        """
        return self._action

    @action.setter
    def action(self, action: BotAction):
        """Sets the action of this ActionChoice.


        :param action: The action of this ActionChoice.
        :type action: BotAction
        """

        self._action = action
