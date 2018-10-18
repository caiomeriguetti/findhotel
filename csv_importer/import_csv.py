from dependency_injection import obj_graph
from geoservice.services import ImportService

importer = obj_graph.provide(ImportService)

print importer.import_csv('data_dump.csv')