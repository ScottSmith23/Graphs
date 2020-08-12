from util import Queue

def earliest_ancestor(ancestors, starting_node):
    
    queue = Queue()
    current_node = starting_node
    relations = {}
    
    for ancestor in ancestors: 

        parent = ancestor[0]
        child = ancestor[1]

        if child not in relations:
            relations[child] = set()
        relations[child].add(parent)

    if starting_node in relations:
        queue.enqueue(relations[current_node])
    else:
        return -1

    while True:
        relations = queue.dequeue()
        current_node = min(relations)
        if current_node not in relations:
            return current_node
        else:
            queue.enqueue(relations[current_node])