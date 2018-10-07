from geoservice.services import ImportService


importer = ImportService()

print importer.import_csv('data_dump.csv')