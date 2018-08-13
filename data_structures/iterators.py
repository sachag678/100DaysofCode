"""Understand how iterators function."""
import unittest

class ReverseList():
    """Iterator that outputs the list in reverse."""

    def __init__(self, l=None):
        """Initialize."""
        self.index = 0
        self.l = l
        if l is not None:
            self.num_elements = len(l)
        else:
            self.num_elements = 0

    def __repr__(self):
        """String representation."""
        s = '['

        for index, val in enumerate(self.l):
            s += str(val)
            if index < self.num_elements - 1:
                s += ','
        
        s += ']'

        return s
        
    def __iter__(self):
        """Return the iter object."""
        return self

    def __next__(self):
        """Get the next value."""
        if self.index >= self.num_elements:
            raise StopIteration()
        else:
            val = self.l[self.num_elements - self.index - 1]
            self.index += 1
            return val

class ReverseListUsingGetIndexAsIterator():
    """Use the __getindex__ and __len__ as the iterators."""
    def __init__(self, l):
        """Initialize."""
        self.l = l
        self.num_elements = len(l)

    def __len__(self):
        """Return the number of elements."""
        return self.num_elements
    
    def __getitem__(self, index):
        """Returns the value from the list in reverse order."""
        if index >= self.num_elements:
            raise IndexError 
        return self.l[self.num_elements - index - 1]

class ReverseListUsingGenerator():
    """Use a generator to reverse the list."""
    def __init__(self, l):
        """Initialize."""
        self.l = l
        self.num_elements = len(l)

    def __iter__(self):
        for index in range(len(self.l)):
            yield self.l[self.num_elements - index - 1]

class TestIterators(unittest.TestCase):
    """Test the different iterators."""

    def testReverseList(self):
        """Test the reversing of the list using __iter__ and __next__."""
        self.assertResult(ReverseList([1, 2, 3, 4]))

    def testReverseListUsingGetIndexAsIterator(self):
        """Test the reversing of the list using the __len__ and __getindex__."""
        self.assertResult(ReverseListUsingGetIndexAsIterator([1, 2, 3, 4]))

    def testReverseListUsingGenerator(self):
        """Test the reversing of the list using generators."""
        self.assertResult(ReverseListUsingGenerator([1, 2, 3, 4]))

    def assertResult(self, result):
        """Common test function by iterating through the iter object and comparing
            to the standard reversed list.
        """
        self.assertAlmostEqual([val for val in result], [4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()