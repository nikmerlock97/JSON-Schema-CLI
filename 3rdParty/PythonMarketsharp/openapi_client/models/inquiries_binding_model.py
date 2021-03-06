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


class InquiriesBindingModel(object):
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
        'start_modified_datetime': 'datetime',
        'start_appointment_datetime': 'datetime',
        'end_appointment_datetime': 'datetime',
        'appointment_salesperson_id': 'str',
        'page_number': 'int',
        'rows_per_page': 'int'
    }

    attribute_map = {
        'start_modified_datetime': 'start_modified_datetime',
        'start_appointment_datetime': 'start_appointment_datetime',
        'end_appointment_datetime': 'end_appointment_datetime',
        'appointment_salesperson_id': 'appointment_salesperson_id',
        'page_number': 'pageNumber',
        'rows_per_page': 'rowsPerPage'
    }

    def __init__(self, start_modified_datetime=None, start_appointment_datetime=None, end_appointment_datetime=None, appointment_salesperson_id=None, page_number=None, rows_per_page=None, local_vars_configuration=None):  # noqa: E501
        """InquiriesBindingModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start_modified_datetime = None
        self._start_appointment_datetime = None
        self._end_appointment_datetime = None
        self._appointment_salesperson_id = None
        self._page_number = None
        self._rows_per_page = None
        self.discriminator = None

        if start_modified_datetime is not None:
            self.start_modified_datetime = start_modified_datetime
        if start_appointment_datetime is not None:
            self.start_appointment_datetime = start_appointment_datetime
        if end_appointment_datetime is not None:
            self.end_appointment_datetime = end_appointment_datetime
        if appointment_salesperson_id is not None:
            self.appointment_salesperson_id = appointment_salesperson_id
        if page_number is not None:
            self.page_number = page_number
        if rows_per_page is not None:
            self.rows_per_page = rows_per_page

    @property
    def start_modified_datetime(self):
        """Gets the start_modified_datetime of this InquiriesBindingModel.  # noqa: E501


        :return: The start_modified_datetime of this InquiriesBindingModel.  # noqa: E501
        :rtype: datetime
        """
        return self._start_modified_datetime

    @start_modified_datetime.setter
    def start_modified_datetime(self, start_modified_datetime):
        """Sets the start_modified_datetime of this InquiriesBindingModel.


        :param start_modified_datetime: The start_modified_datetime of this InquiriesBindingModel.  # noqa: E501
        :type: datetime
        """

        self._start_modified_datetime = start_modified_datetime

    @property
    def start_appointment_datetime(self):
        """Gets the start_appointment_datetime of this InquiriesBindingModel.  # noqa: E501


        :return: The start_appointment_datetime of this InquiriesBindingModel.  # noqa: E501
        :rtype: datetime
        """
        return self._start_appointment_datetime

    @start_appointment_datetime.setter
    def start_appointment_datetime(self, start_appointment_datetime):
        """Sets the start_appointment_datetime of this InquiriesBindingModel.


        :param start_appointment_datetime: The start_appointment_datetime of this InquiriesBindingModel.  # noqa: E501
        :type: datetime
        """

        self._start_appointment_datetime = start_appointment_datetime

    @property
    def end_appointment_datetime(self):
        """Gets the end_appointment_datetime of this InquiriesBindingModel.  # noqa: E501


        :return: The end_appointment_datetime of this InquiriesBindingModel.  # noqa: E501
        :rtype: datetime
        """
        return self._end_appointment_datetime

    @end_appointment_datetime.setter
    def end_appointment_datetime(self, end_appointment_datetime):
        """Sets the end_appointment_datetime of this InquiriesBindingModel.


        :param end_appointment_datetime: The end_appointment_datetime of this InquiriesBindingModel.  # noqa: E501
        :type: datetime
        """

        self._end_appointment_datetime = end_appointment_datetime

    @property
    def appointment_salesperson_id(self):
        """Gets the appointment_salesperson_id of this InquiriesBindingModel.  # noqa: E501


        :return: The appointment_salesperson_id of this InquiriesBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._appointment_salesperson_id

    @appointment_salesperson_id.setter
    def appointment_salesperson_id(self, appointment_salesperson_id):
        """Sets the appointment_salesperson_id of this InquiriesBindingModel.


        :param appointment_salesperson_id: The appointment_salesperson_id of this InquiriesBindingModel.  # noqa: E501
        :type: str
        """

        self._appointment_salesperson_id = appointment_salesperson_id

    @property
    def page_number(self):
        """Gets the page_number of this InquiriesBindingModel.  # noqa: E501


        :return: The page_number of this InquiriesBindingModel.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this InquiriesBindingModel.


        :param page_number: The page_number of this InquiriesBindingModel.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def rows_per_page(self):
        """Gets the rows_per_page of this InquiriesBindingModel.  # noqa: E501


        :return: The rows_per_page of this InquiriesBindingModel.  # noqa: E501
        :rtype: int
        """
        return self._rows_per_page

    @rows_per_page.setter
    def rows_per_page(self, rows_per_page):
        """Sets the rows_per_page of this InquiriesBindingModel.


        :param rows_per_page: The rows_per_page of this InquiriesBindingModel.  # noqa: E501
        :type: int
        """

        self._rows_per_page = rows_per_page

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
        if not isinstance(other, InquiriesBindingModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InquiriesBindingModel):
            return True

        return self.to_dict() != other.to_dict()
