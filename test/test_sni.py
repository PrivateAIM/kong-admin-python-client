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

from kong_admin_client.models.sni import SNI

class TestSNI(unittest.TestCase):
    """SNI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SNI:
        """Test SNI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SNI`
        """
        model = SNI()
        if include_optional:
            return SNI(
                certificate = kong_admin_client.models.sni_certificate.SNI_certificate(
                    id = '147f5ef0-1ed6-4711-b77f-489262f8bff7', ),
                created_at = 1422386534,
                id = 'b87eb55d-69a1-41d2-8653-8d706eecefc0',
                name = 'my-sni',
                tags = [
                    'user-level, enterprise'
                    ]
            )
        else:
            return SNI(
        )
        """

    def testSNI(self):
        """Test SNI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
