#Reads the names and locations of all the stations in the file, and returns them as a dictionary.
def get_station_data(filename: str):
    station_coord = {}
    with open(filename) as file:
        for row in file:
            info = row.strip().split(";")
            if info[0] == "Longitude":
                continue
            station_coord[info[3]] = (float(info[0]), float(info[1]))
    return(station_coord)

#Works out the distance between two stations.
def distance(stations: dict, station1: str, station2: str):
    import math
    longitude1 = (stations[station1])[0]
    longitude2 = (stations[station2])[0]
    latitude1 = (stations[station1])[1]
    latitude2 = (stations[station2])[1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

#Works out the two stations on the list with the greatest distance from each other.
def greatest_distance(stations: dict):
    stasies = []
    max_dist = 0
    max_sta1 = ""
    max_sta2 = ""
    for station in stations:
        stasies.append(station)
    for i in range(len(stasies)):
        for j in range(len(stasies)):
            station1 = stasies[i]
            station2 = stasies[j]
            distance_calc = distance(stations, station1, station2)
            if distance_calc > max_dist:
                max_dist = distance_calc
                max_sta1 = station1
                max_sta2 = station2
    return max_sta1, max_sta2, max_dist
    