# PaymentGatewayApi

All URIs are relative to http://api.sandbox.dana.id for sandbox environment

Method | HTTP request | Description
------------- | ------------- | -------------
[**consult_pay**](PaymentGatewayApi.md#consult_pay) | **POST** /v1.0/payment-gateway/consult-pay.htm | Consult Pay API


# **consult_pay**
> consult_pay(consult_pay_request) -> ConsultPayResponse 

Consult Pay API

This API is used to consult the list of payment methods or payment channels that user has and used in certain transactions or orders

### Example
You have to set env variables below (for PRIVATE_KEY and PRIVATE_KEY_PATH you have to choose one)
* ORIGIN
* X_PARTNER_ID
* CHANNEL_ID
* PRIVATE_KEY
* PRIVATE_KEY_PATH
* ENV

```python
from dana_python.utils.snap_configuration import SnapConfiguration, AuthSettings, Env
from dana_python.payment_gateway.payment_gateway.models.consult_pay_request import ConsultPayRequest
from dana_python.payment_gateway.payment_gateway.models.consult_pay_response import ConsultPayResponse
from dana_python.api_client import ApiClient
from dana_python.rest import ApiException
from pprint import pprint

configuration = SnapConfiguration(
    api_key=AuthSettings(
        PRIVATE_KEY=os.environ.get("PRIVATE_KEY"),
        ORIGIN=os.environ.get("ORIGIN"),
        X_PARTNER_ID=os.environ.get("X_PARTNER_ID"),
        CHANNEL_ID=os.environ.get("CHANNEL_ID"),
        ENV=Env.SANDBOX
    )
)


with ApiClient(configuration) as api_client:
    api_instance = dana_python.payment_gateway.payment_gateway.PaymentGatewayApi(api_client)
    consult_pay_request = dana_python.payment_gateway.payment_gateway.ConsultPayRequest()

    try:
        api_response = api_instance.consult_pay(consult_pay_request)
        print("The response of PaymentGatewayApi->consult_pay:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentGatewayApi->consult_pay: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consult_pay_request** | [**ConsultPayRequest**](ConsultPayRequest.md)|  | 

### Return type

[**ConsultPayResponse**](ConsultPayResponse.md)

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment consultation request sent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

