from dsa.challenges.get_edge.get_edge import *

class Test_Builder:
    def __init__(self):
        self.maps = Graph()
        self.pandora = self.maps.add_vertex('Pandora')
        self.arendelle = self.maps.add_vertex('Arendelle')
        self.metroville = self.maps.add_vertex('Metroville')
        self.monstroplolis = self.maps.add_vertex('Monstroplolis')
        self.narnia = self.maps.add_vertex('Narnia')
        self.naboo = self.maps.add_vertex('Naboo')

    def build_edges(self):
        self.maps.add_edge(self.pandora,self.arendelle, 150)
        self.maps.add_edge(self.pandora, self.metroville, 82)
        self.maps.add_edge(self.arendelle,self.metroville, 99)
        self.maps.add_edge(self.arendelle,self.monstroplolis, 42)
        self.maps.add_edge(self.metroville, self.narnia, 37)
        self.maps.add_edge(self.metroville, self.naboo, 26)
        self.maps.add_edge(self.metroville,self.monstroplolis, 105)
        self.maps.add_edge(self.monstroplolis,self.naboo, 73)
        self.maps.add_edge(self.narnia,self.naboo, 250)
        return self.maps


def test_edge_1():
    test = Test_Builder()
    maps = test.build_edges()
    expected = [True, '$82']
    actural = get_edge(maps, ['Metroville', 'Pandora'])
    assert actural == expected


def test_edge_2():
    test = Test_Builder()
    maps = test.build_edges()
    expected = [True, '$115']
    actural = get_edge(maps, ['Arendelle', 'Monstroplolis', 'Naboo'])
    assert actural == expected


def test_edge_3():
    test = Test_Builder()
    maps = test.build_edges()
    expected = [False, '$0']
    actural = get_edge(maps, ['Naboo', 'Pandora'])
    assert actural == expected


def test_edge_4():
    test = Test_Builder()
    maps = test.build_edges()
    expected = [False, '$0']
    actural = get_edge(maps, ['Narnia', 'Arendelle', 'Naboo'])
    assert actural == expected
