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
    assert len(graph.get_neighbors(vertex_1)) == 0
    graph.add_edge(vertex_1, vertex_2)
    assert len(graph.get_neighbors(vertex_1)) == 1


def test_get_vertices():

    graph = Graph()

    test1 = graph.add_vertex('test1')

    test2 = graph.add_vertex('test2')

    assert len(graph.get_vertices()) == 2


def test_get_neighbors():

    graph = Graph()

    test1 = graph.add_vertex('test1')

    test2 = graph.add_vertex('test2')

    graph.add_edge(test1, test2)

    neighbors = graph.get_neighbors(test1)

    assert len(neighbors) == 1

    neighbor = neighbors[0]

    assert neighbor.vertex.value == 'test2'

    assert neighbor.weight == 1


def test_get_size():

    graph = Graph()

    test1 = graph.add_vertex('test1')

    test2 = graph.add_vertex('test2')

    assert graph.size() == 2
