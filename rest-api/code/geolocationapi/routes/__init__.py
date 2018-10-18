import pinject

from geolocationapi.resources import IpResource
from geoservice import services, repositories

obj_graph = pinject.new_object_graph(modules=[services, repositories])

main_routes = [
    ('/{ip}/info', obj_graph.provide(IpResource))
]