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


class PrintFileExistsBindingModel(object):
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
        'exists': 'bool',
        'last_update_by_employee_name': 'str',
        'last_update': 'datetime'
    }

    attribute_map = {
        'exists': 'exists',
        'last_update_by_employee_name': 'lastUpdateByEmployeeName',
        'last_update': 'lastUpdate'
    }

    def __init__(self, exists=None, last_update_by_employee_name=None, last_update=None, local_vars_configuration=None):  # noqa: E501
        """PrintFileExistsBindingModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._exists = None
        self._last_update_by_employee_name = None
        self._last_update = None
        self.discriminator = None

        if exists is not None:
            self.exists = exists
        if last_update_by_employee_name is not None:
            self.last_update_by_employee_name = last_update_by_employee_name
        if last_update is not None:
            self.last_update = last_update

    @property
    def exists(self):
        """Gets the exists of this PrintFileExistsBindingModel.  # noqa: E501


        :return: The exists of this PrintFileExistsBindingModel.  # noqa: E501
        :rtype: bool
        """
        return self._exists

    @exists.setter
    def exists(self, exists):
        """Sets the exists of this PrintFileExistsBindingModel.


        :param exists: The exists of this PrintFileExistsBindingModel.  # noqa: E501
        :type: bool
        """

        self._exists = exists

    @property
    def last_update_by_employee_name(self):
        """Gets the last_update_by_employee_name of this PrintFileExistsBindingModel.  # noqa: E501


        :return: The last_update_by_employee_name of this PrintFileExistsBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._last_update_by_employee_name

    @last_update_by_employee_name.setter
    def last_update_by_employee_name(self, last_update_by_employee_name):
        """Sets the last_update_by_employee_name of this PrintFileExistsBindingModel.


        :param last_update_by_employee_name: The last_update_by_employee_name of this PrintFileExistsBindingModel.  # noqa: E501
        :type: str
        """

        self._last_update_by_employee_name = last_update_by_employee_name

    @property
    def last_update(self):
        """Gets the last_update of this PrintFileExistsBindingModel.  # noqa: E501


        :return: The last_update of this PrintFileExistsBindingModel.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this PrintFileExistsBindingModel.


        :param last_update: The last_update of this PrintFileExistsBindingModel.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

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
        if not isinstance(other, PrintFileExistsBindingModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintFileExistsBindingModel):
            return True

        return self.to_dict() != other.to_dict()
