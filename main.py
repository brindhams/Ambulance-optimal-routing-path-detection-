#from helpers import Map, load_map_10, load_map_40, show_map
import math
import osmnx as ox
import networkx as nx
from geopy.geocoders import Nominatim
import folium
import webbrowser
from support import codeGenerator
import argparse
from operation_manager import RouteManager
from operation_manager import Route
from utils import *


def route_input():
    starting_point = input('Enter Source: ')
    ending_point = input('Enter Destination: ')
    print("Source: {0}\nDestination: {1}".format(starting_point, ending_point))
    return [starting_point, ending_point]

if __name__=='__main__':
    
    
    ri_op = route_input()
    lat1, long1 = get_lat_long_from_address(ri_op[0])
    lat2, long2 = get_lat_long_from_address(ri_op[1])
    
    response = get_directions_response(lat1, long1, lat2, long2)
    m = create_map(response)
    m.save('map.html')
    
    file_path = 'map.html'
    webbrowser.open(file_path, new=0)