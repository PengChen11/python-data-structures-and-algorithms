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

            for neighbor in self.get_neighbors(front):
                if neighbor.vertex not in visted:
                    visted.add(neighbor.vertex)
                    breadth.enqueue(neighbor.vertex)
        return output


    def has_path(self, vertex_1, vertex_2):
        path = self.breadth_first(vertex_1)

        return vertex_2.value in path




if __name__ == "__main__":
    pass
