from geoservice.repositories import IpInfoRepository
import time


class IpInfoService(object):

    def __init__(self):
        self.ip_repo = IpInfoRepository()

    def get_info(self, ip):
        return self.ip_repo.get_ip_info(ip)


class ImportService(object):

    def __init__(self):
        self.ip_repo = IpInfoRepository()

    def import_csv(self, file_path):

        start_time = time.time()

        self.ip_repo.create_indexes()

        buffer_size = 1000
        buffer = []

        imported = set()
        rejected = 0
        accepted = 0

        with open(file_path, 'r') as f:

            while 1:
                line = f.readline()

                if not line:
                    break

                line_parts = line.split(',')

                try:
                    ip_info = self.ip_repo.create_ipinfo_from_list(line_parts)

                    if ip_info['ip'] in imported:
                        rejected += 1
                        continue

                except:
                    rejected += 1
                    continue

                imported.add(ip_info['ip'])

                buffer.append(ip_info)

                accepted += 1

                if len(buffer) == buffer_size:
                    self.ip_repo.import_many(buffer)
                    buffer = []

            if len(buffer):
                self.ip_repo.import_many(buffer)

        end_time = time.time()
        time_spent = end_time - start_time

        return {
            'time_spent': time_spent,
            'rejected': rejected,
            'accepted': accepted
        }








