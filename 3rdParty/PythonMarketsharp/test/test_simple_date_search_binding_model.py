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
from openapi_client.models.simple_date_search_binding_model import SimpleDateSearchBindingModel  # noqa: E501
from openapi_client.rest import ApiException

class TestSimpleDateSearchBindingModel(unittest.TestCase):
    """SimpleDateSearchBindingModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SimpleDateSearchBindingModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.simple_date_search_binding_model.SimpleDateSearchBindingModel()  # noqa: E501
        if include_optional :
            return SimpleDateSearchBindingModel(
                from_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                number_of_records = 56
            )
        else :
            return SimpleDateSearchBindingModel(
        )

    def testSimpleDateSearchBindingModel(self):
        """Test SimpleDateSearchBindingModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
