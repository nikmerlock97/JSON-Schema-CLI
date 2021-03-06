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
from openapi_client.models.proposed_activities_request_binding_model import ProposedActivitiesRequestBindingModel  # noqa: E501
from openapi_client.rest import ApiException

class TestProposedActivitiesRequestBindingModel(unittest.TestCase):
    """ProposedActivitiesRequestBindingModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProposedActivitiesRequestBindingModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.proposed_activities_request_binding_model.ProposedActivitiesRequestBindingModel()  # noqa: E501
        if include_optional :
            return ProposedActivitiesRequestBindingModel(
                request_source_type = 0, 
                request_source_id = '0'
            )
        else :
            return ProposedActivitiesRequestBindingModel(
        )

    def testProposedActivitiesRequestBindingModel(self):
        """Test ProposedActivitiesRequestBindingModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
