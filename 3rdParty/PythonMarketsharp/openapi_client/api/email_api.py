# coding: utf-8

"""
    MarketSharp CRM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EmailApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def email_get_all_active_email_templates(self, companyid, **kwargs):  # noqa: E501
        """Get active email templates  # noqa: E501

        Return a list of valid email templates the User can select  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.email_get_all_active_email_templates(companyid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str companyid: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[KeyValueResourceModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.email_get_all_active_email_templates_with_http_info(companyid, **kwargs)  # noqa: E501

    def email_get_all_active_email_templates_with_http_info(self, companyid, **kwargs):  # noqa: E501
        """Get active email templates  # noqa: E501

        Return a list of valid email templates the User can select  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.email_get_all_active_email_templates_with_http_info(companyid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str companyid: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[KeyValueResourceModel], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'companyid'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method email_get_all_active_email_templates" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'companyid' is set
        if self.api_client.client_side_validation and ('companyid' not in local_var_params or  # noqa: E501
                                                        local_var_params['companyid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `companyid` when calling `email_get_all_active_email_templates`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'companyid' in local_var_params:
            path_params['companyid'] = local_var_params['companyid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyid}/email/templates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[KeyValueResourceModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def email_get_email_template_linked_events(self, template_id, companyid, **kwargs):  # noqa: E501
        """Get Email Template Dependencies  # noqa: E501

        This returns true or false for a given template whether it needs detals about a service orders, lead/inquiry and so on  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.email_get_email_template_linked_events(template_id, companyid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str template_id: (required)
        :param str companyid: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: EmailLinkedEventsResourceModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.email_get_email_template_linked_events_with_http_info(template_id, companyid, **kwargs)  # noqa: E501

    def email_get_email_template_linked_events_with_http_info(self, template_id, companyid, **kwargs):  # noqa: E501
        """Get Email Template Dependencies  # noqa: E501

        This returns true or false for a given template whether it needs detals about a service orders, lead/inquiry and so on  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.email_get_email_template_linked_events_with_http_info(template_id, companyid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str template_id: (required)
        :param str companyid: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(EmailLinkedEventsResourceModel, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'template_id',
            'companyid'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method email_get_email_template_linked_events" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'template_id' is set
        if self.api_client.client_side_validation and ('template_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['template_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `template_id` when calling `email_get_email_template_linked_events`")  # noqa: E501
        # verify the required parameter 'companyid' is set
        if self.api_client.client_side_validation and ('companyid' not in local_var_params or  # noqa: E501
                                                        local_var_params['companyid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `companyid` when calling `email_get_email_template_linked_events`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'template_id' in local_var_params:
            path_params['templateId'] = local_var_params['template_id']  # noqa: E501
        if 'companyid' in local_var_params:
            path_params['companyid'] = local_var_params['companyid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyid}/email/template/{templateId}/linkedevents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailLinkedEventsResourceModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
