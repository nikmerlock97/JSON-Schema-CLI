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


class JobSearchBindingModel(object):
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
        'business_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'address_line_one': 'str',
        'city': 'str',
        'state': 'str',
        'zip': 'str',
        'email_address': 'str',
        'phone_number': 'str',
        'job_name': 'str',
        'job_number': 'str',
        'contact_type': 'int',
        'company_id': 'str',
        'number_of_records': 'int'
    }

    attribute_map = {
        'business_name': 'business_name',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'address_line_one': 'address_line_one',
        'city': 'city',
        'state': 'state',
        'zip': 'zip',
        'email_address': 'email_address',
        'phone_number': 'phone_number',
        'job_name': 'job_name',
        'job_number': 'job_number',
        'contact_type': 'contactType',
        'company_id': 'companyId',
        'number_of_records': 'numberOfRecords'
    }

    def __init__(self, business_name=None, first_name=None, last_name=None, address_line_one=None, city=None, state=None, zip=None, email_address=None, phone_number=None, job_name=None, job_number=None, contact_type=None, company_id=None, number_of_records=None, local_vars_configuration=None):  # noqa: E501
        """JobSearchBindingModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._business_name = None
        self._first_name = None
        self._last_name = None
        self._address_line_one = None
        self._city = None
        self._state = None
        self._zip = None
        self._email_address = None
        self._phone_number = None
        self._job_name = None
        self._job_number = None
        self._contact_type = None
        self._company_id = None
        self._number_of_records = None
        self.discriminator = None

        if business_name is not None:
            self.business_name = business_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if address_line_one is not None:
            self.address_line_one = address_line_one
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if zip is not None:
            self.zip = zip
        if email_address is not None:
            self.email_address = email_address
        if phone_number is not None:
            self.phone_number = phone_number
        if job_name is not None:
            self.job_name = job_name
        if job_number is not None:
            self.job_number = job_number
        if contact_type is not None:
            self.contact_type = contact_type
        if company_id is not None:
            self.company_id = company_id
        if number_of_records is not None:
            self.number_of_records = number_of_records

    @property
    def business_name(self):
        """Gets the business_name of this JobSearchBindingModel.  # noqa: E501


        :return: The business_name of this JobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """Sets the business_name of this JobSearchBindingModel.


        :param business_name: The business_name of this JobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._business_name = business_name

    @property
    def first_name(self):
        """Gets the first_name of this JobSearchBindingModel.  # noqa: E501


        :return: The first_name of this JobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this JobSearchBindingModel.


        :param first_name: The first_name of this JobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this JobSearchBindingModel.  # noqa: E501


        :return: The last_name of this JobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this JobSearchBindingModel.


        :param last_name: The last_name of this JobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def address_line_one(self):
        """Gets the address_line_one of this JobSearchBindingModel.  # noqa: E501


        :return: The address_line_one of this JobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._address_line_one

    @address_line_one.setter
    def address_line_one(self, address_line_one):
        """Sets the address_line_one of this JobSearchBindingModel.


        :param address_line_one: The address_line_one of this JobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._address_line_one = address_line_one

    @property
    def city(self):
        """Gets the city of this JobSearchBindingModel.  # noqa: E501


        :return: The city of this JobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this JobSearchBindingModel.


        :param city: The city of this JobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this JobSearchBindingModel.  # noqa: E501


        :return: The state of this JobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this JobSearchBindingModel.


        :param state: The state of this JobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this JobSearchBindingModel.  # noqa: E501


        :return: The zip of this JobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this JobSearchBindingModel.


        :param zip: The zip of this JobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def email_address(self):
        """Gets the email_address of this JobSearchBindingModel.  # noqa: E501


        :return: The email_address of this JobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this JobSearchBindingModel.


        :param email_address: The email_address of this JobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def phone_number(self):
        """Gets the phone_number of this JobSearchBindingModel.  # noqa: E501


        :return: The phone_number of this JobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this JobSearchBindingModel.


        :param phone_number: The phone_number of this JobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def job_name(self):
        """Gets the job_name of this JobSearchBindingModel.  # noqa: E501


        :return: The job_name of this JobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this JobSearchBindingModel.


        :param job_name: The job_name of this JobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._job_name = job_name

    @property
    def job_number(self):
        """Gets the job_number of this JobSearchBindingModel.  # noqa: E501


        :return: The job_number of this JobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._job_number

    @job_number.setter
    def job_number(self, job_number):
        """Sets the job_number of this JobSearchBindingModel.


        :param job_number: The job_number of this JobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._job_number = job_number

    @property
    def contact_type(self):
        """Gets the contact_type of this JobSearchBindingModel.  # noqa: E501


        :return: The contact_type of this JobSearchBindingModel.  # noqa: E501
        :rtype: int
        """
        return self._contact_type

    @contact_type.setter
    def contact_type(self, contact_type):
        """Sets the contact_type of this JobSearchBindingModel.


        :param contact_type: The contact_type of this JobSearchBindingModel.  # noqa: E501
        :type: int
        """

        self._contact_type = contact_type

    @property
    def company_id(self):
        """Gets the company_id of this JobSearchBindingModel.  # noqa: E501


        :return: The company_id of this JobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this JobSearchBindingModel.


        :param company_id: The company_id of this JobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def number_of_records(self):
        """Gets the number_of_records of this JobSearchBindingModel.  # noqa: E501


        :return: The number_of_records of this JobSearchBindingModel.  # noqa: E501
        :rtype: int
        """
        return self._number_of_records

    @number_of_records.setter
    def number_of_records(self, number_of_records):
        """Sets the number_of_records of this JobSearchBindingModel.


        :param number_of_records: The number_of_records of this JobSearchBindingModel.  # noqa: E501
        :type: int
        """

        self._number_of_records = number_of_records

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
        if not isinstance(other, JobSearchBindingModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobSearchBindingModel):
            return True

        return self.to_dict() != other.to_dict()
