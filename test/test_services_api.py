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

from kong_admin_client.api.services_api import ServicesApi


class TestServicesApi(unittest.TestCase):
    """ServicesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServicesApi()

    def tearDown(self) -> None:
        pass

    def test_create_service(self) -> None:
        """Test case for create_service

        Create a new service
        """
        pass

    def test_delete_service(self) -> None:
        """Test case for delete_service

        Delete a service
        """
        pass

    def test_get_service(self) -> None:
        """Test case for get_service

        Fetch a service
        """
        pass

    def test_list_service(self) -> None:
        """Test case for list_service

        List all services
        """
        pass

    def test_update_service(self) -> None:
        """Test case for update_service

        Update a service
        """
        pass

    def test_upsert_service(self) -> None:
        """Test case for upsert_service

        Upsert a service
        """
        pass


if __name__ == '__main__':
    unittest.main()