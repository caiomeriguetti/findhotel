import pymongo

from db import client


class IpInfoRepository(object):

    def geodb(self):
        return client().geodb

    def get_ip_info(self, ip):

        info = self.geodb().ip_info.find_one({'ip': ip})

        if not info:
            return None

        info['_id'] = str(info['_id'])
        return info

    def create_indexes(self):
        self.geodb().ip_info.create_index([('ip', pymongo.DESCENDING)], unique=True)

    def import_many(self, ip_info_list):
        self.geodb().ip_info.insert_many(ip_info_list)

    def create_ipinfo_from_list(self, list_data):

        return dict(
            ip = list_data[0],
            country_code = list_data[1],
            country_name = list_data[2],
            city = list_data[3],
            lat = float(list_data[4]),
            lng = float(list_data[5]),
            mystery_value = int(list_data[6])
        )
