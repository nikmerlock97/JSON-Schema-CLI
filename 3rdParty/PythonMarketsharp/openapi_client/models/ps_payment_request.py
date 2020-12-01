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


class PSPaymentRequest(object):
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
        'account_id': 'int',
        'amount': 'float',
        'is_debit': 'str',
        'invoice_number': 'int',
        'purchase_order_number': 'int',
        'order_id': 'str',
        'description': 'str',
        'cvv': 'str',
        'payment_sub_type': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'amount': 'amount',
        'is_debit': 'isDebit',
        'invoice_number': 'invoiceNumber',
        'purchase_order_number': 'purchaseOrderNumber',
        'order_id': 'orderId',
        'description': 'description',
        'cvv': 'cvv',
        'payment_sub_type': 'paymentSubType'
    }

    def __init__(self, account_id=None, amount=None, is_debit=None, invoice_number=None, purchase_order_number=None, order_id=None, description=None, cvv=None, payment_sub_type=None, local_vars_configuration=None):  # noqa: E501
        """PSPaymentRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._amount = None
        self._is_debit = None
        self._invoice_number = None
        self._purchase_order_number = None
        self._order_id = None
        self._description = None
        self._cvv = None
        self._payment_sub_type = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if amount is not None:
            self.amount = amount
        if is_debit is not None:
            self.is_debit = is_debit
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if purchase_order_number is not None:
            self.purchase_order_number = purchase_order_number
        if order_id is not None:
            self.order_id = order_id
        if description is not None:
            self.description = description
        if cvv is not None:
            self.cvv = cvv
        if payment_sub_type is not None:
            self.payment_sub_type = payment_sub_type

    @property
    def account_id(self):
        """Gets the account_id of this PSPaymentRequest.  # noqa: E501


        :return: The account_id of this PSPaymentRequest.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PSPaymentRequest.


        :param account_id: The account_id of this PSPaymentRequest.  # noqa: E501
        :type: int
        """

        self._account_id = account_id

    @property
    def amount(self):
        """Gets the amount of this PSPaymentRequest.  # noqa: E501


        :return: The amount of this PSPaymentRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PSPaymentRequest.


        :param amount: The amount of this PSPaymentRequest.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def is_debit(self):
        """Gets the is_debit of this PSPaymentRequest.  # noqa: E501


        :return: The is_debit of this PSPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._is_debit

    @is_debit.setter
    def is_debit(self, is_debit):
        """Sets the is_debit of this PSPaymentRequest.


        :param is_debit: The is_debit of this PSPaymentRequest.  # noqa: E501
        :type: str
        """

        self._is_debit = is_debit

    @property
    def invoice_number(self):
        """Gets the invoice_number of this PSPaymentRequest.  # noqa: E501


        :return: The invoice_number of this PSPaymentRequest.  # noqa: E501
        :rtype: int
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this PSPaymentRequest.


        :param invoice_number: The invoice_number of this PSPaymentRequest.  # noqa: E501
        :type: int
        """

        self._invoice_number = invoice_number

    @property
    def purchase_order_number(self):
        """Gets the purchase_order_number of this PSPaymentRequest.  # noqa: E501


        :return: The purchase_order_number of this PSPaymentRequest.  # noqa: E501
        :rtype: int
        """
        return self._purchase_order_number

    @purchase_order_number.setter
    def purchase_order_number(self, purchase_order_number):
        """Sets the purchase_order_number of this PSPaymentRequest.


        :param purchase_order_number: The purchase_order_number of this PSPaymentRequest.  # noqa: E501
        :type: int
        """

        self._purchase_order_number = purchase_order_number

    @property
    def order_id(self):
        """Gets the order_id of this PSPaymentRequest.  # noqa: E501


        :return: The order_id of this PSPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PSPaymentRequest.


        :param order_id: The order_id of this PSPaymentRequest.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def description(self):
        """Gets the description of this PSPaymentRequest.  # noqa: E501


        :return: The description of this PSPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PSPaymentRequest.


        :param description: The description of this PSPaymentRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def cvv(self):
        """Gets the cvv of this PSPaymentRequest.  # noqa: E501


        :return: The cvv of this PSPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        """Sets the cvv of this PSPaymentRequest.


        :param cvv: The cvv of this PSPaymentRequest.  # noqa: E501
        :type: str
        """

        self._cvv = cvv

    @property
    def payment_sub_type(self):
        """Gets the payment_sub_type of this PSPaymentRequest.  # noqa: E501


        :return: The payment_sub_type of this PSPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_sub_type

    @payment_sub_type.setter
    def payment_sub_type(self, payment_sub_type):
        """Sets the payment_sub_type of this PSPaymentRequest.


        :param payment_sub_type: The payment_sub_type of this PSPaymentRequest.  # noqa: E501
        :type: str
        """

        self._payment_sub_type = payment_sub_type

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
        if not isinstance(other, PSPaymentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PSPaymentRequest):
            return True

        return self.to_dict() != other.to_dict()
