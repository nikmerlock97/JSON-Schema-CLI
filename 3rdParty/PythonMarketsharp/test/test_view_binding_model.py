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
from openapi_client.models.view_binding_model import ViewBindingModel  # noqa: E501
from openapi_client.rest import ApiException

class TestViewBindingModel(unittest.TestCase):
    """ViewBindingModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ViewBindingModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.view_binding_model.ViewBindingModel()  # noqa: E501
        if include_optional :
            return ViewBindingModel(
                field_list = [
                    openapi_client.models.field.Field(
                        order = 56, 
                        field_id = '0', 
                        field_def_id = '0', )
                    ], 
                company_id = '0', 
                view_id = '0', 
                view_name = '0', 
                list_view_type = '0', 
                is_public = True
            )
        else :
            return ViewBindingModel(
        )

    def testViewBindingModel(self):
        """Test ViewBindingModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()