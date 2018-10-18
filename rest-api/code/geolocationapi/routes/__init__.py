from geolocationapi.dependency_injection import obj_graph
from geolocationapi.resources import IpResource

main_routes = [
    ('/{ip}/info', obj_graph.provide(IpResource))
]