"""Graph Class."""
import numpy as np
import copy
from collections import defaultdict


class Graph():
    """Graph class."""

    def __init__(self, nodes=None, edges=None, dist_between_nodes=None):
        """Initialize."""
        self.nodes = {}
        self.dist_between_nodes = {}

        if nodes is not None:
            for node in nodes:
                self.add_node(node)

        if edges is not None:
            for edge in edges:
                self.add_edge(edge)

        if dist_between_nodes is None:
            for k, values in self.nodes.items():
                dists = {}
                for value in values:
                    dists[value] = 1
                self.dist_between_nodes[k] = dists
        else:
            self.dist_between_nodes = copy.deepcopy(dist_between_nodes)

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

    def get_neighbours(self, node, unvisited_nodes=None):
        """Return nodes neigbours."""
        neighbours = self.nodes[node]
        if unvisited_nodes is not None:
            neighbours = list(set(neighbours).intersection(set(unvisited_nodes)))
        return neighbours

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

    def dijkstra(self, start, end):
        """Find the shortest path between two nodes using dijkstra."""
        unvisited_nodes = list(self.nodes.keys())
        node_distances = {}
        prev = defaultdict(list)
        for key in self.nodes.keys():
            if key != start:
                node_distances[key] = float('Inf')
            else:
                node_distances[key] = 0
        current_node = start
        while True:
            neighbours = self.get_neighbours(current_node, unvisited_nodes)
            for neighbour in neighbours:
                if self.dist_between_nodes[current_node][neighbour] + node_distances[current_node] <= node_distances[neighbour]:
                    node_distances[neighbour] = self.dist_between_nodes[current_node][neighbour] + node_distances[current_node]
                    prev[neighbour].append(current_node)
            unvisited_nodes.remove(current_node)
            if not unvisited_nodes.__contains__(end):
                path = []
                path2 = []
                path = self.backtrack_path(prev, path, end)                
                path2 = self.get_all_paths(prev, path2, end)
                return node_distances[end], path, path2[0:len(path2)//2], path2[len(path2)//2: ]
            unvisited_closest_nodes_distances = [v for k, v in node_distances.items() if unvisited_nodes.__contains__(k)]
            min_dist = min(unvisited_closest_nodes_distances)
            unvisited_closest_nodes = [k for k, v in node_distances.items() if v == min_dist and unvisited_nodes.__contains__(k)]
            current_node = np.random.choice(unvisited_closest_nodes)
    
    def backtrack_path(self, prev, path, u):
        """Recursive method to get the path from end to start in the shortest manner."""
        if prev.get(u, None) is None:
            path.insert(0, u)
            return path
        path.insert(0, u)
        u = np.random.choice(prev[u])
        return self.backtrack_path(prev, path, u)
    
    def get_all_paths(self, prev, path, u, paths=[]):
        if prev.get(u, None) is None:
            path.insert(0, u)
            return path
        neighbours = prev[u]
        for all in neighbours:
            path.insert(0, u)
            path = self.get_all_paths(prev, path, all, paths)
        return path
            




if __name__ == '__main__':
    g = Graph(['A', 'B', 'C', 'D'], [('A', 'B'), ('D', 'B'), ('A', 'C'), ('C', 'D')])
    path = g.find_path('C', 'B')
    shortest_path = g.dijkstra('C', 'B')
    print(shortest_path)
