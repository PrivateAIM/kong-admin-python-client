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

from kong_admin_client.models.create_upstream_request_healthchecks_passive import CreateUpstreamRequestHealthchecksPassive

class TestCreateUpstreamRequestHealthchecksPassive(unittest.TestCase):
    """CreateUpstreamRequestHealthchecksPassive unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateUpstreamRequestHealthchecksPassive:
        """Test CreateUpstreamRequestHealthchecksPassive
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateUpstreamRequestHealthchecksPassive`
        """
        model = CreateUpstreamRequestHealthchecksPassive()
        if include_optional:
            return CreateUpstreamRequestHealthchecksPassive(
                type = 'http',
                healthy = kong_admin_client.models.create_upstream_request_healthchecks_passive_healthy.create_upstream_request_healthchecks_passive_healthy(
                    http_statuses = [200,201,202], 
                    successes = 2, ),
                unhealthy = kong_admin_client.models.create_upstream_request_healthchecks_passive_unhealthy.create_upstream_request_healthchecks_passive_unhealthy(
                    http_statuses = [500,503], 
                    timeouts = 1, 
                    http_failures = 3, 
                    tcp_failures = 1, )
            )
        else:
            return CreateUpstreamRequestHealthchecksPassive(
        )
        """

    def testCreateUpstreamRequestHealthchecksPassive(self):
        """Test CreateUpstreamRequestHealthchecksPassive"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()