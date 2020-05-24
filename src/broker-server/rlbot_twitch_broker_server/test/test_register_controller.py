# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from rlbot_twitch_broker_server.models.action_server_registration import ActionServerRegistration  # noqa: E501
from rlbot_twitch_broker_server.models.api_response import ApiResponse  # noqa: E501
from rlbot_twitch_broker_server.test import BaseTestCase


class TestRegisterController(BaseTestCase):
    """RegisterController integration test stubs"""

    def test_register_action_server(self):
        """Test case for register_action_server

        
        """
        body = ActionServerRegistration()
        response = self.client.open(
            '/register/actionServer',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
