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

from kong_admin_client.models.list_upstream200_response import ListUpstream200Response

class TestListUpstream200Response(unittest.TestCase):
    """ListUpstream200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListUpstream200Response:
        """Test ListUpstream200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListUpstream200Response`
        """
        model = ListUpstream200Response()
        if include_optional:
            return ListUpstream200Response(
                data = [
                    {"algorithm":"round-robin","hash_fallback":"none","hash_on":"none","hash_on_cookie_path":"/","healthchecks":{"active":{"concurrency":10,"healthy":{"http_statuses":[200,302],"interval":0,"successes":0},"http_path":"/","https_verify_certificate":true,"timeout":1,"type":"http","unhealthy":{"http_failures":0,"http_statuses":[429,404,500,501,502,503,504,505],"interval":0,"tcp_failures":0,"timeouts":0}},"passive":{"healthy":{"http_statuses":[200,201,202,203,204,205,206,207,208,226,300,301,302,303,304,305,306,307,308],"successes":0},"type":"http","unhealthy":{"http_failures":0,"http_statuses":[429,500,503],"tcp_failures":0,"timeouts":0}},"threshold":0},"id":"6eed5e9c-5398-4026-9a4c-d48f18a2431e","name":"api.example.internal","slots":10000}
                    ],
                offset = ''
            )
        else:
            return ListUpstream200Response(
        )
        """

    def testListUpstream200Response(self):
        """Test ListUpstream200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
