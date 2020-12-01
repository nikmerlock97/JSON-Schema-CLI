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
from openapi_client.models.estimate_line_item_resource_model import EstimateLineItemResourceModel  # noqa: E501
from openapi_client.rest import ApiException

class TestEstimateLineItemResourceModel(unittest.TestCase):
    """EstimateLineItemResourceModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EstimateLineItemResourceModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.estimate_line_item_resource_model.EstimateLineItemResourceModel()  # noqa: E501
        if include_optional :
            return EstimateLineItemResourceModel(
                id = '0', 
                sku = '0', 
                position = 56, 
                estimate_id = 56, 
                quantity = 56, 
                unit_of_measure = 56, 
                retail_price = 1.337, 
                line_item_discount_amount = 1.337, 
                line_item_discount_percent = 1.337, 
                cost = 1.337, 
                notes = '0'
            )
        else :
            return EstimateLineItemResourceModel(
        )

    def testEstimateLineItemResourceModel(self):
        """Test EstimateLineItemResourceModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
