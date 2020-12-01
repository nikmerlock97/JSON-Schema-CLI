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


class JobsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def jobs_get_jobs_and_leads(self, company_id, search_model, **kwargs):  # noqa: E501
        """Get jobs and leads.  # noqa: E501

        Lists job and lead information for the company passed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.jobs_get_jobs_and_leads(company_id, search_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str company_id: Database company Id. (required)
        :param SimpleDateSearchBindingModel search_model: Model containing search parameters. numberOfRecords specifies the number of records to be returned. Defaulted to 50 if omitted.              fromDate specifies the datetime from which to begin your search.  Will return all records for that datetime and after. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[JobLeadResourceModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.jobs_get_jobs_and_leads_with_http_info(company_id, search_model, **kwargs)  # noqa: E501

    def jobs_get_jobs_and_leads_with_http_info(self, company_id, search_model, **kwargs):  # noqa: E501
        """Get jobs and leads.  # noqa: E501

        Lists job and lead information for the company passed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.jobs_get_jobs_and_leads_with_http_info(company_id, search_model, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str company_id: Database company Id. (required)
        :param SimpleDateSearchBindingModel search_model: Model containing search parameters. numberOfRecords specifies the number of records to be returned. Defaulted to 50 if omitted.              fromDate specifies the datetime from which to begin your search.  Will return all records for that datetime and after. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[JobLeadResourceModel], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'company_id',
            'search_model'
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
                    " to method jobs_get_jobs_and_leads" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'company_id' is set
        if self.api_client.client_side_validation and ('company_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['company_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `company_id` when calling `jobs_get_jobs_and_leads`")  # noqa: E501
        # verify the required parameter 'search_model' is set
        if self.api_client.client_side_validation and ('search_model' not in local_var_params or  # noqa: E501
                                                        local_var_params['search_model'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `search_model` when calling `jobs_get_jobs_and_leads`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'company_id' in local_var_params:
            path_params['companyId'] = local_var_params['company_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'search_model' in local_var_params:
            body_params = local_var_params['search_model']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyId}/jobs/opportunities', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JobLeadResourceModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def jobs_search_jobs(self, companyid, job, **kwargs):  # noqa: E501
        """Quickfind - Job Search  # noqa: E501

        This is the job search used by the quickfind. Employee Id required in the bearer token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.jobs_search_jobs(companyid, job, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str companyid: (required)
        :param JobSearchBindingModel job: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.jobs_search_jobs_with_http_info(companyid, job, **kwargs)  # noqa: E501

    def jobs_search_jobs_with_http_info(self, companyid, job, **kwargs):  # noqa: E501
        """Quickfind - Job Search  # noqa: E501

        This is the job search used by the quickfind. Employee Id required in the bearer token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.jobs_search_jobs_with_http_info(companyid, job, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str companyid: (required)
        :param JobSearchBindingModel job: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'companyid',
            'job'
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
                    " to method jobs_search_jobs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'companyid' is set
        if self.api_client.client_side_validation and ('companyid' not in local_var_params or  # noqa: E501
                                                        local_var_params['companyid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `companyid` when calling `jobs_search_jobs`")  # noqa: E501
        # verify the required parameter 'job' is set
        if self.api_client.client_side_validation and ('job' not in local_var_params or  # noqa: E501
                                                        local_var_params['job'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job` when calling `jobs_search_jobs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'companyid' in local_var_params:
            path_params['companyid'] = local_var_params['companyid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'job' in local_var_params:
            body_params = local_var_params['job']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/companies/{companyid}/jobs/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def jobs_search_jobs_0(self, job, **kwargs):  # noqa: E501
        """jobs_search_jobs_0  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.jobs_search_jobs_0(job, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param JobSearchBindingModel job: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.jobs_search_jobs_0_with_http_info(job, **kwargs)  # noqa: E501

    def jobs_search_jobs_0_with_http_info(self, job, **kwargs):  # noqa: E501
        """jobs_search_jobs_0  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.jobs_search_jobs_0_with_http_info(job, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param JobSearchBindingModel job: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'job'
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
                    " to method jobs_search_jobs_0" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'job' is set
        if self.api_client.client_side_validation and ('job' not in local_var_params or  # noqa: E501
                                                        local_var_params['job'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job` when calling `jobs_search_jobs_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'job' in local_var_params:
            body_params = local_var_params['job']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/jobs/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
