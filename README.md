# docker_for_vue_and_django

import osmapi
api = osmapi.OsmApi()
print(api.WayGet(5887599))

from OSMPythonTools.api import Api
api = Api()
way = api.query('way/5887599')
print(way.tag('building'))