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
from openapi_client.models.pay_simple_get_reconciliation_binding_model import PaySimpleGetReconciliationBindingModel  # noqa: E501
from openapi_client.rest import ApiException

class TestPaySimpleGetReconciliationBindingModel(unittest.TestCase):
    """PaySimpleGetReconciliationBindingModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaySimpleGetReconciliationBindingModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.pay_simple_get_reconciliation_binding_model.PaySimpleGetReconciliationBindingModel()  # noqa: E501
        if include_optional :
            return PaySimpleGetReconciliationBindingModel(
                payment_reconciliation_statuses = [
                    56
                    ], 
                from_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return PaySimpleGetReconciliationBindingModel(
        )

    def testPaySimpleGetReconciliationBindingModel(self):
        """Test PaySimpleGetReconciliationBindingModel"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
