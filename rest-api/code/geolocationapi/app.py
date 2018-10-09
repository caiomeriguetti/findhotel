# -*- coding: utf-8 -*-
import falcon

from geolocationapi.routes import main_routes


class GeolocationApi(falcon.API):

    def __init__(self, *args, **kwargs):

        super(GeolocationApi, self).__init__(*args, **kwargs)

        for route in main_routes:
            self.add_route(route[0], route[1])


app = GeolocationApi()


