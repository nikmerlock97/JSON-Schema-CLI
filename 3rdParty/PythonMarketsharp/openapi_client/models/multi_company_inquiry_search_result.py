# coding: utf-8

"""
    MarketSharp CRM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class MultiCompanyInquirySearchResult(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'ms_company': 'str',
        'coy_oid': 'str',
        'contact_type': 'str',
        'oid': 'str',
        'last_name': 'str',
        'first_name': 'str',
        'company': 'str',
        'primary_email': 'str',
        'secondary_email': 'str',
        'teritiary_email': 'str',
        'inquiry_date_time': 'str',
        'inquiry_address_line_one': 'str',
        'inquiry_address_line_two': 'str',
        'inquiry_city': 'str',
        'inquiry_state': 'str',
        'inquiry_zip': 'str',
        'primary_lead_source': 'str',
        'secondary_lead_source': 'str',
        'phone_numbers': 'list[str]',
        'product_interest': 'str'
    }

    attribute_map = {
        'ms_company': 'msCompany',
        'coy_oid': 'coyOid',
        'contact_type': 'contactType',
        'oid': 'oid',
        'last_name': 'lastName',
        'first_name': 'firstName',
        'company': 'company',
        'primary_email': 'primaryEmail',
        'secondary_email': 'secondaryEmail',
        'teritiary_email': 'teritiaryEmail',
        'inquiry_date_time': 'inquiryDateTime',
        'inquiry_address_line_one': 'inquiryAddressLineOne',
        'inquiry_address_line_two': 'inquiryAddressLineTwo',
        'inquiry_city': 'inquiryCity',
        'inquiry_state': 'inquiryState',
        'inquiry_zip': 'inquiryZip',
        'primary_lead_source': 'primaryLeadSource',
        'secondary_lead_source': 'secondaryLeadSource',
        'phone_numbers': 'phoneNumbers',
        'product_interest': 'productInterest'
    }

    def __init__(self, ms_company=None, coy_oid=None, contact_type=None, oid=None, last_name=None, first_name=None, company=None, primary_email=None, secondary_email=None, teritiary_email=None, inquiry_date_time=None, inquiry_address_line_one=None, inquiry_address_line_two=None, inquiry_city=None, inquiry_state=None, inquiry_zip=None, primary_lead_source=None, secondary_lead_source=None, phone_numbers=None, product_interest=None, local_vars_configuration=None):  # noqa: E501
        """MultiCompanyInquirySearchResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ms_company = None
        self._coy_oid = None
        self._contact_type = None
        self._oid = None
        self._last_name = None
        self._first_name = None
        self._company = None
        self._primary_email = None
        self._secondary_email = None
        self._teritiary_email = None
        self._inquiry_date_time = None
        self._inquiry_address_line_one = None
        self._inquiry_address_line_two = None
        self._inquiry_city = None
        self._inquiry_state = None
        self._inquiry_zip = None
        self._primary_lead_source = None
        self._secondary_lead_source = None
        self._phone_numbers = None
        self._product_interest = None
        self.discriminator = None

        if ms_company is not None:
            self.ms_company = ms_company
        if coy_oid is not None:
            self.coy_oid = coy_oid
        if contact_type is not None:
            self.contact_type = contact_type
        if oid is not None:
            self.oid = oid
        if last_name is not None:
            self.last_name = last_name
        if first_name is not None:
            self.first_name = first_name
        if company is not None:
            self.company = company
        if primary_email is not None:
            self.primary_email = primary_email
        if secondary_email is not None:
            self.secondary_email = secondary_email
        if teritiary_email is not None:
            self.teritiary_email = teritiary_email
        if inquiry_date_time is not None:
            self.inquiry_date_time = inquiry_date_time
        if inquiry_address_line_one is not None:
            self.inquiry_address_line_one = inquiry_address_line_one
        if inquiry_address_line_two is not None:
            self.inquiry_address_line_two = inquiry_address_line_two
        if inquiry_city is not None:
            self.inquiry_city = inquiry_city
        if inquiry_state is not None:
            self.inquiry_state = inquiry_state
        if inquiry_zip is not None:
            self.inquiry_zip = inquiry_zip
        if primary_lead_source is not None:
            self.primary_lead_source = primary_lead_source
        if secondary_lead_source is not None:
            self.secondary_lead_source = secondary_lead_source
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if product_interest is not None:
            self.product_interest = product_interest

    @property
    def ms_company(self):
        """Gets the ms_company of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The ms_company of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._ms_company

    @ms_company.setter
    def ms_company(self, ms_company):
        """Sets the ms_company of this MultiCompanyInquirySearchResult.


        :param ms_company: The ms_company of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._ms_company = ms_company

    @property
    def coy_oid(self):
        """Gets the coy_oid of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The coy_oid of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._coy_oid

    @coy_oid.setter
    def coy_oid(self, coy_oid):
        """Sets the coy_oid of this MultiCompanyInquirySearchResult.


        :param coy_oid: The coy_oid of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._coy_oid = coy_oid

    @property
    def contact_type(self):
        """Gets the contact_type of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The contact_type of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._contact_type

    @contact_type.setter
    def contact_type(self, contact_type):
        """Sets the contact_type of this MultiCompanyInquirySearchResult.


        :param contact_type: The contact_type of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._contact_type = contact_type

    @property
    def oid(self):
        """Gets the oid of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The oid of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this MultiCompanyInquirySearchResult.


        :param oid: The oid of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._oid = oid

    @property
    def last_name(self):
        """Gets the last_name of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The last_name of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this MultiCompanyInquirySearchResult.


        :param last_name: The last_name of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def first_name(self):
        """Gets the first_name of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The first_name of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this MultiCompanyInquirySearchResult.


        :param first_name: The first_name of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def company(self):
        """Gets the company of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The company of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this MultiCompanyInquirySearchResult.


        :param company: The company of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def primary_email(self):
        """Gets the primary_email of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The primary_email of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._primary_email

    @primary_email.setter
    def primary_email(self, primary_email):
        """Sets the primary_email of this MultiCompanyInquirySearchResult.


        :param primary_email: The primary_email of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._primary_email = primary_email

    @property
    def secondary_email(self):
        """Gets the secondary_email of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The secondary_email of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._secondary_email

    @secondary_email.setter
    def secondary_email(self, secondary_email):
        """Sets the secondary_email of this MultiCompanyInquirySearchResult.


        :param secondary_email: The secondary_email of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._secondary_email = secondary_email

    @property
    def teritiary_email(self):
        """Gets the teritiary_email of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The teritiary_email of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._teritiary_email

    @teritiary_email.setter
    def teritiary_email(self, teritiary_email):
        """Sets the teritiary_email of this MultiCompanyInquirySearchResult.


        :param teritiary_email: The teritiary_email of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._teritiary_email = teritiary_email

    @property
    def inquiry_date_time(self):
        """Gets the inquiry_date_time of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The inquiry_date_time of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._inquiry_date_time

    @inquiry_date_time.setter
    def inquiry_date_time(self, inquiry_date_time):
        """Sets the inquiry_date_time of this MultiCompanyInquirySearchResult.


        :param inquiry_date_time: The inquiry_date_time of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._inquiry_date_time = inquiry_date_time

    @property
    def inquiry_address_line_one(self):
        """Gets the inquiry_address_line_one of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The inquiry_address_line_one of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._inquiry_address_line_one

    @inquiry_address_line_one.setter
    def inquiry_address_line_one(self, inquiry_address_line_one):
        """Sets the inquiry_address_line_one of this MultiCompanyInquirySearchResult.


        :param inquiry_address_line_one: The inquiry_address_line_one of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._inquiry_address_line_one = inquiry_address_line_one

    @property
    def inquiry_address_line_two(self):
        """Gets the inquiry_address_line_two of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The inquiry_address_line_two of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._inquiry_address_line_two

    @inquiry_address_line_two.setter
    def inquiry_address_line_two(self, inquiry_address_line_two):
        """Sets the inquiry_address_line_two of this MultiCompanyInquirySearchResult.


        :param inquiry_address_line_two: The inquiry_address_line_two of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._inquiry_address_line_two = inquiry_address_line_two

    @property
    def inquiry_city(self):
        """Gets the inquiry_city of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The inquiry_city of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._inquiry_city

    @inquiry_city.setter
    def inquiry_city(self, inquiry_city):
        """Sets the inquiry_city of this MultiCompanyInquirySearchResult.


        :param inquiry_city: The inquiry_city of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._inquiry_city = inquiry_city

    @property
    def inquiry_state(self):
        """Gets the inquiry_state of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The inquiry_state of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._inquiry_state

    @inquiry_state.setter
    def inquiry_state(self, inquiry_state):
        """Sets the inquiry_state of this MultiCompanyInquirySearchResult.


        :param inquiry_state: The inquiry_state of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._inquiry_state = inquiry_state

    @property
    def inquiry_zip(self):
        """Gets the inquiry_zip of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The inquiry_zip of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._inquiry_zip

    @inquiry_zip.setter
    def inquiry_zip(self, inquiry_zip):
        """Sets the inquiry_zip of this MultiCompanyInquirySearchResult.


        :param inquiry_zip: The inquiry_zip of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._inquiry_zip = inquiry_zip

    @property
    def primary_lead_source(self):
        """Gets the primary_lead_source of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The primary_lead_source of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._primary_lead_source

    @primary_lead_source.setter
    def primary_lead_source(self, primary_lead_source):
        """Sets the primary_lead_source of this MultiCompanyInquirySearchResult.


        :param primary_lead_source: The primary_lead_source of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._primary_lead_source = primary_lead_source

    @property
    def secondary_lead_source(self):
        """Gets the secondary_lead_source of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The secondary_lead_source of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._secondary_lead_source

    @secondary_lead_source.setter
    def secondary_lead_source(self, secondary_lead_source):
        """Sets the secondary_lead_source of this MultiCompanyInquirySearchResult.


        :param secondary_lead_source: The secondary_lead_source of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._secondary_lead_source = secondary_lead_source

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The phone_numbers of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this MultiCompanyInquirySearchResult.


        :param phone_numbers: The phone_numbers of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: list[str]
        """

        self._phone_numbers = phone_numbers

    @property
    def product_interest(self):
        """Gets the product_interest of this MultiCompanyInquirySearchResult.  # noqa: E501


        :return: The product_interest of this MultiCompanyInquirySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._product_interest

    @product_interest.setter
    def product_interest(self, product_interest):
        """Sets the product_interest of this MultiCompanyInquirySearchResult.


        :param product_interest: The product_interest of this MultiCompanyInquirySearchResult.  # noqa: E501
        :type: str
        """

        self._product_interest = product_interest

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MultiCompanyInquirySearchResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultiCompanyInquirySearchResult):
            return True

        return self.to_dict() != other.to_dict()