from OSMPythonTools.nominatim import Nominatim
import folium
from openrouteservice import client
import pandas as pd
import json


def get_coordinates_by_city(place='Krasnodar, Russia'):
    nominatim = Nominatim()
    area_result = nominatim.query(place)
    area_result_json = area_result.toJSON()[0]
    area_lat = area_result_json['lat']
    area_lon = area_result_json['lon']
    return float(area_lon), float(area_lat)


def calc_central_point(coords):
    df = pd.DataFrame(coords, columns=['lon', 'lat'])
    return df["lon"].mean(), df["lat"].mean()


def draw_map(objects, coords):
    map1 = folium.Map(location=([coords[1], coords[0]]), zoom_start=12)

    for one_object in objects:
        points = one_object['geometry']['coordinates']
        folium.map.Marker(list(reversed(points)),
                          ).add_to(map1)

    map1.save('map_first.html')


coordinates = get_coordinates_by_city()
api_key = '5b3ce3597851110001cf6248652dfe598d584944bfd36172e4f6aeb3'
params_poi = {'request': 'pois',
              'geojson': {'type': 'point', 'coordinates': list(coordinates)},
              'sortby': 'distance',
              'buffer': 1500,
              'filter_category_ids': [280]}

clnt = client.Client(key=api_key)
all_places = clnt.places(**params_poi)[0]['features']
print('Have all places')
draw_map(all_places, coordinates)
print('Map saved as map_first.html')

with open('data.json', 'w') as fh:
    fh.writelines(json.dumps(all_places))
print('All places saved to data.json')
