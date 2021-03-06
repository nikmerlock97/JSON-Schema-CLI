# openapi_client.LeadCapturesApi

All URIs are relative to *https://restapi1aws.marketsharpm.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lead_captures_get_contacts**](LeadCapturesApi.md#lead_captures_get_contacts) | **POST** /companies/{companyId}/leadcaptures/{applicationInternalName}/contacts/filter | List active contacts submitted by lead capture app since latest updated date/time
[**lead_captures_get_custom_lead_captures**](LeadCapturesApi.md#lead_captures_get_custom_lead_captures) | **GET** /companies/{companyId}/leadcaptures/custom | List all custom lead captures
[**lead_captures_get_global_lead_capture_contacts**](LeadCapturesApi.md#lead_captures_get_global_lead_capture_contacts) | **POST** /leadcaptures/{applicationInternalName}/contacts/filter | List global active contacts submitted by lead capture app since latest updated date/time
[**lead_captures_geti_capture_lead_captures**](LeadCapturesApi.md#lead_captures_geti_capture_lead_captures) | **GET** /companies/{companyId}/leadcaptures/iCapture | List iCapture lead captures


# **lead_captures_get_contacts**
> list[LeadCaptureContactResourceModel] lead_captures_get_contacts(company_id, application_internal_name, model)

List active contacts submitted by lead capture app since latest updated date/time

ContactId: The id representing the contact <br />  ThirdPartyId: Id generated by the third party. Populated via POST request to a MarketSharp lead capture endpoint and using thirdPartyId or MSM_thirdPartyId <br />  InquiryDateTime: Date/time of when the inquiry was created (this can be modified by the user <br />  AppointmentDate: Date/time of the appointment <br />  AppointmentSetDateTime: Date/time of when the appointment was set.  Time will always be 12:00am <br />  AppointmentResult: The current result of the appointment that was scheduled <br />  AppointmentPresenteDateTime: Populated when the current appointment result counts towards a presentation in MarketSharp.  Populates with appointment date/time <br />  AppointmentSoldDateTime: Populated when the current appointment result counts towards a sold appointment in MarketSharp.  Populates with appointment date/time <br />  ContractApprovedDateTime: Populated when the current contract status is marked Approved.  Returns contract date.  Time will always be 12:00am <br />  ContractStatus: Is a required field in MarketSharp <br />  LatestUpdatedTime: Takes the latest updated time between the inquiry, appointment, job or job product <br />

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://restapi1aws.marketsharpm.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://restapi1aws.marketsharpm.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LeadCapturesApi(api_client)
    company_id = 'company_id_example' # str | 
application_internal_name = 'application_internal_name_example' # str | 
model = openapi_client.LeadCaptureContactBindingModel() # LeadCaptureContactBindingModel | 

    try:
        # List active contacts submitted by lead capture app since latest updated date/time
        api_response = api_instance.lead_captures_get_contacts(company_id, application_internal_name, model)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LeadCapturesApi->lead_captures_get_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 
 **application_internal_name** | **str**|  | 
 **model** | [**LeadCaptureContactBindingModel**](LeadCaptureContactBindingModel.md)|  | 

### Return type

[**list[LeadCaptureContactResourceModel]**](LeadCaptureContactResourceModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lead_captures_get_custom_lead_captures**
> list[SimpleLeadCaptureResourceModel] lead_captures_get_custom_lead_captures(company_id)

List all custom lead captures

Returns a list of all of a company's custom lead captures

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://restapi1aws.marketsharpm.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://restapi1aws.marketsharpm.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LeadCapturesApi(api_client)
    company_id = 'company_id_example' # str | 

    try:
        # List all custom lead captures
        api_response = api_instance.lead_captures_get_custom_lead_captures(company_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LeadCapturesApi->lead_captures_get_custom_lead_captures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**list[SimpleLeadCaptureResourceModel]**](SimpleLeadCaptureResourceModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lead_captures_get_global_lead_capture_contacts**
> list[GlobalLeadCaptureContactResourceModel] lead_captures_get_global_lead_capture_contacts(application_internal_name, model)

List global active contacts submitted by lead capture app since latest updated date/time

CompanyId: The company id the contact is tied to <br />  ContactId: The id representing the contact <br />  ThirdPartyId: Id generated by the third party. Populated via POST request to a MarketSharp lead capture endpoint and using thirdPartyId or MSM_thirdPartyId <br />  InquiryDateTime: Date/time of when the inquiry was created (this can be modified by the user <br />  AppointmentDate: Date/time of the appointment <br />  AppointmentSetDateTime: Date/time of when the appointment was set.  Time will always be 12:00am <br />  AppointmentResult: The current result of the appointment that was scheduled <br />  AppointmentPresenteDateTime: Populated when the current appointment result counts towards a presentation in MarketSharp.  Populates with appointment date/time <br />  AppointmentSoldDateTime: Populated when the current appointment result counts towards a sold appointment in MarketSharp.  Populates with appointment date/time <br />  ContractApprovedDateTime: Populated when the current contract status is marked Approved.  Returns contract date.  Time will always be 12:00am <br />  ContractStatus: Is a required field in MarketSharp <br />  LatestUpdatedTime: Takes the latest updated time between the inquiry, appointment, job or job product <br />

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://restapi1aws.marketsharpm.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://restapi1aws.marketsharpm.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LeadCapturesApi(api_client)
    application_internal_name = 'application_internal_name_example' # str | 
model = openapi_client.GlobalLeadCaptureContactBindingModel() # GlobalLeadCaptureContactBindingModel | 

    try:
        # List global active contacts submitted by lead capture app since latest updated date/time
        api_response = api_instance.lead_captures_get_global_lead_capture_contacts(application_internal_name, model)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LeadCapturesApi->lead_captures_get_global_lead_capture_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_internal_name** | **str**|  | 
 **model** | [**GlobalLeadCaptureContactBindingModel**](GlobalLeadCaptureContactBindingModel.md)|  | 

### Return type

[**list[GlobalLeadCaptureContactResourceModel]**](GlobalLeadCaptureContactResourceModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lead_captures_geti_capture_lead_captures**
> list[LeadCaptureResourceModel] lead_captures_geti_capture_lead_captures(company_id)

List iCapture lead captures

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://restapi1aws.marketsharpm.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://restapi1aws.marketsharpm.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LeadCapturesApi(api_client)
    company_id = 'company_id_example' # str | 

    try:
        # List iCapture lead captures
        api_response = api_instance.lead_captures_geti_capture_lead_captures(company_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LeadCapturesApi->lead_captures_geti_capture_lead_captures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  | 

### Return type

[**list[LeadCaptureResourceModel]**](LeadCaptureResourceModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

