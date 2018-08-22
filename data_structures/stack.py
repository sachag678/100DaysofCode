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
    
    def __iter__(self):
        for i in range(len(self.stack)):
            yield self.stack[i]

    def __len__(self):
        return len(self.stack)

    def __repr__(self):
        s = '['
        for index, val in enumerate(self.stack):
            s += str(val)
            if index < len(self.stack) - 1:
                s += ','

        s += ']'
        return s
    
    def __getitem__(self, index):
        return self.stack[index]

class StackOfStacks(Stack):

    def __init__(self, max_len):
        self.stack = Stack()
        self.max_len = max_len
    
    def push(self, item):
        if self.stack.is_empty():
            new_stack = Stack()
        else:
            new_stack = self.stack.pop()
            
        if len(new_stack) > self.max_len:
            self.stack.push(new_stack)
            new_stack = Stack()

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

    def testStackOfStacks(self):

        sos = StackOfStacks(3)
        sos.push(1)
        sos.push(2)
        sos.push(3)
        sos.push(4)
        sos.push(5)

        self.assertEqual(str(sos),'[[1,2,3,4],[5]]')

        self.assertEqual(str(sos.peek()), '[5]')
        
        sos.pop()  # remove latest item - one stack remaining
        
        self.assertEqual(str(sos),'[[1,2,3,4]]')
        
        sos.pop()  # remove latest item - empty stack of stack

        self.assertEqual(sos.is_empty(), True)

        sos.push(1) # push item when stack is empty again

        self.assertEqual(str(sos), '[[1]]')
        

if __name__ == '__main__':
    unittest.main()

