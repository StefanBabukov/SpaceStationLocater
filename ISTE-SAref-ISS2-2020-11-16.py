# CALCULATE AND TIMESTAMP THE ISS DISTANCE
# Samer Aref 2020-11-23
# ITSE ISS tracking project 3
import time
from datetime import datetime
from haversine import haversine, Unit

def returnCoordinates(cityList):
    #this function returns only the coordinates from a list
    coordinates = []
    for element in cityList:
        element = element.split(',')
        item = []
        item.append(float(element[2]))
        item.append(float(element[3]))
        # appending float values as per haversine requirements
        coordinates.append(item)
    return coordinates

def getLocalTime():
    # returning a timestamp
    now = datetime.now()
    print(now.strftime("%B %d, %Y %H:%M:%S"))
    time.sleep(1)
    return now.strftime("%B %d, %Y %H:%M:%S")

def DistToRLC(location):
    richlandCollege = (32.9214, -97.74306)
    distance = haversine(richlandCollege, location, unit=Unit.MILES)
    distance = ("{:0.1f}".format(distance))
    if location[0] < 0:
        relationToEquator = 'south'
    else:
        relationToEquator = 'north'
    if location[1] < 0:
        relationToMeridian = 'west'
    else:
        relationToMeridian = 'east'
    print("On ",getLocalTime(), " the ISS is ", distance, " miles from Richland college " \
    'ISS latitude = ', location[0], 'ISS longitude = ', location[1], ' the ISS is ', relationToEquator,
    ' of the Equator, and ', relationToMeridian, ' of the Prime Meridian')


with open("ISS_city_lat_lon_data_list.txt","r") as cities:
    cityList = []
    for element in cities:
        element=element.strip(',')
        cityList.append(element)
       # time.sleep(1)
coordinates = returnCoordinates(cityList)

for coordinate in coordinates:
    DistToRLC(coordinate)