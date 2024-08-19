import requests
import math

URL_PATH = "https://nominatim.openstreetmap.org/search"

def get_lat_lon(location):
    PARAMS = {'q' : location, 'format': 'jsonv2'}
    headers = {
        'User-Agent': 'DistanceCalc/1.0'
    }

    r = requests.get(URL_PATH, params = PARAMS, headers = headers)
    data = r.json()

    latitude = float(data[0]['lat'])
    longitude = float(data[0]['lon'])

    return [latitude, longitude]
#end function

def calculate_distance(orig, dest): 
    #longgitude = 2nd part of returned coord array
    dlon = dest[1] - orig[1]  #dlon = lon2 - lon1
    # lat = 1st part at index 0 
    dlat = dest[0] - orig[0] #dlat = lat2 - lat1
    #a = (sin(dlat/2))^2 + cos(lat1) * cos(lat2) * (sin(dlon/2))^2
    a = (math.sin(math.radians(dlat/2)))**2 + \
         math.cos(math.radians(orig[0])) * \
         math.cos(math.radians(dest[0])) * \
         (math.sin(math.radians(dlon/2)))**2
    #c = 2 * atan2( sqrt(a), sqrt(1-a) )
    c = 2 * math.atan2(math.sqrt(a) , math.sqrt(1-a))
    R = 3961
    d = R * c
    
    return d
#end function

def selection_sort(array):
    # step 1: loop from the beginning of the array to the second to last item
    currentIndex = 0
    while (currentIndex < len(array) - 1):
        # step 2: save a copy of the currentIndex
        minIndex = currentIndex
        # step 3: loop through all indexes that proceed the currentIndex
        i = currentIndex + 1
        while (i < len(array)):
            # step 4:   if the value of the index of the current loop is less
            #           than the value of the item at minIndex, update minIndex
            #           with the new lowest value index
            if (array[i][0] < array[minIndex][0]):
                # update minIndex with the new lowest value index
                minIndex = i
            i += 1
        # step 5: if minIndex has been updated, swap the values at minIndex and currentIndex
        if (minIndex != currentIndex):
            temp = array[currentIndex]
            array[currentIndex] = array[minIndex]
            array[minIndex] = temp
        currentIndex += 1
#end function

def main():
    # The defult topgolf is in Mexico for some reason. Although, the assignment does not say the chosen places must be in New Mexico.
    place1 = "New Mexico Museum of Natural History & Science"
    place2 = "New Mexico Highlands University"
    place3 = "House of Eternal Return - Meow Wolf"
    place4 = "Topgolf"
    place5 = "Sunlake High school"
    place6 = "Cinco Ranch High school"
    loc1 = get_lat_lon(place1)
    loc2 = get_lat_lon(place2)
    loc3 = get_lat_lon(place3)
    loc4 = get_lat_lon(place4)
    loc5 = get_lat_lon(place5)
    loc6 = get_lat_lon(place6)
    dist1 = calculate_distance(loc1, loc2)
    dist2 = calculate_distance(loc1, loc3)
    dist3 = calculate_distance(loc1, loc4)
    dist4 = calculate_distance(loc1, loc5)
    dist5 = calculate_distance(loc1, loc6)
    distances = [(dist1, place2), (dist2, place3), (dist3, place4), (dist4, place5), (dist5, place6)]
    array = distances
    selection_sort(array)
    
    for i in array:
        print(i[1])
#end main 

if __name__ == "__main__":
    main()