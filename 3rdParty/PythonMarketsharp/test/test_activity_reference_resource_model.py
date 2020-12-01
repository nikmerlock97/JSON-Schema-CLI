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
from openapi_client.models.activity_reference_resource_model import ActivityReferenceResourceModel  # noqa: E501
from openapi_client.rest import ApiException

class TestActivityReferenceResourceModel(unittest.TestCase):
    """ActivityReferenceResourceModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ActivityReferenceResourceModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.activity_reference_resource_model.ActivityReferenceResourceModel()  # noqa: E501
        if include_optional :
            return ActivityReferenceResourceModel(
                id = 56, 
                company_id = '0', 
                name = '0', 
                inquiry_required = True, 
                appointment_required = True, 
                position = 56, 
                is_active = True, 
                call_out_script_template_id = 56
            )
        else :
            return ActivityReferenceResourceModel(
        )

    def testActivityReferenceResourceModel(self):
        """Test ActivityReferenceResourceModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
