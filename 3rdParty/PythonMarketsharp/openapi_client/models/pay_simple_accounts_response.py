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


class PaySimpleAccountsResponse(object):
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
        'response': 'AccountsResponse',
        'meta': 'Meta'
    }

    attribute_map = {
        'response': 'response',
        'meta': 'meta'
    }

    def __init__(self, response=None, meta=None, local_vars_configuration=None):  # noqa: E501
        """PaySimpleAccountsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._response = None
        self._meta = None
        self.discriminator = None

        if response is not None:
            self.response = response
        if meta is not None:
            self.meta = meta

    @property
    def response(self):
        """Gets the response of this PaySimpleAccountsResponse.  # noqa: E501


        :return: The response of this PaySimpleAccountsResponse.  # noqa: E501
        :rtype: AccountsResponse
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this PaySimpleAccountsResponse.


        :param response: The response of this PaySimpleAccountsResponse.  # noqa: E501
        :type: AccountsResponse
        """

        self._response = response

    @property
    def meta(self):
        """Gets the meta of this PaySimpleAccountsResponse.  # noqa: E501


        :return: The meta of this PaySimpleAccountsResponse.  # noqa: E501
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this PaySimpleAccountsResponse.


        :param meta: The meta of this PaySimpleAccountsResponse.  # noqa: E501
        :type: Meta
        """

        self._meta = meta

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
        if not isinstance(other, PaySimpleAccountsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaySimpleAccountsResponse):
            return True

        return self.to_dict() != other.to_dict()
