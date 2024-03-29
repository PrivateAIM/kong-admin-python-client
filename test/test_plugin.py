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

from kong_admin_client.models.plugin import Plugin

class TestPlugin(unittest.TestCase):
    """Plugin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Plugin:
        """Test Plugin
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Plugin`
        """
        model = Plugin()
        if include_optional:
            return Plugin(
                config = None,
                consumer = kong_admin_client.models.plugin_consumer.Plugin_consumer(
                    id = '', ),
                created_at = 56,
                enabled = True,
                id = '',
                instance_name = '',
                name = '',
                ordering = None,
                protocols = [
                    ''
                    ],
                route = kong_admin_client.models.plugin_route.Plugin_route(
                    id = '', ),
                service = kong_admin_client.models.plugin_service.Plugin_service(
                    id = '', ),
                tags = [
                    ''
                    ],
                updated_at = 56
            )
        else:
            return Plugin(
        )
        """

    def testPlugin(self):
        """Test Plugin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
