from geolocationapi.resources import IpResource

main_routes = [
    ('/{ip}/info', IpResource())
]