# rlbot_twitch_broker_client.ChatApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_chat**](ChatApi.md#send_chat) | **POST** /chat | 

# **send_chat**
> ApiResponse send_chat(username, message)



### Example
```python
from __future__ import print_function
import time
import rlbot_twitch_broker_client
from rlbot_twitch_broker_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rlbot_twitch_broker_client.ChatApi()
username = 'username_example' # str | 
message = 'message_example' # str | 

try:
    api_response = api_instance.send_chat(username, message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->send_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **message** | **str**|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

