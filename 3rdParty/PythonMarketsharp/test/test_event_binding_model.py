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
from openapi_client.models.event_binding_model import EventBindingModel  # noqa: E501
from openapi_client.rest import ApiException

class TestEventBindingModel(unittest.TestCase):
    """EventBindingModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EventBindingModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.event_binding_model.EventBindingModel()  # noqa: E501
        if include_optional :
            return EventBindingModel(
                id = 56, 
                type_id = 56, 
                title = '0', 
                description = '0', 
                location = '0', 
                all_day_event = True, 
                start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                category_ids = [
                    56
                    ], 
                last_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                last_update_by = '0', 
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = '0', 
                send_email = True, 
                event_details = '0', 
                additional_details = {
                    'key' : '0'
                    }, 
                event_type = 1
            )
        else :
            return EventBindingModel(
        )

    def testEventBindingModel(self):
        """Test EventBindingModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
