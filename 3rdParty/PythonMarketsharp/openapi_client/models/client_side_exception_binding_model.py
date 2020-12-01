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


class ClientSideExceptionBindingModel(object):
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
        'application_id': 'str',
        'company_id': 'str',
        'company_name': 'str',
        'employee_id': 'str',
        'username': 'str',
        'request_ip': 'str',
        'request_url': 'str',
        'exception_type': 'str',
        'exception_message': 'str',
        'exception_source': 'str',
        'stack_trace': 'str',
        'additional_info': 'str',
        'user_agent': 'str',
        'device_type': 'str',
        'browser': 'str',
        'browser_version': 'str'
    }

    attribute_map = {
        'application_id': 'applicationId',
        'company_id': 'companyId',
        'company_name': 'companyName',
        'employee_id': 'employeeId',
        'username': 'username',
        'request_ip': 'requestIP',
        'request_url': 'requestURL',
        'exception_type': 'exceptionType',
        'exception_message': 'exceptionMessage',
        'exception_source': 'exceptionSource',
        'stack_trace': 'stackTrace',
        'additional_info': 'additionalInfo',
        'user_agent': 'userAgent',
        'device_type': 'deviceType',
        'browser': 'browser',
        'browser_version': 'browserVersion'
    }

    def __init__(self, application_id=None, company_id=None, company_name=None, employee_id=None, username=None, request_ip=None, request_url=None, exception_type=None, exception_message=None, exception_source=None, stack_trace=None, additional_info=None, user_agent=None, device_type=None, browser=None, browser_version=None, local_vars_configuration=None):  # noqa: E501
        """ClientSideExceptionBindingModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_id = None
        self._company_id = None
        self._company_name = None
        self._employee_id = None
        self._username = None
        self._request_ip = None
        self._request_url = None
        self._exception_type = None
        self._exception_message = None
        self._exception_source = None
        self._stack_trace = None
        self._additional_info = None
        self._user_agent = None
        self._device_type = None
        self._browser = None
        self._browser_version = None
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if company_id is not None:
            self.company_id = company_id
        if company_name is not None:
            self.company_name = company_name
        if employee_id is not None:
            self.employee_id = employee_id
        if username is not None:
            self.username = username
        if request_ip is not None:
            self.request_ip = request_ip
        if request_url is not None:
            self.request_url = request_url
        if exception_type is not None:
            self.exception_type = exception_type
        if exception_message is not None:
            self.exception_message = exception_message
        if exception_source is not None:
            self.exception_source = exception_source
        if stack_trace is not None:
            self.stack_trace = stack_trace
        if additional_info is not None:
            self.additional_info = additional_info
        if user_agent is not None:
            self.user_agent = user_agent
        if device_type is not None:
            self.device_type = device_type
        if browser is not None:
            self.browser = browser
        if browser_version is not None:
            self.browser_version = browser_version

    @property
    def application_id(self):
        """Gets the application_id of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The application_id of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ClientSideExceptionBindingModel.


        :param application_id: The application_id of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def company_id(self):
        """Gets the company_id of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The company_id of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this ClientSideExceptionBindingModel.


        :param company_id: The company_id of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def company_name(self):
        """Gets the company_name of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The company_name of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ClientSideExceptionBindingModel.


        :param company_name: The company_name of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def employee_id(self):
        """Gets the employee_id of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The employee_id of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        """Sets the employee_id of this ClientSideExceptionBindingModel.


        :param employee_id: The employee_id of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._employee_id = employee_id

    @property
    def username(self):
        """Gets the username of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The username of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ClientSideExceptionBindingModel.


        :param username: The username of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def request_ip(self):
        """Gets the request_ip of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The request_ip of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._request_ip

    @request_ip.setter
    def request_ip(self, request_ip):
        """Sets the request_ip of this ClientSideExceptionBindingModel.


        :param request_ip: The request_ip of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._request_ip = request_ip

    @property
    def request_url(self):
        """Gets the request_url of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The request_url of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._request_url

    @request_url.setter
    def request_url(self, request_url):
        """Sets the request_url of this ClientSideExceptionBindingModel.


        :param request_url: The request_url of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._request_url = request_url

    @property
    def exception_type(self):
        """Gets the exception_type of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The exception_type of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._exception_type

    @exception_type.setter
    def exception_type(self, exception_type):
        """Sets the exception_type of this ClientSideExceptionBindingModel.


        :param exception_type: The exception_type of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._exception_type = exception_type

    @property
    def exception_message(self):
        """Gets the exception_message of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The exception_message of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._exception_message

    @exception_message.setter
    def exception_message(self, exception_message):
        """Sets the exception_message of this ClientSideExceptionBindingModel.


        :param exception_message: The exception_message of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._exception_message = exception_message

    @property
    def exception_source(self):
        """Gets the exception_source of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The exception_source of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._exception_source

    @exception_source.setter
    def exception_source(self, exception_source):
        """Sets the exception_source of this ClientSideExceptionBindingModel.


        :param exception_source: The exception_source of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._exception_source = exception_source

    @property
    def stack_trace(self):
        """Gets the stack_trace of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The stack_trace of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._stack_trace

    @stack_trace.setter
    def stack_trace(self, stack_trace):
        """Sets the stack_trace of this ClientSideExceptionBindingModel.


        :param stack_trace: The stack_trace of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._stack_trace = stack_trace

    @property
    def additional_info(self):
        """Gets the additional_info of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The additional_info of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this ClientSideExceptionBindingModel.


        :param additional_info: The additional_info of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def user_agent(self):
        """Gets the user_agent of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The user_agent of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this ClientSideExceptionBindingModel.


        :param user_agent: The user_agent of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

    @property
    def device_type(self):
        """Gets the device_type of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The device_type of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this ClientSideExceptionBindingModel.


        :param device_type: The device_type of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def browser(self):
        """Gets the browser of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The browser of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        """Sets the browser of this ClientSideExceptionBindingModel.


        :param browser: The browser of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._browser = browser

    @property
    def browser_version(self):
        """Gets the browser_version of this ClientSideExceptionBindingModel.  # noqa: E501


        :return: The browser_version of this ClientSideExceptionBindingModel.  # noqa: E501
        :rtype: str
        """
        return self._browser_version

    @browser_version.setter
    def browser_version(self, browser_version):
        """Sets the browser_version of this ClientSideExceptionBindingModel.


        :param browser_version: The browser_version of this ClientSideExceptionBindingModel.  # noqa: E501
        :type: str
        """

        self._browser_version = browser_version

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
        if not isinstance(other, ClientSideExceptionBindingModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClientSideExceptionBindingModel):
            return True

        return self.to_dict() != other.to_dict()