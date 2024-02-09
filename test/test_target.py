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

from kong_admin_client.models.target import Target

class TestTarget(unittest.TestCase):
    """Target unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Target:
        """Test Target
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Target`
        """
        model = Target()
        if include_optional:
            return Target(
                created_at = 1422386534,
                id = '173a6cee-90d1-40a7-89cf-0329eca780a6',
                tags = [
                    ''
                    ],
                target = '',
                upstream = kong_admin_client.models.target_upstream.Target_upstream(
                    id = 'bdab0e47-4e37-4f0b-8fd0-87d95cc4addc', ),
                weight = 100
            )
        else:
            return Target(
        )
        """

    def testTarget(self):
        """Test Target"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()