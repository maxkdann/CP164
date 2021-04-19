"""
-------------------------------------------------------
[functions]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-02-04"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
from Graph import Graph


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    if not source.is_empty():
        while not source.is_empty():        
            temp = source.remove()
            if temp < key:
                target1.insert(temp)             
            else:
                target2.insert(temp)
                
    return target1, target2


def pq_split_alt(source):
    """
    -------------------------------------------------------
    Splits a priority queue into two with values going to alternating
    priority queues. The source priority queue is empty when the method
    ends. The order of the values in source is preserved.
    Use: target1, target2 = pq_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
    Returns:
        target1 - a priority queue that contains alternating values
            from source (Priority_Queue)
        target2 - priority queue that contains  alternating values
            from source (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    left = True
    
    while not source.is_empty():
        if left:
            target1.insert(source.remove())
        else:
            target2.insert(source.remove())
        left = not left
    return target1, target2


def prims(graph, start_node):
    """
    -------------------------------------------------------
    Applies Prim's Algorithm to a graph.
    Use: edges, total = prims(graph, node)
    -------------------------------------------------------
    Parameters:
        graph - graph to evaluate (Graph)
        start_node - name of node to start evaluation from (str)
    Returns:
        edges - the list of the edges traversed (list of Edge)
        total - total distance of all edges traversed (int)
    -------------------------------------------------------
    """
    edges = []
    total = 0
    nodes_visited = []
    pq = Priority_Queue()
    current_node = start_node
    
    while len(nodes_visited) != len(graph):
        if current_node not in nodes_visited:
            nodes_visited.append(current_node)
        node_edges = graph.edges_by_node(current_node)
        for e in node_edges:
            if not(e.start() in nodes_visited and e.end() in nodes_visited):
                pq.insert(e)
        edge_to_add = pq.remove()
        already_in = edge_to_add.start() in nodes_visited and edge_to_add.end() in nodes_visited
        if not already_in:
            edges.append(edge_to_add)
            total+=edge_to_add.distance
        current_node = edge_to_add.end()

        
    return edges,total
