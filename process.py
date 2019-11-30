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
viewport = '51.511317, -0.191195, 51.576160, -0.137312'


try:
    # getFeaturesByViewport
    api_response = api_instance.get_features_by_viewport_using_get(
        ocp_apim_subscription_key, viewport=viewport)

    for i in range(0, len(api_response.features)):
        # print(i)
        regulations = api_response.features[i].properties['regulations']
        for j in range(0, len(regulations)):
            try:
                classes = regulations[j]['userClasses'][0]['classes']
                pprint(classes[0])
                # if classes[0] == 'D':
                #     pprint(api_response.features[i].geometry.coordinates)
                # else:
                #     # pprint(classes)
                #     pass
            except KeyError:
                # pprint(regulations[j])
                pass
            #     try:
            #         userClasses = api_response.features[i].properties['regulations'][0]['userClasses'][0]['classes'][0]
            #     if userClasses[0:2] == 'Di':
            #         # print(userClasses)
            #         pass
            # except KeyError:
            #     pass

            # pprint(api_response.features[i].properties['regulations'][0]['userClasses'])
    # pprint(api_response.features[13].properties['regulations'])
    # if api_response.features[i].properties['regulations']
    #     pprint(api_response.features[i].properties['regulations'])
    # pprint(api_response.features[6].properties['regulations'])

    # pprint(api_response.features[i].properties['regulations'][1]['userClasses'][0]['classes'])
    # print(len(api_response.features))
    # print(api_response)
except ApiException as e:
    print("Exception when calling FeaturesControllerApi->get_features_by_viewport_using_get: %s\n" % e)

df = pd.read_csv('data/data.csv')
# print(df)
