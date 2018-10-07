# -*- coding: utf-8 -*-
import falcon

from geolocationapi.routes import main_routes
from falcon_extensions import Request


class GeolocationApi(falcon.API):

    def __init__(self, *args, **kwargs):

        super(GeolocationApi, self).__init__(request_type=Request, *args, **kwargs)

        for route in main_routes:
            self.add_route(route[0], route[1])


app = GeolocationApi()


