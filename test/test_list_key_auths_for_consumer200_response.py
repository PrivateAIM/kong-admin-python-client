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

from kong_admin_client.models.list_key_auths_for_consumer200_response import ListKeyAuthsForConsumer200Response

class TestListKeyAuthsForConsumer200Response(unittest.TestCase):
    """ListKeyAuthsForConsumer200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListKeyAuthsForConsumer200Response:
        """Test ListKeyAuthsForConsumer200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListKeyAuthsForConsumer200Response`
        """
        model = ListKeyAuthsForConsumer200Response()
        if include_optional:
            return ListKeyAuthsForConsumer200Response(
                data = [
                    kong_admin_client.models.key_auth.Key-auth(
                        consumer = kong_admin_client.models.key_auth_consumer.Key_auth_consumer(
                            id = '', ), 
                        created_at = 56, 
                        id = '', 
                        key = '', 
                        tags = [
                            ''
                            ], )
                    ],
                offset = ''
            )
        else:
            return ListKeyAuthsForConsumer200Response(
        )
        """

    def testListKeyAuthsForConsumer200Response(self):
        """Test ListKeyAuthsForConsumer200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
