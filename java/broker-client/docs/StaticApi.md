# StaticApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**staticFilenameGet**](StaticApi.md#staticFilenameGet) | **GET** /static/{filename} | 

<a name="staticFilenameGet"></a>
# **staticFilenameGet**
> String staticFilenameGet(filename)



### Example
```java
// Import classes:
//import org.rlbot.twitch.action.server.invoker.ApiException;
//import org.rlbot.twitch.action.server.api.StaticApi;


StaticApi apiInstance = new StaticApi();
String filename = "filename_example"; // String | 
try {
    String result = apiInstance.staticFilenameGet(filename);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling StaticApi#staticFilenameGet");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **String**|  |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

