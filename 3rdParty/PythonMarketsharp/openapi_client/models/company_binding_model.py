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


class CompanyBindingModel(object):
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
        'name': 'str',
        'address': 'str',
        'address2': 'str',
        'city': 'str',
        'state': 'str',
        'zip': 'str',
        'phonenumber': 'str',
        'fax': 'str',
        'timezone': 'str',
        'country': 'str',
        'email': 'str',
        'website': 'str',
        'contact_name': 'str',
        'contact_title': 'str',
        'saturday_is_workday': 'bool',
        'sunday_is_workday': 'bool',
        'workday_start_time': 'datetime',
        'workday_end_time': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'address': 'address',
        'address2': 'address2',
        'city': 'city',
        'state': 'state',
        'zip': 'zip',
        'phonenumber': 'phonenumber',
        'fax': 'fax',
        'timezone': 'timezone',
        'country': 'country',
        'email': 'email',
        'website': 'website',
        'contact_name': 'contact_name',
        'contact_title': 'contact_title',
        'saturday_is_workday': 'saturday_is_workday',
        'sunday_is_workday': 'sunday_is_workday',
        'workday_start_time': 'workday_start_time',
        'workday_end_time': 'workday_end_time'
    }

    def __init__(self, name=None, address=None, address2=None, city=None, state=None, zip=None, phonenumber=None, fax=None, timezone=None, country=None, email=None, website=None, contact_name=None, contact_title=None, saturday_is_workday=None, sunday_is_workday=None, workday_start_time=None, workday_end_time=None, local_vars_configuration=None):  # noqa: E501
        """CompanyBindingModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._address = None
        self._address2 = None
        self._city = None
        self._state = None
        self._zip = None
        self._phonenumber = None
        self._fax = None
        self._timezone = None
        self._country = None
        self._email = None
        self._website = None
        self._contact_name = None
        self._contact_title = None
        self._saturday_is_workday = None
        self._sunday_is_workday = None
        self._workday_start_time = None
        self._workday_end_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if zip is not None:
            self.zip = zip
        if phonenumber is not None:
            self.phonenumber = phonenumber
        if fax is not None:
            self.fax = fax
        if timezone is not None:
            self.timezone = timezone
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if website is not None:
            self.website = website
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_title is not None:
            self.contact_title = contact_title
        if saturday_is_workday is not None:
            self.saturday_is_workday = saturday_is_workday
        if sunday_is_workday is not None:
            self.sunday_is_workday = sunday_is_workday
        if workday_start_time is not None:
            self.workday_start_time = workday_start_time
        if workday_end_time is not None:
            self.workday_end_time = workday_end_time

    @property
    def name(self):
        """Gets the name of this CompanyBindingModel.  # noqa: E501


        :return: The name of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CompanyBindingModel.


        :param name: The name of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this CompanyBindingModel.  # noqa: E501


        :return: The address of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CompanyBindingModel.


        :param address: The address of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this CompanyBindingModel.  # noqa: E501


        :return: The address2 of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this CompanyBindingModel.


        :param address2: The address2 of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this CompanyBindingModel.  # noqa: E501


        :return: The city of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CompanyBindingModel.


        :param city: The city of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this CompanyBindingModel.  # noqa: E501


        :return: The state of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CompanyBindingModel.


        :param state: The state of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this CompanyBindingModel.  # noqa: E501


        :return: The zip of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this CompanyBindingModel.


        :param zip: The zip of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def phonenumber(self):
        """Gets the phonenumber of this CompanyBindingModel.  # noqa: E501


        :return: The phonenumber of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._phonenumber

    @phonenumber.setter
    def phonenumber(self, phonenumber):
        """Sets the phonenumber of this CompanyBindingModel.


        :param phonenumber: The phonenumber of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._phonenumber = phonenumber

    @property
    def fax(self):
        """Gets the fax of this CompanyBindingModel.  # noqa: E501


        :return: The fax of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this CompanyBindingModel.


        :param fax: The fax of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def timezone(self):
        """Gets the timezone of this CompanyBindingModel.  # noqa: E501


        :return: The timezone of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this CompanyBindingModel.


        :param timezone: The timezone of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def country(self):
        """Gets the country of this CompanyBindingModel.  # noqa: E501


        :return: The country of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CompanyBindingModel.


        :param country: The country of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def email(self):
        """Gets the email of this CompanyBindingModel.  # noqa: E501


        :return: The email of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CompanyBindingModel.


        :param email: The email of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def website(self):
        """Gets the website of this CompanyBindingModel.  # noqa: E501


        :return: The website of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this CompanyBindingModel.


        :param website: The website of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def contact_name(self):
        """Gets the contact_name of this CompanyBindingModel.  # noqa: E501


        :return: The contact_name of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this CompanyBindingModel.


        :param contact_name: The contact_name of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def contact_title(self):
        """Gets the contact_title of this CompanyBindingModel.  # noqa: E501


        :return: The contact_title of this CompanyBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._contact_title

    @contact_title.setter
    def contact_title(self, contact_title):
        """Sets the contact_title of this CompanyBindingModel.


        :param contact_title: The contact_title of this CompanyBindingModel.  # noqa: E501
        :type: str
        """

        self._contact_title = contact_title

    @property
    def saturday_is_workday(self):
        """Gets the saturday_is_workday of this CompanyBindingModel.  # noqa: E501


        :return: The saturday_is_workday of this CompanyBindingModel.  # noqa: E501
        :rtype: bool
        """
        return self._saturday_is_workday

    @saturday_is_workday.setter
    def saturday_is_workday(self, saturday_is_workday):
        """Sets the saturday_is_workday of this CompanyBindingModel.


        :param saturday_is_workday: The saturday_is_workday of this CompanyBindingModel.  # noqa: E501
        :type: bool
        """

        self._saturday_is_workday = saturday_is_workday

    @property
    def sunday_is_workday(self):
        """Gets the sunday_is_workday of this CompanyBindingModel.  # noqa: E501


        :return: The sunday_is_workday of this CompanyBindingModel.  # noqa: E501
        :rtype: bool
        """
        return self._sunday_is_workday

    @sunday_is_workday.setter
    def sunday_is_workday(self, sunday_is_workday):
        """Sets the sunday_is_workday of this CompanyBindingModel.


        :param sunday_is_workday: The sunday_is_workday of this CompanyBindingModel.  # noqa: E501
        :type: bool
        """

        self._sunday_is_workday = sunday_is_workday

    @property
    def workday_start_time(self):
        """Gets the workday_start_time of this CompanyBindingModel.  # noqa: E501


        :return: The workday_start_time of this CompanyBindingModel.  # noqa: E501
        :rtype: datetime
        """
        return self._workday_start_time

    @workday_start_time.setter
    def workday_start_time(self, workday_start_time):
        """Sets the workday_start_time of this CompanyBindingModel.


        :param workday_start_time: The workday_start_time of this CompanyBindingModel.  # noqa: E501
        :type: datetime
        """

        self._workday_start_time = workday_start_time

    @property
    def workday_end_time(self):
        """Gets the workday_end_time of this CompanyBindingModel.  # noqa: E501


        :return: The workday_end_time of this CompanyBindingModel.  # noqa: E501
        :rtype: datetime
        """
        return self._workday_end_time

    @workday_end_time.setter
    def workday_end_time(self, workday_end_time):
        """Sets the workday_end_time of this CompanyBindingModel.


        :param workday_end_time: The workday_end_time of this CompanyBindingModel.  # noqa: E501
        :type: datetime
        """

        self._workday_end_time = workday_end_time

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
        if not isinstance(other, CompanyBindingModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompanyBindingModel):
            return True

        return self.to_dict() != other.to_dict()