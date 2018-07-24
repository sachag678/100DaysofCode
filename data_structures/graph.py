"""Graph Class."""
import numpy as np


class Graph():
    """Graph class."""

    def __init__(self, nodes=None, edges=None):
        """Initialize."""
        self.nodes = {}
        if nodes is not None:
            for node in nodes:
                self.add_node(node)

        if edges is not None:
            for edge in edges:
                self.add_edge(edge)

    def __repr__(self):
        """String representation."""
        s = str(self.nodes)
        return s

    def add_node(self, node):
        """Add node to the dict nodes."""
        self.nodes[node] = set()

    def add_edge(self, edge):
        """Add edge to each node."""
        self.nodes[edge[1]].add(edge[0])
        self.nodes[edge[0]].add(edge[1])

    def get_neighbours(self, node):
        """Return nodes neigbours."""
        return self.nodes[node]

    def find_path(self, start, end, path=[]):
        """Find the path between two nodes."""
        path.append(start)
        if start == end:
            return path
        neighbours = self.get_neighbours(start)
        for neighbour in neighbours:
            if neighbour not in path:
                new_path = self.find_path(neighbour, end, path)
                if new_path:
                    return new_path

        return None

if __name__ == '__main__':
    g = Graph(['A', 'B', 'C', 'D'], [('A', 'B'), ('A', 'D'), ('A', 'C'), ('C', 'D')])
    path = g.find_path('C', 'B')
