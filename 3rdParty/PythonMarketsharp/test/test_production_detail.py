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
from openapi_client.models.production_detail import ProductionDetail  # noqa: E501
from openapi_client.rest import ApiException

class TestProductionDetail(unittest.TestCase):
    """ProductionDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProductionDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.production_detail.ProductionDetail()  # noqa: E501
        if include_optional :
            return ProductionDetail(
                coy_oid = '0', 
                contract_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                contract_status = '0', 
                contract_amount = 1.337, 
                contract_balance_due = 1.337, 
                contact_type = '0', 
                product_id = '0', 
                product_name = '0', 
                contact = openapi_client.models.contact_view_resource_model.ContactViewResourceModel(
                    oid = '0', 
                    age_group = '0', 
                    age_of_home = '0', 
                    company = '0', 
                    do_not_mail = True, 
                    email = '0', 
                    email2 = '0', 
                    email3 = '0', 
                    last_name = '0', 
                    first_name = '0', 
                    home_value = '0', 
                    income_level = '0', 
                    length_of_residence = '0', 
                    marital_status = '0', 
                    created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    contact_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_updated_by = '0', 
                    record_source = '0', 
                    style_of_home = '0', 
                    contact_tagged = True, 
                    contact_title = '0', 
                    contact_website = '0', 
                    contact_website2 = '0', 
                    contact_website3 = '0', 
                    year_home_built = '0', ), 
                address = openapi_client.models.address_view_resource_model.AddressViewResourceModel(
                    bar_code = '0', 
                    carrier_route = '0', 
                    cass = '0', 
                    city = '0', 
                    county = '0', 
                    dpbc = '0', 
                    latitude = '0', 
                    longitude = '0', 
                    address_line1 = '0', 
                    address_line2 = '0', 
                    state = '0', 
                    zip = '0', 
                    zip4 = '0', 
                    country = '0', ), 
                job = openapi_client.models.job_view_resource_model.JobViewResourceModel(
                    job_address1 = '0', 
                    job_address2 = '0', 
                    job_city = '0', 
                    job_completed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    job_name = '0', 
                    job_notes = '0', 
                    job_number = '0', 
                    job_sale_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    job_status = '0', 
                    job_type = '0', 
                    job_zip = '0', ), 
                job_product = openapi_client.models.job_product_view_resource_model.JobProductViewResourceModel(
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
                    product_work_crew = '0', ), 
                custom_field_values = [
                    openapi_client.models.key_value_resource_model.KeyValueResourceModel(
                        id = '0', 
                        name = '0', )
                    ]
            )
        else :
            return ProductionDetail(
        )

    def testProductionDetail(self):
        """Test ProductionDetail"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()