class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight = 1):
        self.vertex = vertex
        self.weight = weight
        pass

class Graph:
    def __init__(self):
        self._adjacency_list = {}


        pass


    def add_vertex(self, value):
        vertex = Vertex(value)

        self._adjacency_list[vertex] = []

        return vertex

    def add_edge(self, start, end):
        pass

    def get_vertex(self, vertex):
        pass

    def get_neighbors(self):
        pass

    def size(self):
        pass


