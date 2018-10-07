class IpInfo(object):

    def __init__(self):

        self.ip = None
        self.country_code = None
        self.country_name = None
        self.city = None
        self.lat = None
        self.lng = None
        self.mystery_value = None

    def from_list(self, list_data):

        self.ip = list_data[0]
        self.country_code = list_data[1]
        self.country_name = list_data[2]
        self.city = list_data[3]
        self.lat = list_data[4]
        self.lng = list_data[5]
        self.mystery_value = list_data[6]

        return self

    def to_dict(self):
        return {
            'ip': self.ip,
            'country_code': self.country_code,
            'country_name': self.country_name,
            'city': self.city,
            'lat': self.lat,
            'lng': self.lng,
            'mystery_value': self.mystery_value
        }
