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
from openapi_client.models.production_step_resource_model import ProductionStepResourceModel  # noqa: E501
from openapi_client.rest import ApiException

class TestProductionStepResourceModel(unittest.TestCase):
    """ProductionStepResourceModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProductionStepResourceModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.production_step_resource_model.ProductionStepResourceModel()  # noqa: E501
        if include_optional :
            return ProductionStepResourceModel(
                assigned_to_id = '0', 
                expected_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                actual_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                activity_process_id = '0', 
                notes = '0', 
                is_work_order_enabled = True, 
                is_scheduler_enabled = True, 
                scheduler_id = 56, 
                work_order_print_file_activity_id = '0', 
                process_type_step_id = '0', 
                id = '0', 
                name = '0', 
                expected_end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                actual_end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return ProductionStepResourceModel(
        )

    def testProductionStepResourceModel(self):
        """Test ProductionStepResourceModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
