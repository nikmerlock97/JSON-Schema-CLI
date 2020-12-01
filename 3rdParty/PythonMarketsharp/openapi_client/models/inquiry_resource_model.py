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


class InquiryResourceModel(object):
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
        'inquiry_date_time': 'datetime',
        'taken_by': 'str',
        'division': 'str',
        'primary_lead_source': 'str',
        'secondary_lead_source': 'str',
        'canvasser': 'str',
        'telemarketer': 'str',
        'promoter': 'str',
        'notes': 'str',
        'product_interests': 'str',
        'lead_paint_year_home_built': 'str',
        'last_modified_date_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'contact_id': 'contactId',
        'inquiry_date_time': 'inquiryDateTime',
        'taken_by': 'takenBy',
        'division': 'division',
        'primary_lead_source': 'primaryLeadSource',
        'secondary_lead_source': 'secondaryLeadSource',
        'canvasser': 'canvasser',
        'telemarketer': 'telemarketer',
        'promoter': 'promoter',
        'notes': 'notes',
        'product_interests': 'productInterests',
        'lead_paint_year_home_built': 'leadPaintYearHomeBuilt',
        'last_modified_date_time': 'lastModifiedDateTime'
    }

    def __init__(self, id=None, contact_id=None, inquiry_date_time=None, taken_by=None, division=None, primary_lead_source=None, secondary_lead_source=None, canvasser=None, telemarketer=None, promoter=None, notes=None, product_interests=None, lead_paint_year_home_built=None, last_modified_date_time=None, local_vars_configuration=None):  # noqa: E501
        """InquiryResourceModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._contact_id = None
        self._inquiry_date_time = None
        self._taken_by = None
        self._division = None
        self._primary_lead_source = None
        self._secondary_lead_source = None
        self._canvasser = None
        self._telemarketer = None
        self._promoter = None
        self._notes = None
        self._product_interests = None
        self._lead_paint_year_home_built = None
        self._last_modified_date_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if contact_id is not None:
            self.contact_id = contact_id
        if inquiry_date_time is not None:
            self.inquiry_date_time = inquiry_date_time
        if taken_by is not None:
            self.taken_by = taken_by
        if division is not None:
            self.division = division
        if primary_lead_source is not None:
            self.primary_lead_source = primary_lead_source
        if secondary_lead_source is not None:
            self.secondary_lead_source = secondary_lead_source
        if canvasser is not None:
            self.canvasser = canvasser
        if telemarketer is not None:
            self.telemarketer = telemarketer
        if promoter is not None:
            self.promoter = promoter
        if notes is not None:
            self.notes = notes
        if product_interests is not None:
            self.product_interests = product_interests
        if lead_paint_year_home_built is not None:
            self.lead_paint_year_home_built = lead_paint_year_home_built
        if last_modified_date_time is not None:
            self.last_modified_date_time = last_modified_date_time

    @property
    def id(self):
        """Gets the id of this InquiryResourceModel.  # noqa: E501


        :return: The id of this InquiryResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InquiryResourceModel.


        :param id: The id of this InquiryResourceModel.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def contact_id(self):
        """Gets the contact_id of this InquiryResourceModel.  # noqa: E501


        :return: The contact_id of this InquiryResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this InquiryResourceModel.


        :param contact_id: The contact_id of this InquiryResourceModel.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def inquiry_date_time(self):
        """Gets the inquiry_date_time of this InquiryResourceModel.  # noqa: E501


        :return: The inquiry_date_time of this InquiryResourceModel.  # noqa: E501
        :rtype: datetime
        """
        return self._inquiry_date_time

    @inquiry_date_time.setter
    def inquiry_date_time(self, inquiry_date_time):
        """Sets the inquiry_date_time of this InquiryResourceModel.


        :param inquiry_date_time: The inquiry_date_time of this InquiryResourceModel.  # noqa: E501
        :type: datetime
        """

        self._inquiry_date_time = inquiry_date_time

    @property
    def taken_by(self):
        """Gets the taken_by of this InquiryResourceModel.  # noqa: E501


        :return: The taken_by of this InquiryResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._taken_by

    @taken_by.setter
    def taken_by(self, taken_by):
        """Sets the taken_by of this InquiryResourceModel.


        :param taken_by: The taken_by of this InquiryResourceModel.  # noqa: E501
        :type: str
        """

        self._taken_by = taken_by

    @property
    def division(self):
        """Gets the division of this InquiryResourceModel.  # noqa: E501


        :return: The division of this InquiryResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._division

    @division.setter
    def division(self, division):
        """Sets the division of this InquiryResourceModel.


        :param division: The division of this InquiryResourceModel.  # noqa: E501
        :type: str
        """

        self._division = division

    @property
    def primary_lead_source(self):
        """Gets the primary_lead_source of this InquiryResourceModel.  # noqa: E501


        :return: The primary_lead_source of this InquiryResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._primary_lead_source

    @primary_lead_source.setter
    def primary_lead_source(self, primary_lead_source):
        """Sets the primary_lead_source of this InquiryResourceModel.


        :param primary_lead_source: The primary_lead_source of this InquiryResourceModel.  # noqa: E501
        :type: str
        """

        self._primary_lead_source = primary_lead_source

    @property
    def secondary_lead_source(self):
        """Gets the secondary_lead_source of this InquiryResourceModel.  # noqa: E501


        :return: The secondary_lead_source of this InquiryResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._secondary_lead_source

    @secondary_lead_source.setter
    def secondary_lead_source(self, secondary_lead_source):
        """Sets the secondary_lead_source of this InquiryResourceModel.


        :param secondary_lead_source: The secondary_lead_source of this InquiryResourceModel.  # noqa: E501
        :type: str
        """

        self._secondary_lead_source = secondary_lead_source

    @property
    def canvasser(self):
        """Gets the canvasser of this InquiryResourceModel.  # noqa: E501


        :return: The canvasser of this InquiryResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._canvasser

    @canvasser.setter
    def canvasser(self, canvasser):
        """Sets the canvasser of this InquiryResourceModel.


        :param canvasser: The canvasser of this InquiryResourceModel.  # noqa: E501
        :type: str
        """

        self._canvasser = canvasser

    @property
    def telemarketer(self):
        """Gets the telemarketer of this InquiryResourceModel.  # noqa: E501


        :return: The telemarketer of this InquiryResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._telemarketer

    @telemarketer.setter
    def telemarketer(self, telemarketer):
        """Sets the telemarketer of this InquiryResourceModel.


        :param telemarketer: The telemarketer of this InquiryResourceModel.  # noqa: E501
        :type: str
        """

        self._telemarketer = telemarketer

    @property
    def promoter(self):
        """Gets the promoter of this InquiryResourceModel.  # noqa: E501


        :return: The promoter of this InquiryResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._promoter

    @promoter.setter
    def promoter(self, promoter):
        """Sets the promoter of this InquiryResourceModel.


        :param promoter: The promoter of this InquiryResourceModel.  # noqa: E501
        :type: str
        """

        self._promoter = promoter

    @property
    def notes(self):
        """Gets the notes of this InquiryResourceModel.  # noqa: E501


        :return: The notes of this InquiryResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this InquiryResourceModel.


        :param notes: The notes of this InquiryResourceModel.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def product_interests(self):
        """Gets the product_interests of this InquiryResourceModel.  # noqa: E501


        :return: The product_interests of this InquiryResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._product_interests

    @product_interests.setter
    def product_interests(self, product_interests):
        """Sets the product_interests of this InquiryResourceModel.


        :param product_interests: The product_interests of this InquiryResourceModel.  # noqa: E501
        :type: str
        """

        self._product_interests = product_interests

    @property
    def lead_paint_year_home_built(self):
        """Gets the lead_paint_year_home_built of this InquiryResourceModel.  # noqa: E501


        :return: The lead_paint_year_home_built of this InquiryResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._lead_paint_year_home_built

    @lead_paint_year_home_built.setter
    def lead_paint_year_home_built(self, lead_paint_year_home_built):
        """Sets the lead_paint_year_home_built of this InquiryResourceModel.


        :param lead_paint_year_home_built: The lead_paint_year_home_built of this InquiryResourceModel.  # noqa: E501
        :type: str
        """

        self._lead_paint_year_home_built = lead_paint_year_home_built

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this InquiryResourceModel.  # noqa: E501


        :return: The last_modified_date_time of this InquiryResourceModel.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this InquiryResourceModel.


        :param last_modified_date_time: The last_modified_date_time of this InquiryResourceModel.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date_time = last_modified_date_time

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
        if not isinstance(other, InquiryResourceModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InquiryResourceModel):
            return True

        return self.to_dict() != other.to_dict()
