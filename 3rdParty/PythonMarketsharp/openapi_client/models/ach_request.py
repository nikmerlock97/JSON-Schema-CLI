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


class ACHRequest(object):
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
        'id': 'int',
        'is_checking_account': 'bool',
        'routing_number': 'str',
        'account_number': 'str',
        'bank_name': 'str',
        'customer_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'is_checking_account': 'isCheckingAccount',
        'routing_number': 'routingNumber',
        'account_number': 'accountNumber',
        'bank_name': 'bankName',
        'customer_id': 'customerId'
    }

    def __init__(self, id=None, is_checking_account=None, routing_number=None, account_number=None, bank_name=None, customer_id=None, local_vars_configuration=None):  # noqa: E501
        """ACHRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._is_checking_account = None
        self._routing_number = None
        self._account_number = None
        self._bank_name = None
        self._customer_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if is_checking_account is not None:
            self.is_checking_account = is_checking_account
        if routing_number is not None:
            self.routing_number = routing_number
        if account_number is not None:
            self.account_number = account_number
        if bank_name is not None:
            self.bank_name = bank_name
        if customer_id is not None:
            self.customer_id = customer_id

    @property
    def id(self):
        """Gets the id of this ACHRequest.  # noqa: E501


        :return: The id of this ACHRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ACHRequest.


        :param id: The id of this ACHRequest.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_checking_account(self):
        """Gets the is_checking_account of this ACHRequest.  # noqa: E501


        :return: The is_checking_account of this ACHRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_checking_account

    @is_checking_account.setter
    def is_checking_account(self, is_checking_account):
        """Sets the is_checking_account of this ACHRequest.


        :param is_checking_account: The is_checking_account of this ACHRequest.  # noqa: E501
        :type: bool
        """

        self._is_checking_account = is_checking_account

    @property
    def routing_number(self):
        """Gets the routing_number of this ACHRequest.  # noqa: E501


        :return: The routing_number of this ACHRequest.  # noqa: E501
        :rtype: str
        """
        return self._routing_number

    @routing_number.setter
    def routing_number(self, routing_number):
        """Sets the routing_number of this ACHRequest.


        :param routing_number: The routing_number of this ACHRequest.  # noqa: E501
        :type: str
        """

        self._routing_number = routing_number

    @property
    def account_number(self):
        """Gets the account_number of this ACHRequest.  # noqa: E501


        :return: The account_number of this ACHRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this ACHRequest.


        :param account_number: The account_number of this ACHRequest.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def bank_name(self):
        """Gets the bank_name of this ACHRequest.  # noqa: E501


        :return: The bank_name of this ACHRequest.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this ACHRequest.


        :param bank_name: The bank_name of this ACHRequest.  # noqa: E501
        :type: str
        """

        self._bank_name = bank_name

    @property
    def customer_id(self):
        """Gets the customer_id of this ACHRequest.  # noqa: E501


        :return: The customer_id of this ACHRequest.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ACHRequest.


        :param customer_id: The customer_id of this ACHRequest.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

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
        if not isinstance(other, ACHRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ACHRequest):
            return True

        return self.to_dict() != other.to_dict()
