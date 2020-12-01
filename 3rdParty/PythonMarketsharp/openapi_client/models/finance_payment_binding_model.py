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


class FinancePaymentBindingModel(object):
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
        'contract_id': 'str',
        'payment_type': 'str',
        'payment_method': 'str',
        'description': 'str',
        'payment_date': 'datetime',
        'amount': 'float',
        'cash_finance': 'str',
        'pay_simple_payment_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'contract_id': 'contractId',
        'payment_type': 'paymentType',
        'payment_method': 'paymentMethod',
        'description': 'description',
        'payment_date': 'paymentDate',
        'amount': 'amount',
        'cash_finance': 'cashFinance',
        'pay_simple_payment_id': 'paySimplePaymentID'
    }

    def __init__(self, id=None, contract_id=None, payment_type=None, payment_method=None, description=None, payment_date=None, amount=None, cash_finance=None, pay_simple_payment_id=None, local_vars_configuration=None):  # noqa: E501
        """FinancePaymentBindingModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._contract_id = None
        self._payment_type = None
        self._payment_method = None
        self._description = None
        self._payment_date = None
        self._amount = None
        self._cash_finance = None
        self._pay_simple_payment_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.contract_id = contract_id
        self.payment_type = payment_type
        if payment_method is not None:
            self.payment_method = payment_method
        if description is not None:
            self.description = description
        if payment_date is not None:
            self.payment_date = payment_date
        self.amount = amount
        self.cash_finance = cash_finance
        if pay_simple_payment_id is not None:
            self.pay_simple_payment_id = pay_simple_payment_id

    @property
    def id(self):
        """Gets the id of this FinancePaymentBindingModel.  # noqa: E501

        The id of the payment history to update  # noqa: E501

        :return: The id of this FinancePaymentBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FinancePaymentBindingModel.

        The id of the payment history to update  # noqa: E501

        :param id: The id of this FinancePaymentBindingModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def contract_id(self):
        """Gets the contract_id of this FinancePaymentBindingModel.  # noqa: E501


        :return: The contract_id of this FinancePaymentBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this FinancePaymentBindingModel.


        :param contract_id: The contract_id of this FinancePaymentBindingModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and contract_id is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_id`, must not be `None`")  # noqa: E501

        self._contract_id = contract_id

    @property
    def payment_type(self):
        """Gets the payment_type of this FinancePaymentBindingModel.  # noqa: E501

        Downpayment, payment, .... user defined data  # noqa: E501

        :return: The payment_type of this FinancePaymentBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this FinancePaymentBindingModel.

        Downpayment, payment, .... user defined data  # noqa: E501

        :param payment_type: The payment_type of this FinancePaymentBindingModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and payment_type is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_type`, must not be `None`")  # noqa: E501

        self._payment_type = payment_type

    @property
    def payment_method(self):
        """Gets the payment_method of this FinancePaymentBindingModel.  # noqa: E501

        The payment method of cash, credit card, check, ach. User defined data, but PaySimple gurantees 'Credit Card' and 'ACH' will be available  # noqa: E501

        :return: The payment_method of this FinancePaymentBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this FinancePaymentBindingModel.

        The payment method of cash, credit card, check, ach. User defined data, but PaySimple gurantees 'Credit Card' and 'ACH' will be available  # noqa: E501

        :param payment_method: The payment_method of this FinancePaymentBindingModel.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def description(self):
        """Gets the description of this FinancePaymentBindingModel.  # noqa: E501

        An optional bit of user entered text that can be said provides additional information about a payment.  # noqa: E501

        :return: The description of this FinancePaymentBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FinancePaymentBindingModel.

        An optional bit of user entered text that can be said provides additional information about a payment.  # noqa: E501

        :param description: The description of this FinancePaymentBindingModel.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def payment_date(self):
        """Gets the payment_date of this FinancePaymentBindingModel.  # noqa: E501

        Date of Payment  # noqa: E501

        :return: The payment_date of this FinancePaymentBindingModel.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this FinancePaymentBindingModel.

        Date of Payment  # noqa: E501

        :param payment_date: The payment_date of this FinancePaymentBindingModel.  # noqa: E501
        :type: datetime
        """

        self._payment_date = payment_date

    @property
    def amount(self):
        """Gets the amount of this FinancePaymentBindingModel.  # noqa: E501

        Stored as negative values in the database  # noqa: E501

        :return: The amount of this FinancePaymentBindingModel.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FinancePaymentBindingModel.

        Stored as negative values in the database  # noqa: E501

        :param amount: The amount of this FinancePaymentBindingModel.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def cash_finance(self):
        """Gets the cash_finance of this FinancePaymentBindingModel.  # noqa: E501

        Used as part of Applies to Contract for finance or cash.  NONE: does not apply to the contract  CASH: applies to contract  FINANCE: applies to contract  # noqa: E501

        :return: The cash_finance of this FinancePaymentBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._cash_finance

    @cash_finance.setter
    def cash_finance(self, cash_finance):
        """Sets the cash_finance of this FinancePaymentBindingModel.

        Used as part of Applies to Contract for finance or cash.  NONE: does not apply to the contract  CASH: applies to contract  FINANCE: applies to contract  # noqa: E501

        :param cash_finance: The cash_finance of this FinancePaymentBindingModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cash_finance is None:  # noqa: E501
            raise ValueError("Invalid value for `cash_finance`, must not be `None`")  # noqa: E501

        self._cash_finance = cash_finance

    @property
    def pay_simple_payment_id(self):
        """Gets the pay_simple_payment_id of this FinancePaymentBindingModel.  # noqa: E501

        ID of PaySimple Payment if applicable  # noqa: E501

        :return: The pay_simple_payment_id of this FinancePaymentBindingModel.  # noqa: E501
        :rtype: int
        """
        return self._pay_simple_payment_id

    @pay_simple_payment_id.setter
    def pay_simple_payment_id(self, pay_simple_payment_id):
        """Sets the pay_simple_payment_id of this FinancePaymentBindingModel.

        ID of PaySimple Payment if applicable  # noqa: E501

        :param pay_simple_payment_id: The pay_simple_payment_id of this FinancePaymentBindingModel.  # noqa: E501
        :type: int
        """

        self._pay_simple_payment_id = pay_simple_payment_id

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
        if not isinstance(other, FinancePaymentBindingModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FinancePaymentBindingModel):
            return True

        return self.to_dict() != other.to_dict()