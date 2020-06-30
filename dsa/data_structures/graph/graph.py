class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight = 1):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self._adjacency_list = {}


    def add_vertex(self, value):
        vertex = Vertex(value)

        self._adjacency_list[vertex] = []

        return vertex

    def add_edge(self, start, end, weight=1):

        if start not in self._adjacency_list:
            raise KeyError('Start Vertex not in graph')

        if end not in self._adjacency_list:
            raise KeyError('End Vertex not in graph')

        edge = Edge(end, weight)

        adjacencies = self._adjacency_list[start]

        adjacencies.append(edge)


    def get_vertices(self):
        return list(self._adjacency_list.keys())

    def get_neighbors(self, vertex):
        return self._adjacency_list.get(vertex, None)

    def size(self):
        return len(self._adjacency_list)


if __name__ == "__main__":

    pass
