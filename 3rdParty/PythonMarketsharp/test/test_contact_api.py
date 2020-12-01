# coding: utf-8

"""
    MarketSharp CRM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.contact_api import ContactApi  # noqa: E501
from openapi_client.rest import ApiException


class TestContactApi(unittest.TestCase):
    """ContactApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.contact_api.ContactApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_contact_call_center_search_contacts(self):
        """Test case for contact_call_center_search_contacts

        Search for contacts.  # noqa: E501
        """
        pass

    def test_contact_filter_contacts(self):
        """Test case for contact_filter_contacts

        Filter for contacts  # noqa: E501
        """
        pass

    def test_contact_get(self):
        """Test case for contact_get

        Retrieve a contact - Deprecated  # noqa: E501
        """
        pass

    def test_contact_get_contact_by_id(self):
        """Test case for contact_get_contact_by_id

        Retrieve a contact  # noqa: E501
        """
        pass

    def test_contact_replace_attachment(self):
        """Test case for contact_replace_attachment

        Replace an attachment - Deprecated  # noqa: E501
        """
        pass

    def test_contact_search_contact(self):
        """Test case for contact_search_contact

        Filter for contacts - Deprecated  # noqa: E501
        """
        pass

    def test_contact_search_contacts(self):
        """Test case for contact_search_contacts

        Search for contacts  # noqa: E501
        """
        pass

    def test_contact_upload_attachment(self):
        """Test case for contact_upload_attachment

        Upload an attachment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
