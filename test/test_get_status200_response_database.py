# coding: utf-8

"""
    Kong Admin API

    OpenAPI 3.0 spec for Kong Gateway's open source Admin API.  You can know more about Kong Gateway at [docs.konghq.com](https://docs.konghq.com) .Give Kong a star at [Kong/kong](https://github.com/kong/kong) repository.

    The version of the OpenAPI document: 3.5.0
    Contact: docs@konghq.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from kong_admin_client.models.get_status200_response_database import GetStatus200ResponseDatabase

class TestGetStatus200ResponseDatabase(unittest.TestCase):
    """GetStatus200ResponseDatabase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetStatus200ResponseDatabase:
        """Test GetStatus200ResponseDatabase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetStatus200ResponseDatabase`
        """
        model = GetStatus200ResponseDatabase()
        if include_optional:
            return GetStatus200ResponseDatabase(
                reachable = True
            )
        else:
            return GetStatus200ResponseDatabase(
        )
        """

    def testGetStatus200ResponseDatabase(self):
        """Test GetStatus200ResponseDatabase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
