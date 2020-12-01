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
from openapi_client.models.job_product_view_resource_model import JobProductViewResourceModel  # noqa: E501
from openapi_client.rest import ApiException

class TestJobProductViewResourceModel(unittest.TestCase):
    """JobProductViewResourceModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobProductViewResourceModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.job_product_view_resource_model.JobProductViewResourceModel()  # noqa: E501
        if include_optional :
            return JobProductViewResourceModel(
                company_id = '0', 
                job_product_id = '0', 
                product_notes = '0', 
                product_production_notes = '0', 
                product_price = 1.337, 
                product_price_adjustment = 1.337, 
                product_completed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                product_sale_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                product_salesperson1 = '0', 
                product_salesperson2 = '0', 
                product_service_expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                product_service_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                product_warranty_expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                product_warranty_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                product_project_manager = '0', 
                product_process_type_id = '0', 
                detail_task_list = [
                    openapi_client.models.base_production_step_model.BaseProductionStepModel(
                        id = '0', 
                        name = '0', 
                        expected_end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        actual_end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
                product_workers = [
                    openapi_client.models.key_value_resource_model.KeyValueResourceModel(
                        id = '0', 
                        name = '0', )
                    ], 
                has_custom_steps = True, 
                product_work_crew = '0'
            )
        else :
            return JobProductViewResourceModel(
        )

    def testJobProductViewResourceModel(self):
        """Test JobProductViewResourceModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()