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

from kong_admin_client.models.upstream_healthchecks_active_unhealthy import UpstreamHealthchecksActiveUnhealthy

class TestUpstreamHealthchecksActiveUnhealthy(unittest.TestCase):
    """UpstreamHealthchecksActiveUnhealthy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpstreamHealthchecksActiveUnhealthy:
        """Test UpstreamHealthchecksActiveUnhealthy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpstreamHealthchecksActiveUnhealthy`
        """
        model = UpstreamHealthchecksActiveUnhealthy()
        if include_optional:
            return UpstreamHealthchecksActiveUnhealthy(
                http_failures = 56,
                http_statuses = [
                    56
                    ],
                interval = 1.337,
                tcp_failures = 56,
                timeouts = 56
            )
        else:
            return UpstreamHealthchecksActiveUnhealthy(
        )
        """

    def testUpstreamHealthchecksActiveUnhealthy(self):
        """Test UpstreamHealthchecksActiveUnhealthy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
