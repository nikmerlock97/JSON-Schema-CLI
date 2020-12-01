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


class AppointmentResourceModel(object):
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
        'contact_id': 'str',
        'inquiry_id': 'str',
        'appointment_date_time': 'datetime',
        'hide_in_scheduler': 'bool',
        'salesperson': 'str',
        'salesperson2': 'str',
        'type': 'str',
        'set_by': 'str',
        'date_issued': 'datetime',
        'result': 'str',
        'result_reason': 'str',
        'notes': 'str',
        'address': 'str',
        'address_line2': 'str',
        'city': 'str',
        'state': 'str',
        'zip': 'str',
        'directions': 'str',
        'last_modified_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'contact_id': 'contactId',
        'inquiry_id': 'inquiryId',
        'appointment_date_time': 'appointmentDateTime',
        'hide_in_scheduler': 'hideInScheduler',
        'salesperson': 'salesperson',
        'salesperson2': 'salesperson2',
        'type': 'type',
        'set_by': 'setBy',
        'date_issued': 'dateIssued',
        'result': 'result',
        'result_reason': 'resultReason',
        'notes': 'notes',
        'address': 'address',
        'address_line2': 'addressLine2',
        'city': 'city',
        'state': 'state',
        'zip': 'zip',
        'directions': 'directions',
        'last_modified_date': 'lastModifiedDate'
    }

    def __init__(self, id=None, contact_id=None, inquiry_id=None, appointment_date_time=None, hide_in_scheduler=None, salesperson=None, salesperson2=None, type=None, set_by=None, date_issued=None, result=None, result_reason=None, notes=None, address=None, address_line2=None, city=None, state=None, zip=None, directions=None, last_modified_date=None, local_vars_configuration=None):  # noqa: E501
        """AppointmentResourceModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._contact_id = None
        self._inquiry_id = None
        self._appointment_date_time = None
        self._hide_in_scheduler = None
        self._salesperson = None
        self._salesperson2 = None
        self._type = None
        self._set_by = None
        self._date_issued = None
        self._result = None
        self._result_reason = None
        self._notes = None
        self._address = None
        self._address_line2 = None
        self._city = None
        self._state = None
        self._zip = None
        self._directions = None
        self._last_modified_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if contact_id is not None:
            self.contact_id = contact_id
        if inquiry_id is not None:
            self.inquiry_id = inquiry_id
        if appointment_date_time is not None:
            self.appointment_date_time = appointment_date_time
        if hide_in_scheduler is not None:
            self.hide_in_scheduler = hide_in_scheduler
        if salesperson is not None:
            self.salesperson = salesperson
        if salesperson2 is not None:
            self.salesperson2 = salesperson2
        if type is not None:
            self.type = type
        if set_by is not None:
            self.set_by = set_by
        if date_issued is not None:
            self.date_issued = date_issued
        if result is not None:
            self.result = result
        if result_reason is not None:
            self.result_reason = result_reason
        if notes is not None:
            self.notes = notes
        if address is not None:
            self.address = address
        if address_line2 is not None:
            self.address_line2 = address_line2
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if zip is not None:
            self.zip = zip
        if directions is not None:
            self.directions = directions
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date

    @property
    def id(self):
        """Gets the id of this AppointmentResourceModel.  # noqa: E501


        :return: The id of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppointmentResourceModel.


        :param id: The id of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def contact_id(self):
        """Gets the contact_id of this AppointmentResourceModel.  # noqa: E501


        :return: The contact_id of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this AppointmentResourceModel.


        :param contact_id: The contact_id of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def inquiry_id(self):
        """Gets the inquiry_id of this AppointmentResourceModel.  # noqa: E501


        :return: The inquiry_id of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._inquiry_id

    @inquiry_id.setter
    def inquiry_id(self, inquiry_id):
        """Sets the inquiry_id of this AppointmentResourceModel.


        :param inquiry_id: The inquiry_id of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._inquiry_id = inquiry_id

    @property
    def appointment_date_time(self):
        """Gets the appointment_date_time of this AppointmentResourceModel.  # noqa: E501


        :return: The appointment_date_time of this AppointmentResourceModel.  # noqa: E501
        :rtype: datetime
        """
        return self._appointment_date_time

    @appointment_date_time.setter
    def appointment_date_time(self, appointment_date_time):
        """Sets the appointment_date_time of this AppointmentResourceModel.


        :param appointment_date_time: The appointment_date_time of this AppointmentResourceModel.  # noqa: E501
        :type: datetime
        """

        self._appointment_date_time = appointment_date_time

    @property
    def hide_in_scheduler(self):
        """Gets the hide_in_scheduler of this AppointmentResourceModel.  # noqa: E501


        :return: The hide_in_scheduler of this AppointmentResourceModel.  # noqa: E501
        :rtype: bool
        """
        return self._hide_in_scheduler

    @hide_in_scheduler.setter
    def hide_in_scheduler(self, hide_in_scheduler):
        """Sets the hide_in_scheduler of this AppointmentResourceModel.


        :param hide_in_scheduler: The hide_in_scheduler of this AppointmentResourceModel.  # noqa: E501
        :type: bool
        """

        self._hide_in_scheduler = hide_in_scheduler

    @property
    def salesperson(self):
        """Gets the salesperson of this AppointmentResourceModel.  # noqa: E501


        :return: The salesperson of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._salesperson

    @salesperson.setter
    def salesperson(self, salesperson):
        """Sets the salesperson of this AppointmentResourceModel.


        :param salesperson: The salesperson of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._salesperson = salesperson

    @property
    def salesperson2(self):
        """Gets the salesperson2 of this AppointmentResourceModel.  # noqa: E501


        :return: The salesperson2 of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._salesperson2

    @salesperson2.setter
    def salesperson2(self, salesperson2):
        """Sets the salesperson2 of this AppointmentResourceModel.


        :param salesperson2: The salesperson2 of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._salesperson2 = salesperson2

    @property
    def type(self):
        """Gets the type of this AppointmentResourceModel.  # noqa: E501


        :return: The type of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AppointmentResourceModel.


        :param type: The type of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def set_by(self):
        """Gets the set_by of this AppointmentResourceModel.  # noqa: E501


        :return: The set_by of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._set_by

    @set_by.setter
    def set_by(self, set_by):
        """Sets the set_by of this AppointmentResourceModel.


        :param set_by: The set_by of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._set_by = set_by

    @property
    def date_issued(self):
        """Gets the date_issued of this AppointmentResourceModel.  # noqa: E501


        :return: The date_issued of this AppointmentResourceModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_issued

    @date_issued.setter
    def date_issued(self, date_issued):
        """Sets the date_issued of this AppointmentResourceModel.


        :param date_issued: The date_issued of this AppointmentResourceModel.  # noqa: E501
        :type: datetime
        """

        self._date_issued = date_issued

    @property
    def result(self):
        """Gets the result of this AppointmentResourceModel.  # noqa: E501


        :return: The result of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this AppointmentResourceModel.


        :param result: The result of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def result_reason(self):
        """Gets the result_reason of this AppointmentResourceModel.  # noqa: E501


        :return: The result_reason of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._result_reason

    @result_reason.setter
    def result_reason(self, result_reason):
        """Sets the result_reason of this AppointmentResourceModel.


        :param result_reason: The result_reason of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._result_reason = result_reason

    @property
    def notes(self):
        """Gets the notes of this AppointmentResourceModel.  # noqa: E501


        :return: The notes of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this AppointmentResourceModel.


        :param notes: The notes of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def address(self):
        """Gets the address of this AppointmentResourceModel.  # noqa: E501


        :return: The address of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AppointmentResourceModel.


        :param address: The address of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def address_line2(self):
        """Gets the address_line2 of this AppointmentResourceModel.  # noqa: E501


        :return: The address_line2 of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this AppointmentResourceModel.


        :param address_line2: The address_line2 of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """Gets the city of this AppointmentResourceModel.  # noqa: E501


        :return: The city of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AppointmentResourceModel.


        :param city: The city of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this AppointmentResourceModel.  # noqa: E501


        :return: The state of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AppointmentResourceModel.


        :param state: The state of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this AppointmentResourceModel.  # noqa: E501


        :return: The zip of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this AppointmentResourceModel.


        :param zip: The zip of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def directions(self):
        """Gets the directions of this AppointmentResourceModel.  # noqa: E501


        :return: The directions of this AppointmentResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._directions

    @directions.setter
    def directions(self, directions):
        """Sets the directions of this AppointmentResourceModel.


        :param directions: The directions of this AppointmentResourceModel.  # noqa: E501
        :type: str
        """

        self._directions = directions

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this AppointmentResourceModel.  # noqa: E501


        :return: The last_modified_date of this AppointmentResourceModel.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this AppointmentResourceModel.


        :param last_modified_date: The last_modified_date of this AppointmentResourceModel.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date = last_modified_date

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
        if not isinstance(other, AppointmentResourceModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppointmentResourceModel):
            return True

        return self.to_dict() != other.to_dict()