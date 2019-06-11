class Node:

    def __init__(self, name, neighbours, cpt):
        self.name = name
        self.neighbours = neighbours
        self.cpt = cpt

    def __repr__(self):
        return str(self.name)

class Graph:

    def __init__(self, nodes):
        self.nodes = nodes

    def __repr__(self):
        s = ""
        for node in self.nodes:
            s += str(node) + '\n'

        return s

class CPT:

    def __init__(self, parents, probs):
        assert 2**len(parents) == len(probs), 'The number of probs should be 2**(number of parents)'
        self.table = {}
        self.parents = parents
        get_bin = lambda x, n: format(x, 'b').zfill(n)

        for i, prob in zip(range(2**len(parents)), probs):
            self.table[get_bin(i, len(parents))] = prob

    def __repr__(self):
        s = ""
        for key in self.table.keys():
            s += key + '|' + str(self.table[key]) + '\n'

        return s

if __name__ == '__main__':
    probs1 = [[0.2, 0.8]]
    cpt1 = CPT([], probs1)
    node1 = Node('Rain', [node2, node3], cpt1)

    probs2 = [[0.4, 0.6], [0.01, 0.99]]
    cpt2 = CPT([node1], probs2)
    node2 = Node('Sprinkler', [node1, node3], cpt2)

    probs3 = [[0, 1], [0.8, 0.2], [0.9, 0.1], [0.99, 0.01]]
    cpt3 = CPT([node2, node1], probs3)
    node3 = Node('Grass Wet', [node2, node1], cpt3)

    graph = Graph([node1, node2, node3])
