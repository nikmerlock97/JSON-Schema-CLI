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


class PaysimpleContactJobSearchBindingModel(object):
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
        'paysimple_customer_id': 'int',
        'name': 'str',
        'email': 'str',
        'appointment_date': 'datetime',
        'use_and_search': 'bool'
    }

    attribute_map = {
        'paysimple_customer_id': 'paysimpleCustomerId',
        'name': 'name',
        'email': 'email',
        'appointment_date': 'appointmentDate',
        'use_and_search': 'useAndSearch'
    }

    def __init__(self, paysimple_customer_id=None, name=None, email=None, appointment_date=None, use_and_search=None, local_vars_configuration=None):  # noqa: E501
        """PaysimpleContactJobSearchBindingModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._paysimple_customer_id = None
        self._name = None
        self._email = None
        self._appointment_date = None
        self._use_and_search = None
        self.discriminator = None

        if paysimple_customer_id is not None:
            self.paysimple_customer_id = paysimple_customer_id
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if appointment_date is not None:
            self.appointment_date = appointment_date
        if use_and_search is not None:
            self.use_and_search = use_and_search

    @property
    def paysimple_customer_id(self):
        """Gets the paysimple_customer_id of this PaysimpleContactJobSearchBindingModel.  # noqa: E501


        :return: The paysimple_customer_id of this PaysimpleContactJobSearchBindingModel.  # noqa: E501
        :rtype: int
        """
        return self._paysimple_customer_id

    @paysimple_customer_id.setter
    def paysimple_customer_id(self, paysimple_customer_id):
        """Sets the paysimple_customer_id of this PaysimpleContactJobSearchBindingModel.


        :param paysimple_customer_id: The paysimple_customer_id of this PaysimpleContactJobSearchBindingModel.  # noqa: E501
        :type: int
        """

        self._paysimple_customer_id = paysimple_customer_id

    @property
    def name(self):
        """Gets the name of this PaysimpleContactJobSearchBindingModel.  # noqa: E501


        :return: The name of this PaysimpleContactJobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaysimpleContactJobSearchBindingModel.


        :param name: The name of this PaysimpleContactJobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this PaysimpleContactJobSearchBindingModel.  # noqa: E501


        :return: The email of this PaysimpleContactJobSearchBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PaysimpleContactJobSearchBindingModel.


        :param email: The email of this PaysimpleContactJobSearchBindingModel.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def appointment_date(self):
        """Gets the appointment_date of this PaysimpleContactJobSearchBindingModel.  # noqa: E501


        :return: The appointment_date of this PaysimpleContactJobSearchBindingModel.  # noqa: E501
        :rtype: datetime
        """
        return self._appointment_date

    @appointment_date.setter
    def appointment_date(self, appointment_date):
        """Sets the appointment_date of this PaysimpleContactJobSearchBindingModel.


        :param appointment_date: The appointment_date of this PaysimpleContactJobSearchBindingModel.  # noqa: E501
        :type: datetime
        """

        self._appointment_date = appointment_date

    @property
    def use_and_search(self):
        """Gets the use_and_search of this PaysimpleContactJobSearchBindingModel.  # noqa: E501


        :return: The use_and_search of this PaysimpleContactJobSearchBindingModel.  # noqa: E501
        :rtype: bool
        """
        return self._use_and_search

    @use_and_search.setter
    def use_and_search(self, use_and_search):
        """Sets the use_and_search of this PaysimpleContactJobSearchBindingModel.


        :param use_and_search: The use_and_search of this PaysimpleContactJobSearchBindingModel.  # noqa: E501
        :type: bool
        """

        self._use_and_search = use_and_search

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
        if not isinstance(other, PaysimpleContactJobSearchBindingModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaysimpleContactJobSearchBindingModel):
            return True

        return self.to_dict() != other.to_dict()
