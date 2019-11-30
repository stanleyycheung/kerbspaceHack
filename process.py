from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import pandas as pd

# create an instance of the API class
api_instance = swagger_client.FeaturesControllerApi()
ocp_apim_subscription_key = 'c105fb930d5b43b09d8da802326651e9'  # str |
# str | viewport - a bounding box specified by two coordinates. First coordinate is bottom left second is top right. For example 51.31159579347505,-0.43013610839850003,51.73880216751415,0.25513610839837497 (optional)
viewport = '51.535144, -0.147268, 51.544436, -0.137753'

try:
    # getFeaturesByViewport
    api_response = api_instance.get_features_by_viewport_using_get(
        ocp_apim_subscription_key, viewport=viewport)

    # for i in range(0, len(api_response.features)):
    #     print(i)
    #     pprint(api_response.features[i].properties['regulations'])
    pprint(api_response)
    # pprint(api_response.features[i].properties['regulations'][1]['userClasses'][0]['classes'])
    # print(len(api_response.features))
    # print(api_response)
except ApiException as e:
    print("Exception when calling FeaturesControllerApi->get_features_by_viewport_using_get: %s\n" % e)

df = pd.read_csv('data/data.csv')
# print(df)
