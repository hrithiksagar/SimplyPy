from math import radians, cos, sin, asin, sqrt
import json

def haversine(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """
    Calculate the great circle distance between two points on the 
    earth (specified in decimal degrees), returns the distance in
    kilometers.
    All arguments must be of equal length.
    :param lon1: longitude of first place
    :param lat1: latitude of first place
    :param lon2: longitude of second place
    :param lat2: latitude of second place
    :return: distance in kilometers between the two sets of coordinates
    """
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers
    return print("Distance: ",c * r)

def open_json(file_path: str):
    """
    Open a JSON file and return its content
    :param file_path: path to the JSON file
    :return: contents of te JSON file
    """
    with open(file_path, "r") as f:
        return json.load(f)
    
def write_json(file_path: str, data: str):
    """
    Write data to a JSON file
    :param file_path: Path to the file
    :param data: Data to write to the JSON file as a dictionary 
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

