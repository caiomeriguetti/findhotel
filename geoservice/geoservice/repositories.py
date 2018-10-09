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

    def create_ipinfo_from_list(self, list_data):
        return dict(
            ip = list_data[0],
            country_code = list_data[1],
            country_name = list_data[2],
            city = list_data[3],
            lat = list_data[4],
            lng = list_data[5],
            mystery_value = list_data[6]
        )
