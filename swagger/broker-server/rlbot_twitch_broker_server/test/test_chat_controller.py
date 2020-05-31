# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from rlbot_twitch_broker_server.models.api_response import ApiResponse  # noqa: E501
from rlbot_twitch_broker_server.models.chat_line import ChatLine  # noqa: E501
from rlbot_twitch_broker_server.test import BaseTestCase


class TestChatController(BaseTestCase):
    """ChatController integration test stubs"""

    def test_send_chat(self):
        """Test case for send_chat

        
        """
        body = ChatLine()
        response = self.client.open(
            '/chat',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
