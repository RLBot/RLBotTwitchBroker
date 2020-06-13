# ChatApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sendChat**](ChatApi.md#sendChat) | **POST** /chat | 

<a name="sendChat"></a>
# **sendChat**
> ModelApiResponse sendChat(username, message)



### Example
```java
// Import classes:
//import org.rlbot.twitch.action.server.invoker.ApiException;
//import org.rlbot.twitch.action.server.api.ChatApi;


ChatApi apiInstance = new ChatApi();
String username = "username_example"; // String | 
String message = "message_example"; // String | 
try {
    ModelApiResponse result = apiInstance.sendChat(username, message);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling ChatApi#sendChat");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**|  |
 **message** | **String**|  |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

