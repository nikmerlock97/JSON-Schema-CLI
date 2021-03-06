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
from openapi_client.models.product_type_detail_resource_model import ProductTypeDetailResourceModel  # noqa: E501
from openapi_client.rest import ApiException

class TestProductTypeDetailResourceModel(unittest.TestCase):
    """ProductTypeDetailResourceModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProductTypeDetailResourceModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.product_type_detail_resource_model.ProductTypeDetailResourceModel()  # noqa: E501
        if include_optional :
            return ProductTypeDetailResourceModel(
                product_type_id = '0', 
                product_type_name = '0', 
                is_active = True, 
                product_details = [
                    openapi_client.models.product_detail_resource_model.ProductDetailResourceModel(
                        product_detail_id = '0', 
                        product_detail_name = '0', 
                        is_active = True, )
                    ]
            )
        else :
            return ProductTypeDetailResourceModel(
        )

    def testProductTypeDetailResourceModel(self):
        """Test ProductTypeDetailResourceModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
