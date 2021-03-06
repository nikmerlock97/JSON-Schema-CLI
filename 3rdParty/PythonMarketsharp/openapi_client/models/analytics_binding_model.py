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


class AnalyticsBindingModel(object):
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
        'net_sales': 'bool',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'divisions': 'list[str]',
        'include_white_space_divs': 'bool',
        'widget_guid': 'str',
        'pref_value': 'str',
        'use_sales_pace_month': 'bool'
    }

    attribute_map = {
        'net_sales': 'netSales',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'divisions': 'divisions',
        'include_white_space_divs': 'includeWhiteSpaceDivs',
        'widget_guid': 'widgetGuid',
        'pref_value': 'prefValue',
        'use_sales_pace_month': 'useSalesPaceMonth'
    }

    def __init__(self, net_sales=None, start_date=None, end_date=None, divisions=None, include_white_space_divs=None, widget_guid=None, pref_value=None, use_sales_pace_month=None, local_vars_configuration=None):  # noqa: E501
        """AnalyticsBindingModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._net_sales = None
        self._start_date = None
        self._end_date = None
        self._divisions = None
        self._include_white_space_divs = None
        self._widget_guid = None
        self._pref_value = None
        self._use_sales_pace_month = None
        self.discriminator = None

        if net_sales is not None:
            self.net_sales = net_sales
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if divisions is not None:
            self.divisions = divisions
        if include_white_space_divs is not None:
            self.include_white_space_divs = include_white_space_divs
        if widget_guid is not None:
            self.widget_guid = widget_guid
        if pref_value is not None:
            self.pref_value = pref_value
        if use_sales_pace_month is not None:
            self.use_sales_pace_month = use_sales_pace_month

    @property
    def net_sales(self):
        """Gets the net_sales of this AnalyticsBindingModel.  # noqa: E501


        :return: The net_sales of this AnalyticsBindingModel.  # noqa: E501
        :rtype: bool
        """
        return self._net_sales

    @net_sales.setter
    def net_sales(self, net_sales):
        """Sets the net_sales of this AnalyticsBindingModel.


        :param net_sales: The net_sales of this AnalyticsBindingModel.  # noqa: E501
        :type: bool
        """

        self._net_sales = net_sales

    @property
    def start_date(self):
        """Gets the start_date of this AnalyticsBindingModel.  # noqa: E501


        :return: The start_date of this AnalyticsBindingModel.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this AnalyticsBindingModel.


        :param start_date: The start_date of this AnalyticsBindingModel.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this AnalyticsBindingModel.  # noqa: E501


        :return: The end_date of this AnalyticsBindingModel.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this AnalyticsBindingModel.


        :param end_date: The end_date of this AnalyticsBindingModel.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def divisions(self):
        """Gets the divisions of this AnalyticsBindingModel.  # noqa: E501


        :return: The divisions of this AnalyticsBindingModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._divisions

    @divisions.setter
    def divisions(self, divisions):
        """Sets the divisions of this AnalyticsBindingModel.


        :param divisions: The divisions of this AnalyticsBindingModel.  # noqa: E501
        :type: list[str]
        """

        self._divisions = divisions

    @property
    def include_white_space_divs(self):
        """Gets the include_white_space_divs of this AnalyticsBindingModel.  # noqa: E501


        :return: The include_white_space_divs of this AnalyticsBindingModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_white_space_divs

    @include_white_space_divs.setter
    def include_white_space_divs(self, include_white_space_divs):
        """Sets the include_white_space_divs of this AnalyticsBindingModel.


        :param include_white_space_divs: The include_white_space_divs of this AnalyticsBindingModel.  # noqa: E501
        :type: bool
        """

        self._include_white_space_divs = include_white_space_divs

    @property
    def widget_guid(self):
        """Gets the widget_guid of this AnalyticsBindingModel.  # noqa: E501


        :return: The widget_guid of this AnalyticsBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._widget_guid

    @widget_guid.setter
    def widget_guid(self, widget_guid):
        """Sets the widget_guid of this AnalyticsBindingModel.


        :param widget_guid: The widget_guid of this AnalyticsBindingModel.  # noqa: E501
        :type: str
        """

        self._widget_guid = widget_guid

    @property
    def pref_value(self):
        """Gets the pref_value of this AnalyticsBindingModel.  # noqa: E501


        :return: The pref_value of this AnalyticsBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._pref_value

    @pref_value.setter
    def pref_value(self, pref_value):
        """Sets the pref_value of this AnalyticsBindingModel.


        :param pref_value: The pref_value of this AnalyticsBindingModel.  # noqa: E501
        :type: str
        """

        self._pref_value = pref_value

    @property
    def use_sales_pace_month(self):
        """Gets the use_sales_pace_month of this AnalyticsBindingModel.  # noqa: E501


        :return: The use_sales_pace_month of this AnalyticsBindingModel.  # noqa: E501
        :rtype: bool
        """
        return self._use_sales_pace_month

    @use_sales_pace_month.setter
    def use_sales_pace_month(self, use_sales_pace_month):
        """Sets the use_sales_pace_month of this AnalyticsBindingModel.


        :param use_sales_pace_month: The use_sales_pace_month of this AnalyticsBindingModel.  # noqa: E501
        :type: bool
        """

        self._use_sales_pace_month = use_sales_pace_month

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
        if not isinstance(other, AnalyticsBindingModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnalyticsBindingModel):
            return True

        return self.to_dict() != other.to_dict()
