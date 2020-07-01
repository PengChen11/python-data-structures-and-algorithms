from dsa.challenges.breadth_first.breadth_first import *

def get_edge(graph, lists):
    '''function to find all edges between a list of vertices'''
    costs =0
    for i in range(1,len(lists)):
        start = graph.get_vertex(lists[i-1])
        end = graph.get_vertex(lists[i])
        if not start or not end:
            return [False, '$0']
        neighbors = graph.get_neighbors(start)
        is_neighbor = False
        for neighbor in neighbors:
            if end == neighbor.vertex:
                costs += neighbor.weight
                is_neighbor = True
                break
    if not is_neighbor:
        return [False, '$0']
    else:
        return [True, f'${costs}']



