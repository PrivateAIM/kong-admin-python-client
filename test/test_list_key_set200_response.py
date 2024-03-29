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

from kong_admin_client.models.list_key_set200_response import ListKeySet200Response

class TestListKeySet200Response(unittest.TestCase):
    """ListKeySet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListKeySet200Response:
        """Test ListKeySet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListKeySet200Response`
        """
        model = ListKeySet200Response()
        if include_optional:
            return ListKeySet200Response(
                id = '4D0DBDA-671C-11ED-BA0B-EF1DCCD3725F',
                name = 'my-key_set',
                created_at = 1422386534,
                updated_at = 1422386534,
                tags = [
                    ''
                    ],
                next = 'http://localhost:8001/key-sets?offset=6378122c-a0a1-438d-a5c6-efabae9fb969'
            )
        else:
            return ListKeySet200Response(
        )
        """

    def testListKeySet200Response(self):
        """Test ListKeySet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
