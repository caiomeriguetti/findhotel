import json

import falcon

from geoservice.services import IpInfoService


class IpResource(object):

    def __init__(self):
        self.ip_service = IpInfoService()

    def on_get(self, req, resp, ip):

        info = self.ip_service.get_info(ip)

        if not info:
            resp.status = falcon.HTTP_404
        else:
            resp.set_header('Content-type', 'application/json')
            resp.body = json.dumps(info)
            resp.status = falcon.HTTP_200