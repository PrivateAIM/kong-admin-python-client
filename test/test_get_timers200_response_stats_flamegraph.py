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

from kong_admin_client.models.get_timers200_response_stats_flamegraph import GetTimers200ResponseStatsFlamegraph

class TestGetTimers200ResponseStatsFlamegraph(unittest.TestCase):
    """GetTimers200ResponseStatsFlamegraph unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTimers200ResponseStatsFlamegraph:
        """Test GetTimers200ResponseStatsFlamegraph
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTimers200ResponseStatsFlamegraph`
        """
        model = GetTimers200ResponseStatsFlamegraph()
        if include_optional:
            return GetTimers200ResponseStatsFlamegraph(
                pending = '@./kong/init.lua:706:init_worker();@./kong/runloop/handler.lua:1086:before() 0
',
                running = '@./kong/init.lua:706:init_worker();@./kong/runloop/handler.lua:1086:before() 0
',
                elapsed_time = '@./kong/init.lua:706:init_worker();@./kong/runloop/handler.lua:1086:before() 17
'
            )
        else:
            return GetTimers200ResponseStatsFlamegraph(
        )
        """

    def testGetTimers200ResponseStatsFlamegraph(self):
        """Test GetTimers200ResponseStatsFlamegraph"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
