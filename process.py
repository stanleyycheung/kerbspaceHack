from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import pandas as pd
from math import sin, cos, sqrt, atan2, radians

# create an instance of the API class
api_instance = swagger_client.FeaturesControllerApi()
ocp_apim_subscription_key = 'c105fb930d5b43b09d8da802326651e9'  # str |
# str | viewport - a bounding box specified by two coordinates. First coordinate is bottom left second is top right. For example 51.31159579347505,-0.43013610839850003,51.73880216751415,0.25513610839837497 (optional)
viewport = '51.514784, -0.133652, 51.530104, -0.117755'

# bedford square
location = [51.519781, -0.129711]


def squareFinder(loc, radius):
    square_corners = ""
    longitude, latitude = loc[0], loc[1]
    d_vertical = (radius/1e3)/69
    d_horizontal = d_vertical / cos(d_vertical)
    square_corners += str(longitude - d_horizontal) + ", " + str(latitude - d_vertical) + ", " + str(longitude + d_horizontal) + ", " + str(latitude + d_vertical)

    return square_corners

def distanceFinder(loc1, loc2):
    # in meters
    R = 6373.0

    lat1, lon1 = loc1.split(',')
    lat2, lon2 = loc2.split(',')
    lat1, lon1 = radians(float(lat1)), radians(float(lon1))
    lat2, lon2 = radians(float(lat2)), radians(float(lon2))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c * 1e3

    return distance


def kerbSize():
    # for jj to write
    pass


def kerbCenter(coordList):
    n = len(coordList)

    if n % 2 != 0:
        return coordList[n//2+1]
    else:
        return



try:
    api_response = api_instance.get_features_by_viewport_using_get(
        ocp_apim_subscription_key, viewport=viewport)
except ApiException as e:
    print("Exception when calling FeaturesControllerApi->get_features_by_viewport_using_get: %s\n" % e)

accepted_parking = []
distances = []
for i in range(0, len(api_response.features)):
    kerb = api_response.features[i]
    regulations = kerb.properties['regulations']
    coord = kerb.geometry.coordinates
    for j in range(0, len(regulations)):
        if regulations[j]['rule']['payment']:
            if j == 0:
                accepted_parking.append(kerb)
                print(kerbCenter(coord))

        try:
            classes = regulations[j]['userClasses'][0]['classes'][0]
        except KeyError:
            pass
        if classes[0:2] == 'Di':
            if j == 0:
                accepted_parking.append(kerb)


# pprint(len(accepted_parking))
