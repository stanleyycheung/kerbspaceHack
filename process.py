from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesControllerApi()
ocp_apim_subscription_key = 'c105fb930d5b43b09d8da802326651e9'  # str |
# str | viewport - a bounding box specified by two coordinates. First coordinate is bottom left second is top right. For example 51.31159579347505,-0.43013610839850003,51.73880216751415,0.25513610839837497 (optional)
viewport = '51.538489, -0.143965, 51.540270, -0.142239'

try:
    # getFeaturesByViewport
    api_response = api_instance.get_features_by_viewport_using_get(
        ocp_apim_subscription_key, viewport=viewport)
    pprint(api_response.features[0])
    # print(len(api_response.features))
    # print(api_response)
except ApiException as e:
    print("Exception when calling FeaturesControllerApi->get_features_by_viewport_using_get: %s\n" % e)
