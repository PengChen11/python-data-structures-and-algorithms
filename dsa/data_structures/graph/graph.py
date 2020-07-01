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

        edge_start = Edge(end, weight)

        adjacencies = self._adjacency_list[start]

        adjacencies.append(edge_start)

        edge_end = Edge(start, weight)

        adjacencies = self._adjacency_list[end]

        adjacencies.append(edge_end)


    def get_vertices(self):
        return list(self._adjacency_list.keys())

    def get_neighbors(self, vertex):
        return self._adjacency_list.get(vertex, None)

    def size(self):
        return len(self._adjacency_list)


    def get_vertex(self, string_val):
        lists = self.get_vertices()
        for i in range(len(lists)):
            if lists[i].value == string_val:
                return lists[i]
        return None



if __name__ == "__main__":

    pass
