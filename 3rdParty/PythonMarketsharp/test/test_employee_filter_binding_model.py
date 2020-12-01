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
from openapi_client.models.employee_filter_binding_model import EmployeeFilterBindingModel  # noqa: E501
from openapi_client.rest import ApiException

class TestEmployeeFilterBindingModel(unittest.TestCase):
    """EmployeeFilterBindingModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EmployeeFilterBindingModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.employee_filter_binding_model.EmployeeFilterBindingModel()  # noqa: E501
        if include_optional :
            return EmployeeFilterBindingModel(
                has_phone = True, 
                has_email = True, 
                include_inactive = True, 
                employee_list_types = [
                    '0'
                    ], 
                include_employees = [
                    '0'
                    ]
            )
        else :
            return EmployeeFilterBindingModel(
        )

    def testEmployeeFilterBindingModel(self):
        """Test EmployeeFilterBindingModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()