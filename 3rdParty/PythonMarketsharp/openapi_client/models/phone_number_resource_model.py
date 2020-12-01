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


class PhoneNumberResourceModel(object):
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
        'id': 'str',
        'contact_id': 'str',
        'type': 'str',
        'is_primary': 'bool',
        'free_form_number': 'str',
        'phone_number_digits': 'str'
    }

    attribute_map = {
        'id': 'id',
        'contact_id': 'contactId',
        'type': 'type',
        'is_primary': 'isPrimary',
        'free_form_number': 'freeFormNumber',
        'phone_number_digits': 'phoneNumberDigits'
    }

    def __init__(self, id=None, contact_id=None, type=None, is_primary=None, free_form_number=None, phone_number_digits=None, local_vars_configuration=None):  # noqa: E501
        """PhoneNumberResourceModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._contact_id = None
        self._type = None
        self._is_primary = None
        self._free_form_number = None
        self._phone_number_digits = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if contact_id is not None:
            self.contact_id = contact_id
        if type is not None:
            self.type = type
        if is_primary is not None:
            self.is_primary = is_primary
        if free_form_number is not None:
            self.free_form_number = free_form_number
        if phone_number_digits is not None:
            self.phone_number_digits = phone_number_digits

    @property
    def id(self):
        """Gets the id of this PhoneNumberResourceModel.  # noqa: E501


        :return: The id of this PhoneNumberResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PhoneNumberResourceModel.


        :param id: The id of this PhoneNumberResourceModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def contact_id(self):
        """Gets the contact_id of this PhoneNumberResourceModel.  # noqa: E501


        :return: The contact_id of this PhoneNumberResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this PhoneNumberResourceModel.


        :param contact_id: The contact_id of this PhoneNumberResourceModel.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def type(self):
        """Gets the type of this PhoneNumberResourceModel.  # noqa: E501


        :return: The type of this PhoneNumberResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PhoneNumberResourceModel.


        :param type: The type of this PhoneNumberResourceModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def is_primary(self):
        """Gets the is_primary of this PhoneNumberResourceModel.  # noqa: E501


        :return: The is_primary of this PhoneNumberResourceModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        """Sets the is_primary of this PhoneNumberResourceModel.


        :param is_primary: The is_primary of this PhoneNumberResourceModel.  # noqa: E501
        :type: bool
        """

        self._is_primary = is_primary

    @property
    def free_form_number(self):
        """Gets the free_form_number of this PhoneNumberResourceModel.  # noqa: E501


        :return: The free_form_number of this PhoneNumberResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._free_form_number

    @free_form_number.setter
    def free_form_number(self, free_form_number):
        """Sets the free_form_number of this PhoneNumberResourceModel.


        :param free_form_number: The free_form_number of this PhoneNumberResourceModel.  # noqa: E501
        :type: str
        """

        self._free_form_number = free_form_number

    @property
    def phone_number_digits(self):
        """Gets the phone_number_digits of this PhoneNumberResourceModel.  # noqa: E501


        :return: The phone_number_digits of this PhoneNumberResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._phone_number_digits

    @phone_number_digits.setter
    def phone_number_digits(self, phone_number_digits):
        """Sets the phone_number_digits of this PhoneNumberResourceModel.


        :param phone_number_digits: The phone_number_digits of this PhoneNumberResourceModel.  # noqa: E501
        :type: str
        """

        self._phone_number_digits = phone_number_digits

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
        if not isinstance(other, PhoneNumberResourceModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhoneNumberResourceModel):
            return True

        return self.to_dict() != other.to_dict()
