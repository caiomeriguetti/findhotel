import pymongo

from db import client


class IpInfoRepository(object):

    def get_ip_info(self, ip):
        geodb = client().geodb
        info = geodb.ip_info.find_one({'ip': ip})

        if not info:
            return None

        info['_id'] = str(info['_id'])
        return info

    def create_indexes(self):
        geodb = client().geodb
        geodb.ip_info.create_index([('ip', pymongo.DESCENDING)], unique=True)

    def import_many(self, ip_info_list):
        geodb = client().geodb
        geodb.ip_info.insert_many(ip_info_list)
