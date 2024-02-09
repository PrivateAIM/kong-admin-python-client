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

from kong_admin_client.api.certificates_api import CertificatesApi


class TestCertificatesApi(unittest.TestCase):
    """CertificatesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CertificatesApi()

    def tearDown(self) -> None:
        pass

    def test_create_certificate(self) -> None:
        """Test case for create_certificate

        Create a new Certificate
        """
        pass

    def test_delete_certificate(self) -> None:
        """Test case for delete_certificate

        Delete a Certificate
        """
        pass

    def test_get_certificate(self) -> None:
        """Test case for get_certificate

        Fetch a Certificate
        """
        pass

    def test_list_certificate(self) -> None:
        """Test case for list_certificate

        List all certificates
        """
        pass

    def test_update_certificate(self) -> None:
        """Test case for update_certificate

        Update a Certificate
        """
        pass

    def test_update_certificate_put(self) -> None:
        """Test case for update_certificate_put

        Update a Certificate
        """
        pass


if __name__ == '__main__':
    unittest.main()