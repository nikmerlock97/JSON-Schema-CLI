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


class JobLeadResourceModel(object):
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
        'job_unique_number': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'opportunity_name': 'str',
        'inquiry_date': 'datetime',
        'contact_created_date': 'datetime',
        'contact_updated_date': 'datetime',
        'lead_updated_date': 'datetime',
        'job_updated_date': 'datetime',
        'contact_id': 'str',
        'job_id': 'str',
        'inquiry_id': 'str',
        'job_site_address': 'AddressResourceModel',
        'state': 'OpportunityState'
    }

    attribute_map = {
        'job_unique_number': 'jobUniqueNumber',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'opportunity_name': 'opportunityName',
        'inquiry_date': 'inquiryDate',
        'contact_created_date': 'contactCreatedDate',
        'contact_updated_date': 'contactUpdatedDate',
        'lead_updated_date': 'leadUpdatedDate',
        'job_updated_date': 'jobUpdatedDate',
        'contact_id': 'contactId',
        'job_id': 'jobId',
        'inquiry_id': 'inquiryId',
        'job_site_address': 'jobSiteAddress',
        'state': 'state'
    }

    def __init__(self, job_unique_number=None, first_name=None, last_name=None, opportunity_name=None, inquiry_date=None, contact_created_date=None, contact_updated_date=None, lead_updated_date=None, job_updated_date=None, contact_id=None, job_id=None, inquiry_id=None, job_site_address=None, state=None, local_vars_configuration=None):  # noqa: E501
        """JobLeadResourceModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._job_unique_number = None
        self._first_name = None
        self._last_name = None
        self._opportunity_name = None
        self._inquiry_date = None
        self._contact_created_date = None
        self._contact_updated_date = None
        self._lead_updated_date = None
        self._job_updated_date = None
        self._contact_id = None
        self._job_id = None
        self._inquiry_id = None
        self._job_site_address = None
        self._state = None
        self.discriminator = None

        if job_unique_number is not None:
            self.job_unique_number = job_unique_number
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if opportunity_name is not None:
            self.opportunity_name = opportunity_name
        if inquiry_date is not None:
            self.inquiry_date = inquiry_date
        if contact_created_date is not None:
            self.contact_created_date = contact_created_date
        if contact_updated_date is not None:
            self.contact_updated_date = contact_updated_date
        if lead_updated_date is not None:
            self.lead_updated_date = lead_updated_date
        if job_updated_date is not None:
            self.job_updated_date = job_updated_date
        if contact_id is not None:
            self.contact_id = contact_id
        if job_id is not None:
            self.job_id = job_id
        if inquiry_id is not None:
            self.inquiry_id = inquiry_id
        if job_site_address is not None:
            self.job_site_address = job_site_address
        if state is not None:
            self.state = state

    @property
    def job_unique_number(self):
        """Gets the job_unique_number of this JobLeadResourceModel.  # noqa: E501

        Job unique number.  # noqa: E501

        :return: The job_unique_number of this JobLeadResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._job_unique_number

    @job_unique_number.setter
    def job_unique_number(self, job_unique_number):
        """Sets the job_unique_number of this JobLeadResourceModel.

        Job unique number.  # noqa: E501

        :param job_unique_number: The job_unique_number of this JobLeadResourceModel.  # noqa: E501
        :type: str
        """

        self._job_unique_number = job_unique_number

    @property
    def first_name(self):
        """Gets the first_name of this JobLeadResourceModel.  # noqa: E501

        First name of the contact lead.  # noqa: E501

        :return: The first_name of this JobLeadResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this JobLeadResourceModel.

        First name of the contact lead.  # noqa: E501

        :param first_name: The first_name of this JobLeadResourceModel.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this JobLeadResourceModel.  # noqa: E501

        Last name of the contact lead.  # noqa: E501

        :return: The last_name of this JobLeadResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this JobLeadResourceModel.

        Last name of the contact lead.  # noqa: E501

        :param last_name: The last_name of this JobLeadResourceModel.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def opportunity_name(self):
        """Gets the opportunity_name of this JobLeadResourceModel.  # noqa: E501

        Name of the opportunity or job.  # noqa: E501

        :return: The opportunity_name of this JobLeadResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._opportunity_name

    @opportunity_name.setter
    def opportunity_name(self, opportunity_name):
        """Sets the opportunity_name of this JobLeadResourceModel.

        Name of the opportunity or job.  # noqa: E501

        :param opportunity_name: The opportunity_name of this JobLeadResourceModel.  # noqa: E501
        :type: str
        """

        self._opportunity_name = opportunity_name

    @property
    def inquiry_date(self):
        """Gets the inquiry_date of this JobLeadResourceModel.  # noqa: E501

        The date that the Inquiry came in.  # noqa: E501

        :return: The inquiry_date of this JobLeadResourceModel.  # noqa: E501
        :rtype: datetime
        """
        return self._inquiry_date

    @inquiry_date.setter
    def inquiry_date(self, inquiry_date):
        """Sets the inquiry_date of this JobLeadResourceModel.

        The date that the Inquiry came in.  # noqa: E501

        :param inquiry_date: The inquiry_date of this JobLeadResourceModel.  # noqa: E501
        :type: datetime
        """

        self._inquiry_date = inquiry_date

    @property
    def contact_created_date(self):
        """Gets the contact_created_date of this JobLeadResourceModel.  # noqa: E501

        Date that the contact record was created.  # noqa: E501

        :return: The contact_created_date of this JobLeadResourceModel.  # noqa: E501
        :rtype: datetime
        """
        return self._contact_created_date

    @contact_created_date.setter
    def contact_created_date(self, contact_created_date):
        """Sets the contact_created_date of this JobLeadResourceModel.

        Date that the contact record was created.  # noqa: E501

        :param contact_created_date: The contact_created_date of this JobLeadResourceModel.  # noqa: E501
        :type: datetime
        """

        self._contact_created_date = contact_created_date

    @property
    def contact_updated_date(self):
        """Gets the contact_updated_date of this JobLeadResourceModel.  # noqa: E501

        Date that the contact record was last updated.  # noqa: E501

        :return: The contact_updated_date of this JobLeadResourceModel.  # noqa: E501
        :rtype: datetime
        """
        return self._contact_updated_date

    @contact_updated_date.setter
    def contact_updated_date(self, contact_updated_date):
        """Sets the contact_updated_date of this JobLeadResourceModel.

        Date that the contact record was last updated.  # noqa: E501

        :param contact_updated_date: The contact_updated_date of this JobLeadResourceModel.  # noqa: E501
        :type: datetime
        """

        self._contact_updated_date = contact_updated_date

    @property
    def lead_updated_date(self):
        """Gets the lead_updated_date of this JobLeadResourceModel.  # noqa: E501

        Date that the lead record was last updated.  # noqa: E501

        :return: The lead_updated_date of this JobLeadResourceModel.  # noqa: E501
        :rtype: datetime
        """
        return self._lead_updated_date

    @lead_updated_date.setter
    def lead_updated_date(self, lead_updated_date):
        """Sets the lead_updated_date of this JobLeadResourceModel.

        Date that the lead record was last updated.  # noqa: E501

        :param lead_updated_date: The lead_updated_date of this JobLeadResourceModel.  # noqa: E501
        :type: datetime
        """

        self._lead_updated_date = lead_updated_date

    @property
    def job_updated_date(self):
        """Gets the job_updated_date of this JobLeadResourceModel.  # noqa: E501

        Date that the job record was last updated.  # noqa: E501

        :return: The job_updated_date of this JobLeadResourceModel.  # noqa: E501
        :rtype: datetime
        """
        return self._job_updated_date

    @job_updated_date.setter
    def job_updated_date(self, job_updated_date):
        """Sets the job_updated_date of this JobLeadResourceModel.

        Date that the job record was last updated.  # noqa: E501

        :param job_updated_date: The job_updated_date of this JobLeadResourceModel.  # noqa: E501
        :type: datetime
        """

        self._job_updated_date = job_updated_date

    @property
    def contact_id(self):
        """Gets the contact_id of this JobLeadResourceModel.  # noqa: E501

        Contact id.  # noqa: E501

        :return: The contact_id of this JobLeadResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this JobLeadResourceModel.

        Contact id.  # noqa: E501

        :param contact_id: The contact_id of this JobLeadResourceModel.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def job_id(self):
        """Gets the job_id of this JobLeadResourceModel.  # noqa: E501

        Job id.  # noqa: E501

        :return: The job_id of this JobLeadResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobLeadResourceModel.

        Job id.  # noqa: E501

        :param job_id: The job_id of this JobLeadResourceModel.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def inquiry_id(self):
        """Gets the inquiry_id of this JobLeadResourceModel.  # noqa: E501

        Lead or inquiry id.  # noqa: E501

        :return: The inquiry_id of this JobLeadResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._inquiry_id

    @inquiry_id.setter
    def inquiry_id(self, inquiry_id):
        """Sets the inquiry_id of this JobLeadResourceModel.

        Lead or inquiry id.  # noqa: E501

        :param inquiry_id: The inquiry_id of this JobLeadResourceModel.  # noqa: E501
        :type: str
        """

        self._inquiry_id = inquiry_id

    @property
    def job_site_address(self):
        """Gets the job_site_address of this JobLeadResourceModel.  # noqa: E501


        :return: The job_site_address of this JobLeadResourceModel.  # noqa: E501
        :rtype: AddressResourceModel
        """
        return self._job_site_address

    @job_site_address.setter
    def job_site_address(self, job_site_address):
        """Sets the job_site_address of this JobLeadResourceModel.


        :param job_site_address: The job_site_address of this JobLeadResourceModel.  # noqa: E501
        :type: AddressResourceModel
        """

        self._job_site_address = job_site_address

    @property
    def state(self):
        """Gets the state of this JobLeadResourceModel.  # noqa: E501


        :return: The state of this JobLeadResourceModel.  # noqa: E501
        :rtype: OpportunityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this JobLeadResourceModel.


        :param state: The state of this JobLeadResourceModel.  # noqa: E501
        :type: OpportunityState
        """

        self._state = state

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
        if not isinstance(other, JobLeadResourceModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobLeadResourceModel):
            return True

        return self.to_dict() != other.to_dict()