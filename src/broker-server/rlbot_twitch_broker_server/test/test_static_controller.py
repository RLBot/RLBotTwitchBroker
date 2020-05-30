# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from rlbot_twitch_broker_server.test import BaseTestCase


class TestStaticController(BaseTestCase):
    """StaticController integration test stubs"""

    def test_static_filename_get(self):
        """Test case for static_filename_get

        
        """
        response = self.client.open(
            '/static/{filename}'.format(filename='filename_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
