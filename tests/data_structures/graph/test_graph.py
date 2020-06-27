from dsa.data_structures.graph.graph import Graph, Vertex, Edge



def test_add_vertex():

    graph = Graph()

    expected = 'test'

    vertex = graph.add_vertex('test')

    actual = vertex.value

    assert actual == expected


def test_add_edge():

    graph = Graph()

    vertex_1 = graph.add_vertex('test1')

    vertex_2 = graph.add_vertex('test2')

    graph.add_edge(vertex_1, vertex_2)


def test_add_edge_interloper():

    graph = Graph()






