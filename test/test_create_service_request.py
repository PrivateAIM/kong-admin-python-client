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

from kong_admin_client.models.create_service_request import CreateServiceRequest

class TestCreateServiceRequest(unittest.TestCase):
    """CreateServiceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateServiceRequest:
        """Test CreateServiceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateServiceRequest`
        """
        model = CreateServiceRequest()
        if include_optional:
            return CreateServiceRequest(
                name = 'my-service',
                retries = 5,
                protocol = 'http',
                host = 'example.com',
                port = 80,
                path = '/some_api',
                connect_timeout = 6000,
                write_timeout = 6000,
                read_timeout = 6000,
                tags = [
                    'user-level'
                    ],
                client_certificate = kong_admin_client.models.create_service_request_client_certificate.create_service_request_client_certificate(
                    id = '4e3ad2e4-0bc4-4638-8e34-c84a417ba39b', ),
                tls_verify = True,
                tls_verify_depth = 'respected',
                ca_certificates = [
                    '4e3ad2e4-0bc4-4638-8e34-c84a417ba39b'
                    ],
                enabled = True
            )
        else:
            return CreateServiceRequest(
                protocol = 'http',
                host = 'example.com',
                port = 80,
                enabled = True,
        )
        """

    def testCreateServiceRequest(self):
        """Test CreateServiceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
