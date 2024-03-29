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

from kong_admin_client.api.information_api import InformationApi


class TestInformationApi(unittest.TestCase):
    """InformationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InformationApi()

    def tearDown(self) -> None:
        pass

    def test_get_endpoints(self) -> None:
        """Test case for get_endpoints

        List all endpoints
        """
        pass

    def test_get_schemas_entity(self) -> None:
        """Test case for get_schemas_entity

        Retrieve entity schema
        """
        pass

    def test_get_schemas_filters_filter_name(self) -> None:
        """Test case for get_schemas_filters_filter_name

        Retrieve Proxy-Wasm Filter JSON Schema
        """
        pass

    def test_get_schemas_plugins_plugin_name(self) -> None:
        """Test case for get_schemas_plugins_plugin_name

        Retrieve Plugin Schema
        """
        pass

    def test_get_schemas_vaults_vault_name(self) -> None:
        """Test case for get_schemas_vaults_vault_name

        Retrieve Vault Schema
        """
        pass

    def test_get_status(self) -> None:
        """Test case for get_status

        Health Routes
        """
        pass

    def test_get_timers(self) -> None:
        """Test case for get_timers

        Retrieve Runtime Debugging Info of Kong's Timers
        """
        pass

    def test_head_endpoints(self) -> None:
        """Test case for head_endpoints

        Check endpoint or entity existence
        """
        pass

    def test_options_endpoint(self) -> None:
        """Test case for options_endpoint

        List method by endpoint
        """
        pass

    def test_post_schemas_entity_validate(self) -> None:
        """Test case for post_schemas_entity_validate

        Validate a configuration against a schema
        """
        pass

    def test_post_schemas_plugins_validate(self) -> None:
        """Test case for post_schemas_plugins_validate

        Validate plugin schema
        """
        pass


if __name__ == '__main__':
    unittest.main()
