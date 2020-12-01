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


class EmployeePictureResourceModel(object):
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
        'employee_id': 'str',
        'employee_name': 'str',
        'employee_picture_file_name': 'str',
        'employee_picture_image_url': 'str'
    }

    attribute_map = {
        'employee_id': 'employeeId',
        'employee_name': 'employeeName',
        'employee_picture_file_name': 'employeePictureFileName',
        'employee_picture_image_url': 'employeePictureImageUrl'
    }

    def __init__(self, employee_id=None, employee_name=None, employee_picture_file_name=None, employee_picture_image_url=None, local_vars_configuration=None):  # noqa: E501
        """EmployeePictureResourceModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._employee_id = None
        self._employee_name = None
        self._employee_picture_file_name = None
        self._employee_picture_image_url = None
        self.discriminator = None

        if employee_id is not None:
            self.employee_id = employee_id
        if employee_name is not None:
            self.employee_name = employee_name
        if employee_picture_file_name is not None:
            self.employee_picture_file_name = employee_picture_file_name
        if employee_picture_image_url is not None:
            self.employee_picture_image_url = employee_picture_image_url

    @property
    def employee_id(self):
        """Gets the employee_id of this EmployeePictureResourceModel.  # noqa: E501

        Id of the employee.  # noqa: E501

        :return: The employee_id of this EmployeePictureResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this EmployeePictureResourceModel.

        Id of the employee.  # noqa: E501

        :param employee_id: The employee_id of this EmployeePictureResourceModel.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def employee_name(self):
        """Gets the employee_name of this EmployeePictureResourceModel.  # noqa: E501

        Name of the employee.  # noqa: E501

        :return: The employee_name of this EmployeePictureResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._employee_name

    @employee_name.setter
    def employee_name(self, employee_name):
        """Sets the employee_name of this EmployeePictureResourceModel.

        Name of the employee.  # noqa: E501

        :param employee_name: The employee_name of this EmployeePictureResourceModel.  # noqa: E501
        :type: str
        """

        self._employee_name = employee_name

    @property
    def employee_picture_file_name(self):
        """Gets the employee_picture_file_name of this EmployeePictureResourceModel.  # noqa: E501

        Employee picture file name.  # noqa: E501

        :return: The employee_picture_file_name of this EmployeePictureResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._employee_picture_file_name

    @employee_picture_file_name.setter
    def employee_picture_file_name(self, employee_picture_file_name):
        """Sets the employee_picture_file_name of this EmployeePictureResourceModel.

        Employee picture file name.  # noqa: E501

        :param employee_picture_file_name: The employee_picture_file_name of this EmployeePictureResourceModel.  # noqa: E501
        :type: str
        """

        self._employee_picture_file_name = employee_picture_file_name

    @property
    def employee_picture_image_url(self):
        """Gets the employee_picture_image_url of this EmployeePictureResourceModel.  # noqa: E501

        Full employee picture file path.  Need to call SetEmployeePictureImageUrl() method to populate.  # noqa: E501

        :return: The employee_picture_image_url of this EmployeePictureResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._employee_picture_image_url

    @employee_picture_image_url.setter
    def employee_picture_image_url(self, employee_picture_image_url):
        """Sets the employee_picture_image_url of this EmployeePictureResourceModel.

        Full employee picture file path.  Need to call SetEmployeePictureImageUrl() method to populate.  # noqa: E501

        :param employee_picture_image_url: The employee_picture_image_url of this EmployeePictureResourceModel.  # noqa: E501
        :type: str
        """

        self._employee_picture_image_url = employee_picture_image_url

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
        if not isinstance(other, EmployeePictureResourceModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmployeePictureResourceModel):
            return True

        return self.to_dict() != other.to_dict()