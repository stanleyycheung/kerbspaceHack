# swagger-client
API for serving kerbside assets. Data is served in CurbLR format https://github.com/sharedstreets/curblr

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.fordkerbhack.com](https://www.fordkerbhack.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesControllerApi(swagger_client.ApiClient(configuration))
ocp_apim_subscription_key = 'ocp_apim_subscription_key_example' # str | 
viewport = 'viewport_example' # str | viewport - a bounding box specified by two coordinates. First coordinate is bottom left second is top right. For example 51.31159579347505,-0.43013610839850003,51.73880216751415,0.25513610839837497 (optional)

try:
    # getFeaturesByViewport
    api_response = api_instance.get_features_by_viewport_using_get(ocp_apim_subscription_key, viewport=viewport)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesControllerApi->get_features_by_viewport_using_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://fordkerbhack.azure-api.net*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FeaturesControllerApi* | [**get_features_by_viewport_using_get**](docs/FeaturesControllerApi.md#get_features_by_viewport_using_get) | **GET** /features | getFeaturesByViewport
*HealthControllerApi* | [**message_using_get**](docs/HealthControllerApi.md#message_using_get) | **GET** /health | message


## Documentation For Models

 - [Authority](docs/Authority.md)
 - [CurbLR](docs/CurbLR.md)
 - [Feature](docs/Feature.md)
 - [Geometry](docs/Geometry.md)
 - [Manifest](docs/Manifest.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

tbd@ford.com
