"""Tree class - Based on Cracking the Coding Interview."""
import numpy as np
from queue import Queue

class BinaryTreeNode():
    """Node class is used to create Trees."""

    def __init__(self, name):
        """Initialize the node name and it's left, right nodes."""
        self.name = name
        self.marked = False

    def add_left(self, node):
        """Add a child node to the left."""
        self.left = node
    
    def add_right(self, node):
        """Add a child node to the right."""
        self.right = node
    
    def __repr__(self):
        """String representation."""
        queue = Queue()
        self.marked = True
        queue.add(self)
        s = ''
        counter = 1
        depth = 0

        while not queue.is_empty():
            r = queue.remove()
            s += str(r.name)
            s += '\t'
            
            if counter == 2**depth:
                s += '\n'
                counter = 0
                depth += 1

            counter += 1

            if r.left is not None:
                if r.left.marked == False:
                    r.left.marked = True
                    queue.add(r.left)
            if r.right is not None:
                if r.right.marked == False:
                    r.right.marked = True
                    queue.add(r.right)
        return s

def create_binary_search_tree(integer_list):
    """Create a binary search tree with minimal height given a sorted list of
        unique integer elements.

        Recall a binary search tree is a binary tree where all the elements on the left of 
        the current node are less than or equal to it and all the elements on the right of the
        current node are greater than it. 
        left elements <= current node < right elements.
    """
    if len(integer_list) == 0:
        return

    root_index = len(integer_list)//2
    root = BinaryTreeNode(integer_list[root_index])
    root.left = create_binary_search_tree(integer_list[:root_index])
    root.right = create_binary_search_tree(integer_list[root_index + 1:])
    return root
    
if __name__ == '__main__':
    sorted_list = [2, 4, 6, 8, 10, 20]
    print(create_binary_search_tree(sorted_list))