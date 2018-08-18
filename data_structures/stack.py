"""Contains Stack Questions from the Cracking the Coding Interview."""
import unittest
import sys

class MinStack():
    """A stack that keeps track of the minimum element and can retrieve it in O(1), and keep push()
    and pop() at O(1) as well.
        Q 3.2. 
    """
    def __init__(self):

        self.stack = []
        self.min_stack = []
    
    def min(self):
        """Returns the min_stack element."""
        if len(self.min_stack) == 0:
            return sys.maxsize
        return self.min_stack[-1]
    
    def __repr__(self):
        """String representation."""
        s = '['

        for index, val in enumerate(self.stack):
            s += str(val)
            if index < len(self.stack) - 1:
                s += ','
        
        s += ']'
        return s

    def pop(self):
        """Removes the last element added to the stack and returns it."""
        if len(self.stack) == 0:
            raise Exception('The stack is empty.')
        val = self.stack.pop()
        if val == self.min():
            self.min_stack.pop()
        return val
    
    def push(self, item):
        """Pushes an item to the top of the stack."""
        if item < self.min():
            self.min_stack.append(item)
        self.stack.append(item)
    
    def peak(self):
        """Gets the value of the most recently added element."""
        return self.stack[-1] 

    def is_empty(self):
        """Checks if the stack is empty or not."""
        return len(self.stack) == 0

class Stack():
    """Simple Stack Implementation."""
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0    

class StackOfStacks(Stack):

    def __init__(self):
        self.stack = Stack()
        new_stack = Stack()
        self.stack.push(new_stack)
    
    def push(self, item):
        new_stack = self.stack.pop()
        new_stack.push(item)
        self.stack.push(new_stack)

class TestStack(unittest.TestCase):
    
    def test_min_stack(self):
        min_stack = MinStack()

        min_stack.push(5)
        self.assertEqual(min_stack.min(), 5)

        min_stack.push(6)
        min_stack.push(3)
        min_stack.push(7)

        self.assertEqual(min_stack.min(), 3)

        min_stack.pop()
        self.assertEqual(min_stack.min(), 3)

        min_stack.pop()
        self.assertEqual(min_stack.min(), 5)

if __name__ == '__main__':
    unittest.main()


