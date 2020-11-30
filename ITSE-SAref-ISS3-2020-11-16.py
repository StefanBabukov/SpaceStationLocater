# CALCULATE AND TIMESTAMP THE ISS DISTANCE
# Samer Aref 2020-11-16
# ITSE ISS tracking project 3
import time
from datetime import datetime
from haversine import haversine, Unit
import requests

def returnSampleCoordinates():
    #this function returns only the coordinates from a list
    with open("ISS_city_lat_lon_data_list.txt","r") as cities:
        cityList = []
        coordinates = []
        for element in cities:
            #creating the cityList and coordinates list from the sample file
            element=element.strip(',')
            cityList.append(element)
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
    time.sleep(1)
    return now.strftime("%B %d, %Y %H:%M:%S")

def DistToRLC(location):
    richlandCollege = (32.9214, -96.7285)
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

def returnLocation():
    data = requests.get('http://api.open-notify.org/iss-now.json').json()
    location = (float(data['iss_position']['longitude']), float(data['iss_position']['latitude']))
    return location

returnLocation()
print("Enter '1' for simulated ISS position or '2' for using real time position data")
decision = int(input())
if decision == 1:
    coordinates = returnSampleCoordinates()
    for coordinate in coordinates:
        DistToRLC(coordinate)
elif decision == 2:
    print("***************************************************************************************************")
    print("DISTANCE TO RICHLAND COLLEGE IS CALCULATED USING REAL-TIME POSITION DATA, PRESS CTRL+C TO INTERRUPT")
    print("***************************************************************************************************")

    while 1:
        location = returnLocation()
        DistToRLC(location)
else:
    print("INVALID CHOICE, TRY AGAIN!")
#print(returnLocation())