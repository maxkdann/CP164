"""
-------------------------------------------------------
[Graph]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-02-06"
-------------------------------------------------------
"""


class Edge:
    """
    Contains information about a graph edge.
    nodes: names of edge nodes stored in alphabetical order
    distance: arbitrary numeric distance between nodes
    """

    def __init__(self, nodes, distance):
        """
        -------------------------------------------------------
        Initializes an Edge object.
        Use: e = Edge(nodes, distance)
        -------------------------------------------------------
        Parameters:
            nodes - list of node names (list of str, len(nodes) == 2)
            distance - distance between start and end (int > 0)
        Returns:
            None
        -------------------------------------------------------
        """
        assert len(nodes) == 2, "Must have two node names"

        # Sort the node names into alphabetical order
        self.nodes = nodes
        self.distance = distance
        return

    def reverse(self):
        """
        -------------------------------------------------------
        Returns an Edge object with the start and end nodes reversed.
        Use: e2 = e1.reverse()
        -------------------------------------------------------
        Returns:
            new_edge - an Edge object with the node names swapped (Edge)
        -------------------------------------------------------
        """
        new_edge = Edge([self.nodes[1], self.nodes[0]], self.distance)
        return new_edge

    def __str__(self):
        """
        -------------------------------------------------------
        Returns a string representation of the edge.
        Use: s = str(e) or print(e)
        -------------------------------------------------------
        Returns:
            A string representation of the edge.
        -------------------------------------------------------
        """
        return "{} - {}: {}".format(self.nodes[0], self.nodes[1], self.distance)

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares two edges for equality of distance.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - another edge (Edge)
        Returns:
            Whether the distance of two edges are the same. (bool)
        -------------------------------------------------------
        """
        return self.distance == target.distance

    def __lt__(self, target):
        """
        -------------------------------------------------------
        Compares distance of two edges.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - another edge (Edge)
        Returns:
            True if distance of edge < distance of target,
                False otherwise. (bool)
        -------------------------------------------------------
        """
        return self.distance < target.distance

    def le(self, target):
        """
        -------------------------------------------------------
        Compares distance of two edges.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - another edge (Edge)
        Returns:
            True if distance of edge <= distance of target,
                False otherwise. (bool)
        -------------------------------------------------------
        """
        return self == target or self < target

    def start(self):
        """
        -------------------------------------------------------
        Returns name of starting node of edge.
        Use: edge = source.start()
        -------------------------------------------------------
        Returns:
            Name of starting node of edge (str)
        -------------------------------------------------------
        """
        return self.nodes[0]

    def end(self):
        """
        -------------------------------------------------------
        Returns name of ending node of edge.
        Use: edge = source.end()
        -------------------------------------------------------
        Returns:
            Name of ending node of edge (str)
        -------------------------------------------------------
        """
        return self.nodes[1]


class Graph:

    def __init__(self, edges):
        """
        -------------------------------------------------------
        Initializes a Graph object. Edges are stored in a dictionary
        keyed by node name.
        Use: g = Graph(edges)
        -------------------------------------------------------
        Parameters:
            edges - a list of Edge objects - each edge may appear
                only once in the list (list of Edge)
        Returns:
            None
        -------------------------------------------------------
        """
        self._nodes = dict()

        for edge in edges:
            # Store the edge with its start node name.
            node_name = edge.start()

            if node_name not in self._nodes:
                self._nodes[node_name] = list()
            self._nodes[node_name].append(edge)

            # Store the reversed edge with its start node name.
            r_edge = edge.reverse()
            node_name = r_edge.start()

            if node_name not in self._nodes:
                self._nodes[node_name] = list()

            self._nodes[node_name].append(r_edge)
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the graph.
        Use: n = len(g)
        -------------------------------------------------------
        Returns:
            The number of node names in graph (int)
        -------------------------------------------------------
        """
        return len(self._nodes)

    def node_names(self):
        """
        -------------------------------------------------------
        Returns a sorted list of graph node names.
        Use: names = g.node_names()
        -------------------------------------------------------
        Returns:
            a sorted list of all graph node names (list of str)
        -------------------------------------------------------
        """
        return sorted(self._nodes.keys())

    def edges_by_node(self, node_name):
        """
        -------------------------------------------------------
        Returns all the edges connected to node_name.
        Use: edges = g.edges_by_node(node_name)
        -------------------------------------------------------
        Parameters:
            node_name - a node name in the graph (str)
        Returns:
            edges - a list of all the edges staring at node_name (list of Edge)
        -------------------------------------------------------
        """
        edges = self._nodes[node_name]
        return edges


def graph_test(data):
    """
    -------------------------------------------------------
    Demonstrates use of Graph class. Prints
    all node names and edges in the graph
    Use: graph_test(data)
    -------------------------------------------------------
    Parameters:
        data - graph edges stored in tuples, where each tuple contains
            an edge [start, end], and distance (tuple of ([str, str], int))
    Returns:
        None
    -------------------------------------------------------
    """
    edges = []

    for d in data:
        edge = Edge(d[0], d[1])
        edges.append(edge)

    # Initialize the graph.
    graph = Graph(edges)

    node_names = graph.node_names()

    for node_name in node_names:
        print("Node: {}".format(node_name))
        node_edges = graph.edges_by_node(node_name)

        for edge in node_edges:
            print(edge)
        print()
    return

