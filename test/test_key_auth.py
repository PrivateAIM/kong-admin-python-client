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

from kong_admin_client.models.key_auth import KeyAuth

class TestKeyAuth(unittest.TestCase):
    """KeyAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KeyAuth:
        """Test KeyAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KeyAuth`
        """
        model = KeyAuth()
        if include_optional:
            return KeyAuth(
                consumer = kong_admin_client.models.key_auth_consumer.Key_auth_consumer(
                    id = '', ),
                created_at = 56,
                id = '',
                key = '',
                tags = [
                    ''
                    ]
            )
        else:
            return KeyAuth(
        )
        """

    def testKeyAuth(self):
        """Test KeyAuth"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
