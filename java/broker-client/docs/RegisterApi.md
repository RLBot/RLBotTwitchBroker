# RegisterApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registerActionServer**](RegisterApi.md#registerActionServer) | **POST** /register/actionServer | 

<a name="registerActionServer"></a>
# **registerActionServer**
> ModelApiResponse registerActionServer(body)



### Example
```java
// Import classes:
//import org.rlbot.twitch.action.server.invoker.ApiException;
//import org.rlbot.twitch.action.server.api.RegisterApi;


RegisterApi apiInstance = new RegisterApi();
ActionServerRegistration body = new ActionServerRegistration(); // ActionServerRegistration | 
try {
    ModelApiResponse result = apiInstance.registerActionServer(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RegisterApi#registerActionServer");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActionServerRegistration**](ActionServerRegistration.md)|  |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

