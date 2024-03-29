# coding: utf-8

"""
    Kerbside Curblr Api

    API for serving kerbside assets. Data is served in CurbLR format https://github.com/sharedstreets/curblr  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: tbd@ford.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.health_controller_api import HealthControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestHealthControllerApi(unittest.TestCase):
    """HealthControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.health_controller_api.HealthControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_message_using_get(self):
        """Test case for message_using_get

        message  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
