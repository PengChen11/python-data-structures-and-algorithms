from dsa.data_structures.graph.graph import Graph
from dsa.challenges.depth_first.depth_first import depth_first

class Test_Builder:
    def __init__(self):
        self.maps = Graph()
        self.A = self.maps.add_vertex('A')
        self.B = self.maps.add_vertex('B')
        self.C = self.maps.add_vertex('C')
        self.D = self.maps.add_vertex('D')
        self.E = self.maps.add_vertex('E')
        self.F = self.maps.add_vertex('F')
        self.G = self.maps.add_vertex('G')
        self.H = self.maps.add_vertex('H')

    def build_edges(self):
        self.maps.add_edge(self.A, self.B)
        self.maps.add_edge(self.A, self.D)
        self.maps.add_edge(self.B, self.C)
        self.maps.add_edge(self.B, self.D)
        self.maps.add_edge(self.C, self.G)
        self.maps.add_edge(self.D, self.E)
        self.maps.add_edge(self.D, self.H)
        self.maps.add_edge(self.D, self.F)
        self.maps.add_edge(self.F, self.H)
        return self.maps

def test_depth_first():
    test = Test_Builder()
    maps = test.build_edges()
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    actural = depth_first(maps, test.A)
    assert expected == actural

