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


class Reminder(object):
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
        'activity_id': 'str',
        'contact_id': 'str',
        'activity_type': 'str',
        'activity_reference_name': 'str',
        'due_date': 'datetime',
        'contact_first_name': 'str',
        'contact_last_name': 'str',
        'contact_type': 'str',
        'past_due': 'bool',
        'created_date': 'datetime',
        'viewed': 'bool'
    }

    attribute_map = {
        'activity_id': 'activityId',
        'contact_id': 'contactId',
        'activity_type': 'activityType',
        'activity_reference_name': 'activityReferenceName',
        'due_date': 'dueDate',
        'contact_first_name': 'contactFirstName',
        'contact_last_name': 'contactLastName',
        'contact_type': 'contactType',
        'past_due': 'pastDue',
        'created_date': 'createdDate',
        'viewed': 'viewed'
    }

    def __init__(self, activity_id=None, contact_id=None, activity_type=None, activity_reference_name=None, due_date=None, contact_first_name=None, contact_last_name=None, contact_type=None, past_due=None, created_date=None, viewed=None, local_vars_configuration=None):  # noqa: E501
        """Reminder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._activity_id = None
        self._contact_id = None
        self._activity_type = None
        self._activity_reference_name = None
        self._due_date = None
        self._contact_first_name = None
        self._contact_last_name = None
        self._contact_type = None
        self._past_due = None
        self._created_date = None
        self._viewed = None
        self.discriminator = None

        if activity_id is not None:
            self.activity_id = activity_id
        if contact_id is not None:
            self.contact_id = contact_id
        if activity_type is not None:
            self.activity_type = activity_type
        if activity_reference_name is not None:
            self.activity_reference_name = activity_reference_name
        if due_date is not None:
            self.due_date = due_date
        if contact_first_name is not None:
            self.contact_first_name = contact_first_name
        if contact_last_name is not None:
            self.contact_last_name = contact_last_name
        if contact_type is not None:
            self.contact_type = contact_type
        if past_due is not None:
            self.past_due = past_due
        if created_date is not None:
            self.created_date = created_date
        if viewed is not None:
            self.viewed = viewed

    @property
    def activity_id(self):
        """Gets the activity_id of this Reminder.  # noqa: E501


        :return: The activity_id of this Reminder.  # noqa: E501
        :rtype: str
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this Reminder.


        :param activity_id: The activity_id of this Reminder.  # noqa: E501
        :type: str
        """

        self._activity_id = activity_id

    @property
    def contact_id(self):
        """Gets the contact_id of this Reminder.  # noqa: E501


        :return: The contact_id of this Reminder.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this Reminder.


        :param contact_id: The contact_id of this Reminder.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def activity_type(self):
        """Gets the activity_type of this Reminder.  # noqa: E501


        :return: The activity_type of this Reminder.  # noqa: E501
        :rtype: str
        """
        return self._activity_type

    @activity_type.setter
    def activity_type(self, activity_type):
        """Sets the activity_type of this Reminder.


        :param activity_type: The activity_type of this Reminder.  # noqa: E501
        :type: str
        """

        self._activity_type = activity_type

    @property
    def activity_reference_name(self):
        """Gets the activity_reference_name of this Reminder.  # noqa: E501


        :return: The activity_reference_name of this Reminder.  # noqa: E501
        :rtype: str
        """
        return self._activity_reference_name

    @activity_reference_name.setter
    def activity_reference_name(self, activity_reference_name):
        """Sets the activity_reference_name of this Reminder.


        :param activity_reference_name: The activity_reference_name of this Reminder.  # noqa: E501
        :type: str
        """

        self._activity_reference_name = activity_reference_name

    @property
    def due_date(self):
        """Gets the due_date of this Reminder.  # noqa: E501


        :return: The due_date of this Reminder.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Reminder.


        :param due_date: The due_date of this Reminder.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def contact_first_name(self):
        """Gets the contact_first_name of this Reminder.  # noqa: E501


        :return: The contact_first_name of this Reminder.  # noqa: E501
        :rtype: str
        """
        return self._contact_first_name

    @contact_first_name.setter
    def contact_first_name(self, contact_first_name):
        """Sets the contact_first_name of this Reminder.


        :param contact_first_name: The contact_first_name of this Reminder.  # noqa: E501
        :type: str
        """

        self._contact_first_name = contact_first_name

    @property
    def contact_last_name(self):
        """Gets the contact_last_name of this Reminder.  # noqa: E501


        :return: The contact_last_name of this Reminder.  # noqa: E501
        :rtype: str
        """
        return self._contact_last_name

    @contact_last_name.setter
    def contact_last_name(self, contact_last_name):
        """Sets the contact_last_name of this Reminder.


        :param contact_last_name: The contact_last_name of this Reminder.  # noqa: E501
        :type: str
        """

        self._contact_last_name = contact_last_name

    @property
    def contact_type(self):
        """Gets the contact_type of this Reminder.  # noqa: E501


        :return: The contact_type of this Reminder.  # noqa: E501
        :rtype: str
        """
        return self._contact_type

    @contact_type.setter
    def contact_type(self, contact_type):
        """Sets the contact_type of this Reminder.


        :param contact_type: The contact_type of this Reminder.  # noqa: E501
        :type: str
        """

        self._contact_type = contact_type

    @property
    def past_due(self):
        """Gets the past_due of this Reminder.  # noqa: E501


        :return: The past_due of this Reminder.  # noqa: E501
        :rtype: bool
        """
        return self._past_due

    @past_due.setter
    def past_due(self, past_due):
        """Sets the past_due of this Reminder.


        :param past_due: The past_due of this Reminder.  # noqa: E501
        :type: bool
        """

        self._past_due = past_due

    @property
    def created_date(self):
        """Gets the created_date of this Reminder.  # noqa: E501


        :return: The created_date of this Reminder.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Reminder.


        :param created_date: The created_date of this Reminder.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def viewed(self):
        """Gets the viewed of this Reminder.  # noqa: E501


        :return: The viewed of this Reminder.  # noqa: E501
        :rtype: bool
        """
        return self._viewed

    @viewed.setter
    def viewed(self, viewed):
        """Sets the viewed of this Reminder.


        :param viewed: The viewed of this Reminder.  # noqa: E501
        :type: bool
        """

        self._viewed = viewed

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
        if not isinstance(other, Reminder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Reminder):
            return True

        return self.to_dict() != other.to_dict()