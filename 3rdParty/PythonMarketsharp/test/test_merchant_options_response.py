# coding: utf-8

"""
    MarketSharp CRM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.merchant_options_response import MerchantOptionsResponse  # noqa: E501
from openapi_client.rest import ApiException

class TestMerchantOptionsResponse(unittest.TestCase):
    """MerchantOptionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MerchantOptionsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.merchant_options_response.MerchantOptionsResponse()  # noqa: E501
        if include_optional :
            return MerchantOptionsResponse(
                accepts_credit_card = True, 
                accepts_ach = True, 
                credit_card_issuers = [
                    '0'
                    ]
            )
        else :
            return MerchantOptionsResponse(
        )

    def testMerchantOptionsResponse(self):
        """Test MerchantOptionsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
