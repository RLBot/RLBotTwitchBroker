# rlbot_twitch_broker_client.RegisterApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_action_server**](RegisterApi.md#register_action_server) | **POST** /register/actionServer | 

# **register_action_server**
> ApiResponse register_action_server(body)



### Example
```python
from __future__ import print_function
import time
import rlbot_twitch_broker_client
from rlbot_twitch_broker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rlbot_twitch_broker_client.RegisterApi()
body = rlbot_twitch_broker_client.ActionServerRegistration() # ActionServerRegistration | 

try:
    api_response = api_instance.register_action_server(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegisterApi->register_action_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActionServerRegistration**](ActionServerRegistration.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

