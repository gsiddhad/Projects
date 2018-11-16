# Algorthms GUI Project / tsort_graph.py
# Created on: 07-Nov-2018
# Author: Gourav Siddhad
# Topological Sort Graph

class T_Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        if key not in self.vertices:
            vertex = T_Vertex(key)
            self.vertices[key] = vertex

    def get_vertex(self, key):
        return self.vertices[key]

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, src_key, dest_key, weight = 1):
        if src_key not in self.vertices:
            self.add_vertex(src_key)
        if dest_key not in self.vertices:
            self.add_vertex(dest_key)
        if not self.does_edge_exist(src_key, dest_key):
            self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)

    def does_edge_exist(self, src_key, dest_key):
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])

    def __iter__(self):
        return iter(self.vertices.values())


class T_Vertex:

    def __init__(self, key):
        self.key = key
        self.points_to = {}

    def get_key(self):
        return self.key

    def add_neighbour(self, dest, weight):
        self.points_to[dest] = weight

    def get_neighbours(self):
        return self.points_to.keys()

    def get_weight(self, dest):
        return self.points_to[dest]

    def does_it_point_to(self, dest):
        return dest in self.points_to
