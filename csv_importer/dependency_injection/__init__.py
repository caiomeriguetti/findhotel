import pinject

from geoservice import services, repositories

obj_graph = pinject.new_object_graph(modules=[services, repositories])