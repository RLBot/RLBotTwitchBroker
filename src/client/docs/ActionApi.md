# rlbot_action_client.ActionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**choose_action**](ActionApi.md#choose_action) | **POST** /action/choose | 
[**get_actions_currently_available**](ActionApi.md#get_actions_currently_available) | **GET** /action/currentlyAvailable | 

# **choose_action**
> ApiResponse choose_action(body)



### Example
```python
from __future__ import print_function
import time
import rlbot_action_client
from rlbot_action_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rlbot_action_client.ActionApi()
body = rlbot_action_client.ActionChoice() # ActionChoice | Action to choose

try:
    api_response = api_instance.choose_action(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionApi->choose_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActionChoice**](ActionChoice.md)| Action to choose | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_currently_available**
> AvailableActions get_actions_currently_available()



### Example
```python
from __future__ import print_function
import time
import rlbot_action_client
from rlbot_action_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rlbot_action_client.ActionApi()

try:
    api_response = api_instance.get_actions_currently_available()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActionApi->get_actions_currently_available: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AvailableActions**](AvailableActions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

