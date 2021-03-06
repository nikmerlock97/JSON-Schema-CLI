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


class ApptResultBindingModel(object):
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
        'appt_id': 'str',
        'result_id': 'str',
        'result_reason': 'str',
        'notes': 'str',
        'employee_id': 'str'
    }

    attribute_map = {
        'appt_id': 'appt_id',
        'result_id': 'result_id',
        'result_reason': 'result_reason',
        'notes': 'notes',
        'employee_id': 'employee_id'
    }

    def __init__(self, appt_id=None, result_id=None, result_reason=None, notes=None, employee_id=None, local_vars_configuration=None):  # noqa: E501
        """ApptResultBindingModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._appt_id = None
        self._result_id = None
        self._result_reason = None
        self._notes = None
        self._employee_id = None
        self.discriminator = None

        if appt_id is not None:
            self.appt_id = appt_id
        if result_id is not None:
            self.result_id = result_id
        if result_reason is not None:
            self.result_reason = result_reason
        if notes is not None:
            self.notes = notes
        if employee_id is not None:
            self.employee_id = employee_id

    @property
    def appt_id(self):
        """Gets the appt_id of this ApptResultBindingModel.  # noqa: E501


        :return: The appt_id of this ApptResultBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._appt_id

    @appt_id.setter
    def appt_id(self, appt_id):
        """Sets the appt_id of this ApptResultBindingModel.


        :param appt_id: The appt_id of this ApptResultBindingModel.  # noqa: E501
        :type: str
        """

        self._appt_id = appt_id

    @property
    def result_id(self):
        """Gets the result_id of this ApptResultBindingModel.  # noqa: E501


        :return: The result_id of this ApptResultBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        """Sets the result_id of this ApptResultBindingModel.


        :param result_id: The result_id of this ApptResultBindingModel.  # noqa: E501
        :type: str
        """

        self._result_id = result_id

    @property
    def result_reason(self):
        """Gets the result_reason of this ApptResultBindingModel.  # noqa: E501


        :return: The result_reason of this ApptResultBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._result_reason

    @result_reason.setter
    def result_reason(self, result_reason):
        """Sets the result_reason of this ApptResultBindingModel.


        :param result_reason: The result_reason of this ApptResultBindingModel.  # noqa: E501
        :type: str
        """

        self._result_reason = result_reason

    @property
    def notes(self):
        """Gets the notes of this ApptResultBindingModel.  # noqa: E501


        :return: The notes of this ApptResultBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ApptResultBindingModel.


        :param notes: The notes of this ApptResultBindingModel.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def employee_id(self):
        """Gets the employee_id of this ApptResultBindingModel.  # noqa: E501


        :return: The employee_id of this ApptResultBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this ApptResultBindingModel.


        :param employee_id: The employee_id of this ApptResultBindingModel.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

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
        if not isinstance(other, ApptResultBindingModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApptResultBindingModel):
            return True

        return self.to_dict() != other.to_dict()
