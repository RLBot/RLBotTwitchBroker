# rlbot_twitch_broker_client.StaticApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**static_filename_get**](StaticApi.md#static_filename_get) | **GET** /static/{filename} | 

# **static_filename_get**
> str static_filename_get(filename)



### Example
```python
from __future__ import print_function
import time
import rlbot_twitch_broker_client
from rlbot_twitch_broker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rlbot_twitch_broker_client.StaticApi()
filename = 'filename_example' # str | 

try:
    api_response = api_instance.static_filename_get(filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StaticApi->static_filename_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

