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

from kong_admin_client.api.debug_api import DebugApi


class TestDebugApi(unittest.TestCase):
    """DebugApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DebugApi()

    def tearDown(self) -> None:
        pass

    def test_get_debug_node_log_level(self) -> None:
        """Test case for get_debug_node_log_level

        Retrieve Node Log Level of A Node
        """
        pass

    def test_put_debug_cluster_control_planes_nodes_log_level_log_level(self) -> None:
        """Test case for put_debug_cluster_control_planes_nodes_log_level_log_level

        Set Node Log Level of All Control Plane Nodes
        """
        pass

    def test_put_debug_cluster_log_level_log_level(self) -> None:
        """Test case for put_debug_cluster_log_level_log_level

        Set Node Log Level of All Nodes
        """
        pass

    def test_put_debug_node_log_level_log_level(self) -> None:
        """Test case for put_debug_node_log_level_log_level

        Set log level of a single node
        """
        pass


if __name__ == '__main__':
    unittest.main()