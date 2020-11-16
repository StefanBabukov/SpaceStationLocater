#Returning a list cities and their coordinates
with open("ISS_city_lat_lon_data_list.txt","r") as cities:
    cityList = []
    for element in cities:
        element=element.strip(',')
        cityList.append(element)
print(cityList)