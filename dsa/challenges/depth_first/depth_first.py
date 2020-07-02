def depth_first(graph,vertex):
    '''function to run depth first traverse method in a graph'''
    result = []
    visited = set()
    result.append(vertex.value)
    visited.add(vertex.value)

    def traverse(graph, vertex):
        '''recursive function to travel inside of graph'''
        children = graph.get_neighbors(vertex)
        nonlocal visited
        if not children:
            return
        for child in children:
            if child.vertex.value not in visited:
                result.append(child.vertex.value)
                visited.add(child.vertex.value)
                traverse(graph, child.vertex)
        return

    traverse(graph,vertex)

    return result



