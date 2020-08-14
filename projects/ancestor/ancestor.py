from util import Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    
    #initialize 
    q = Queue()
    current_node = starting_node
    relation = {}
    
    #loop through each parent,child pair
    for ancestor in ancestors: 
        #separate parent and child
        parent = ancestor[0]
        child = ancestor[1]

        #check if child is not already a key in relation cache
        if child not in relation:
            relation[child] = set()
        #add parent node to child key
        relation[child].add(parent)
    print("relateCache",relation)    

    #queue parent nodes
    if starting_node in relation:
        q.enqueue(relation[current_node])
        print('NodeParents',relation[current_node])
    else:
        return -1
    while q.size() > 0:
        #dequeue parent nodes
        related = q.dequeue()
        print("Dequeue",related)
        #grab lowest ID
        current_node = min(related)

        #check if node doesn't have parents
        #if it doesn't return the node itself
        if current_node not in relation:
            print("currentNode",current_node)
            return current_node
        #if the node has parents then queue the parent nodes
        else:
            q.enqueue(relation[current_node])
            print("newNodeParents",relation[current_node])


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors,6)

def earliest_ancestor2(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])

    # Do a BFS storing the path
    q = Queue()
    q.enqueue([starting_node])
    max_path_length = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = v
            max_path_length = len(path)
            for neighbor in graph.vertices[v]:
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    return earliest_ancestor