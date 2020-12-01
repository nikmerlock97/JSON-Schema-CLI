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


class SimpleProductDetailResourceModel(object):
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
        'product_detail_id': 'str',
        'product_detail_name': 'str'
    }

    attribute_map = {
        'product_detail_id': 'productDetailId',
        'product_detail_name': 'productDetailName'
    }

    def __init__(self, product_detail_id=None, product_detail_name=None, local_vars_configuration=None):  # noqa: E501
        """SimpleProductDetailResourceModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._product_detail_id = None
        self._product_detail_name = None
        self.discriminator = None

        if product_detail_id is not None:
            self.product_detail_id = product_detail_id
        if product_detail_name is not None:
            self.product_detail_name = product_detail_name

    @property
    def product_detail_id(self):
        """Gets the product_detail_id of this SimpleProductDetailResourceModel.  # noqa: E501

        Product detail id.  # noqa: E501

        :return: The product_detail_id of this SimpleProductDetailResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._product_detail_id

    @product_detail_id.setter
    def product_detail_id(self, product_detail_id):
        """Sets the product_detail_id of this SimpleProductDetailResourceModel.

        Product detail id.  # noqa: E501

        :param product_detail_id: The product_detail_id of this SimpleProductDetailResourceModel.  # noqa: E501
        :type: str
        """

        self._product_detail_id = product_detail_id

    @property
    def product_detail_name(self):
        """Gets the product_detail_name of this SimpleProductDetailResourceModel.  # noqa: E501

        The name of the product detail record.  # noqa: E501

        :return: The product_detail_name of this SimpleProductDetailResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._product_detail_name

    @product_detail_name.setter
    def product_detail_name(self, product_detail_name):
        """Sets the product_detail_name of this SimpleProductDetailResourceModel.

        The name of the product detail record.  # noqa: E501

        :param product_detail_name: The product_detail_name of this SimpleProductDetailResourceModel.  # noqa: E501
        :type: str
        """

        self._product_detail_name = product_detail_name

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
        if not isinstance(other, SimpleProductDetailResourceModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimpleProductDetailResourceModel):
            return True

        return self.to_dict() != other.to_dict()