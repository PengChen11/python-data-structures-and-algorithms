from dsa.data_structures.graph.graph import Graph as Gra
from dsa.data_structures.stacks_and_queues.stacks_and_queues import Queue

class Graph(Gra):
    def breadth_first(self,vertex):
        output = []
        breadth = Queue()
        breadth.enqueue(vertex)
        visted = set()
        while not breadth.isEmpty():
            front = breadth.dequeue()
            output.append(front.value)
            visted.add(front.value)

            for neighbor in self.get_neighbors(front):
                if neighbor.vertex.value not in visted:
                    visted.add(neighbor.vertex.value)
                    breadth.enqueue(neighbor.vertex)
        return output


    def has_path(self, vertex_1, vertex_2):
        path = self.breadth_first(vertex_1)

        return vertex_2.value in path




if __name__ == "__main__":
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
    print(test.breadth_first(pandora))
