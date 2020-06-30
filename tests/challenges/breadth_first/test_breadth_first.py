from dsa.challenges.breadth_first.breadth_first import Graph

def build_graph():
    test = Graph()
    pandora = test.add_vertex('Pandora')
    arendelle = test.add_vertex('Arendelle')
    metroville = test.add_vertex('Metroville')
    monstroplolis = test.add_vertex('Monstroplolis')
    narnia = test.add_vertex('Narnia')
    naboo = test.add_vertex('Naboo')
    test.add_edge(pandora,arendelle)
    test.add_edge(arendelle,metroville)
    test.add_edge(arendelle,monstroplolis)
    test.add_edge(metroville, narnia)
    test.add_edge(metroville, naboo)
    test.add_edge(metroville,monstroplolis)
    test.add_edge(monstroplolis,naboo)
    test.add_edge(narnia,naboo)
    return test

def test_breadth_first():
    test = build_graph()
    keys = test.get_vertices()
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']
    actural = test.breadth_first(keys[0])
    assert actural == expected


def test_has_path():
    test = build_graph()
    keys = test.get_vertices()
    pandora = keys[0]
    metroville = keys[2]

    assert test.has_path(pandora,metroville) == True

    earth = test.add_vertex('Earth')

    assert test.has_path(pandora, earth) == False

    test.add_edge(metroville, earth)

    assert test.has_path(pandora, earth) == True


