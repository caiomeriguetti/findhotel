import json

import falcon


class IpResource(object):

    def __init__(self, ip_info_service, import_service):
        self.ip_service = ip_info_service

        # just to illustrate dependency injection working
        self.import_service = import_service

    def on_get(self, req, resp, ip):

        info = self.ip_service.get_info(ip)

        if not info:
            resp.status = falcon.HTTP_404
        else:
            resp.set_header('Content-type', 'application/json')
            resp.body = json.dumps(info)
            resp.status = falcon.HTTP_200