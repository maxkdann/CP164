"""
-------------------------------------------------------
[t06]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-02-06"
-------------------------------------------------------
"""
from Graph import Graph
from functions import prims
from Graph import Edge


def main():
    
    data = (
    (['A', 'B'], 3), (['A', 'C'], 3), (['B', 'H'], 6), (['B', 'C'], 3),
    (['C', 'D'], 2), (['D', 'E'], 8), (['D', 'G'], 7), (['E', 'D'], 8),
    (['E', 'F'], 7), (['F', 'G'], 5),(['F', 'H'], 3),(['H', 'I'], 4))
    edges = []

    for d in data:
        edge = Edge(d[0], d[1])
        edges.append(edge)
    
    graph = Graph(edges)
    edges_returned,total = prims(graph, "E")
    for e in edges_returned:
        print(e)
    print("total: {}".format(total))
    
main()
