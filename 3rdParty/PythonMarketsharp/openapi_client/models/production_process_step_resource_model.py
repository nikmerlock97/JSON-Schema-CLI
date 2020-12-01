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


class ProductionProcessStepResourceModel(object):
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
        'production_process_step_oid': 'str',
        'company_id': 'str',
        'assigned_to': 'str',
        'process_type_oid': 'str',
        'product_type_oid': 'str',
        'name': 'str',
        'order': 'int',
        'active_days': 'int',
        'enable_scheduler': 'bool',
        'enable_workorder': 'bool',
        'step_duration': 'int',
        'calculated_expected_state_date': 'int',
        'activity_process_oid': 'str'
    }

    attribute_map = {
        'production_process_step_oid': 'productionProcessStepOid',
        'company_id': 'companyId',
        'assigned_to': 'assignedTo',
        'process_type_oid': 'processTypeOid',
        'product_type_oid': 'productTypeOid',
        'name': 'name',
        'order': 'order',
        'active_days': 'activeDays',
        'enable_scheduler': 'enableScheduler',
        'enable_workorder': 'enableWorkorder',
        'step_duration': 'stepDuration',
        'calculated_expected_state_date': 'calculatedExpectedStateDate',
        'activity_process_oid': 'activityProcessOid'
    }

    def __init__(self, production_process_step_oid=None, company_id=None, assigned_to=None, process_type_oid=None, product_type_oid=None, name=None, order=None, active_days=None, enable_scheduler=None, enable_workorder=None, step_duration=None, calculated_expected_state_date=None, activity_process_oid=None, local_vars_configuration=None):  # noqa: E501
        """ProductionProcessStepResourceModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._production_process_step_oid = None
        self._company_id = None
        self._assigned_to = None
        self._process_type_oid = None
        self._product_type_oid = None
        self._name = None
        self._order = None
        self._active_days = None
        self._enable_scheduler = None
        self._enable_workorder = None
        self._step_duration = None
        self._calculated_expected_state_date = None
        self._activity_process_oid = None
        self.discriminator = None

        if production_process_step_oid is not None:
            self.production_process_step_oid = production_process_step_oid
        if company_id is not None:
            self.company_id = company_id
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if process_type_oid is not None:
            self.process_type_oid = process_type_oid
        if product_type_oid is not None:
            self.product_type_oid = product_type_oid
        if name is not None:
            self.name = name
        if order is not None:
            self.order = order
        if active_days is not None:
            self.active_days = active_days
        if enable_scheduler is not None:
            self.enable_scheduler = enable_scheduler
        if enable_workorder is not None:
            self.enable_workorder = enable_workorder
        if step_duration is not None:
            self.step_duration = step_duration
        if calculated_expected_state_date is not None:
            self.calculated_expected_state_date = calculated_expected_state_date
        if activity_process_oid is not None:
            self.activity_process_oid = activity_process_oid

    @property
    def production_process_step_oid(self):
        """Gets the production_process_step_oid of this ProductionProcessStepResourceModel.  # noqa: E501


        :return: The production_process_step_oid of this ProductionProcessStepResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._production_process_step_oid

    @production_process_step_oid.setter
    def production_process_step_oid(self, production_process_step_oid):
        """Sets the production_process_step_oid of this ProductionProcessStepResourceModel.


        :param production_process_step_oid: The production_process_step_oid of this ProductionProcessStepResourceModel.  # noqa: E501
        :type: str
        """

        self._production_process_step_oid = production_process_step_oid

    @property
    def company_id(self):
        """Gets the company_id of this ProductionProcessStepResourceModel.  # noqa: E501


        :return: The company_id of this ProductionProcessStepResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this ProductionProcessStepResourceModel.


        :param company_id: The company_id of this ProductionProcessStepResourceModel.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def assigned_to(self):
        """Gets the assigned_to of this ProductionProcessStepResourceModel.  # noqa: E501


        :return: The assigned_to of this ProductionProcessStepResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this ProductionProcessStepResourceModel.


        :param assigned_to: The assigned_to of this ProductionProcessStepResourceModel.  # noqa: E501
        :type: str
        """

        self._assigned_to = assigned_to

    @property
    def process_type_oid(self):
        """Gets the process_type_oid of this ProductionProcessStepResourceModel.  # noqa: E501


        :return: The process_type_oid of this ProductionProcessStepResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._process_type_oid

    @process_type_oid.setter
    def process_type_oid(self, process_type_oid):
        """Sets the process_type_oid of this ProductionProcessStepResourceModel.


        :param process_type_oid: The process_type_oid of this ProductionProcessStepResourceModel.  # noqa: E501
        :type: str
        """

        self._process_type_oid = process_type_oid

    @property
    def product_type_oid(self):
        """Gets the product_type_oid of this ProductionProcessStepResourceModel.  # noqa: E501


        :return: The product_type_oid of this ProductionProcessStepResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._product_type_oid

    @product_type_oid.setter
    def product_type_oid(self, product_type_oid):
        """Sets the product_type_oid of this ProductionProcessStepResourceModel.


        :param product_type_oid: The product_type_oid of this ProductionProcessStepResourceModel.  # noqa: E501
        :type: str
        """

        self._product_type_oid = product_type_oid

    @property
    def name(self):
        """Gets the name of this ProductionProcessStepResourceModel.  # noqa: E501


        :return: The name of this ProductionProcessStepResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductionProcessStepResourceModel.


        :param name: The name of this ProductionProcessStepResourceModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order(self):
        """Gets the order of this ProductionProcessStepResourceModel.  # noqa: E501


        :return: The order of this ProductionProcessStepResourceModel.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ProductionProcessStepResourceModel.


        :param order: The order of this ProductionProcessStepResourceModel.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def active_days(self):
        """Gets the active_days of this ProductionProcessStepResourceModel.  # noqa: E501


        :return: The active_days of this ProductionProcessStepResourceModel.  # noqa: E501
        :rtype: int
        """
        return self._active_days

    @active_days.setter
    def active_days(self, active_days):
        """Sets the active_days of this ProductionProcessStepResourceModel.


        :param active_days: The active_days of this ProductionProcessStepResourceModel.  # noqa: E501
        :type: int
        """

        self._active_days = active_days

    @property
    def enable_scheduler(self):
        """Gets the enable_scheduler of this ProductionProcessStepResourceModel.  # noqa: E501


        :return: The enable_scheduler of this ProductionProcessStepResourceModel.  # noqa: E501
        :rtype: bool
        """
        return self._enable_scheduler

    @enable_scheduler.setter
    def enable_scheduler(self, enable_scheduler):
        """Sets the enable_scheduler of this ProductionProcessStepResourceModel.


        :param enable_scheduler: The enable_scheduler of this ProductionProcessStepResourceModel.  # noqa: E501
        :type: bool
        """

        self._enable_scheduler = enable_scheduler

    @property
    def enable_workorder(self):
        """Gets the enable_workorder of this ProductionProcessStepResourceModel.  # noqa: E501


        :return: The enable_workorder of this ProductionProcessStepResourceModel.  # noqa: E501
        :rtype: bool
        """
        return self._enable_workorder

    @enable_workorder.setter
    def enable_workorder(self, enable_workorder):
        """Sets the enable_workorder of this ProductionProcessStepResourceModel.


        :param enable_workorder: The enable_workorder of this ProductionProcessStepResourceModel.  # noqa: E501
        :type: bool
        """

        self._enable_workorder = enable_workorder

    @property
    def step_duration(self):
        """Gets the step_duration of this ProductionProcessStepResourceModel.  # noqa: E501


        :return: The step_duration of this ProductionProcessStepResourceModel.  # noqa: E501
        :rtype: int
        """
        return self._step_duration

    @step_duration.setter
    def step_duration(self, step_duration):
        """Sets the step_duration of this ProductionProcessStepResourceModel.


        :param step_duration: The step_duration of this ProductionProcessStepResourceModel.  # noqa: E501
        :type: int
        """

        self._step_duration = step_duration

    @property
    def calculated_expected_state_date(self):
        """Gets the calculated_expected_state_date of this ProductionProcessStepResourceModel.  # noqa: E501


        :return: The calculated_expected_state_date of this ProductionProcessStepResourceModel.  # noqa: E501
        :rtype: int
        """
        return self._calculated_expected_state_date

    @calculated_expected_state_date.setter
    def calculated_expected_state_date(self, calculated_expected_state_date):
        """Sets the calculated_expected_state_date of this ProductionProcessStepResourceModel.


        :param calculated_expected_state_date: The calculated_expected_state_date of this ProductionProcessStepResourceModel.  # noqa: E501
        :type: int
        """

        self._calculated_expected_state_date = calculated_expected_state_date

    @property
    def activity_process_oid(self):
        """Gets the activity_process_oid of this ProductionProcessStepResourceModel.  # noqa: E501


        :return: The activity_process_oid of this ProductionProcessStepResourceModel.  # noqa: E501
        :rtype: str
        """
        return self._activity_process_oid

    @activity_process_oid.setter
    def activity_process_oid(self, activity_process_oid):
        """Sets the activity_process_oid of this ProductionProcessStepResourceModel.


        :param activity_process_oid: The activity_process_oid of this ProductionProcessStepResourceModel.  # noqa: E501
        :type: str
        """

        self._activity_process_oid = activity_process_oid

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
        if not isinstance(other, ProductionProcessStepResourceModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductionProcessStepResourceModel):
            return True

        return self.to_dict() != other.to_dict()