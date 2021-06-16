from OSMPythonTools.nominatim import Nominatim
from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
import folium
from openrouteservice import client
import pandas as pd

def get_objects_by_query(place='Krasnodar, Russia', selector='"leisure"="park"'):
    nominatim = Nominatim()
    area_result = nominatim.query(place)
    areaId = area_result.areaId()
    area_result_json = area_result.toJSON()[0]
    area_lat = area_result_json['lat']
    area_lon = area_result_json['lon']

    overpass = Overpass()
    query = overpassQueryBuilder(area=areaId, elementType=['way', 'relation'], selector=selector, includeGeometry=True)
    result = overpass.query(query)

    return result.elements(), (float(area_lon), float(area_lat))

def calc_central_point(coords):
    df = pd.DataFrame(coords, columns=['lon', 'lat'])
    return df["lon"].mean(), df["lat"].mean()

def draw_map(objects, coords):
    map1 = folium.Map(location=([coords[1], coords[0]]), zoom_start=12)

    for one_object in objects:
        geometry = one_object.geometry()
        points = calc_central_point(geometry['coordinates'][0])
        name = one_object.tag('name')
        if name != None:
            folium.map.Marker(list(reversed(points)),
                              popup=name,
                              ).add_to(map1)

    map1.save('map_first.html')

all_objects, coords = get_objects_by_query()
draw_map(all_objects, coords)

# https://github.com/GIScience/openrouteservice-examples/blob/master/python/Apartment_Search.ipynb
