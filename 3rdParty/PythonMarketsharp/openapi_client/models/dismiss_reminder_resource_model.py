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


class DismissReminderResourceModel(object):
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
        'dismiss_successful': 'bool'
    }

    attribute_map = {
        'dismiss_successful': 'dismissSuccessful'
    }

    def __init__(self, dismiss_successful=None, local_vars_configuration=None):  # noqa: E501
        """DismissReminderResourceModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dismiss_successful = None
        self.discriminator = None

        if dismiss_successful is not None:
            self.dismiss_successful = dismiss_successful

    @property
    def dismiss_successful(self):
        """Gets the dismiss_successful of this DismissReminderResourceModel.  # noqa: E501


        :return: The dismiss_successful of this DismissReminderResourceModel.  # noqa: E501
        :rtype: bool
        """
        return self._dismiss_successful

    @dismiss_successful.setter
    def dismiss_successful(self, dismiss_successful):
        """Sets the dismiss_successful of this DismissReminderResourceModel.


        :param dismiss_successful: The dismiss_successful of this DismissReminderResourceModel.  # noqa: E501
        :type: bool
        """

        self._dismiss_successful = dismiss_successful

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
        if not isinstance(other, DismissReminderResourceModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DismissReminderResourceModel):
            return True

        return self.to_dict() != other.to_dict()
