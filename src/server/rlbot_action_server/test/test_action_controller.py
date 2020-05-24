# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from rlbot_action_server.models.action_choice import ActionChoice  # noqa: E501
from rlbot_action_server.models.api_response import ApiResponse  # noqa: E501
from rlbot_action_server.models.available_actions import AvailableActions  # noqa: E501
from rlbot_action_server.test import BaseTestCase


class TestActionController(BaseTestCase):
    """ActionController integration test stubs"""

    def test_choose_action(self):
        """Test case for choose_action

        
        """
        body = ActionChoice()
        response = self.client.open(
            '/action/choose',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_actions_currently_available(self):
        """Test case for get_actions_currently_available

        
        """
        response = self.client.open(
            '/action/currentlyAvailable',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
