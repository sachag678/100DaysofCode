"""Set structure."""
import numpy as np


class MySet():
    """Set structure."""

    def __init__(self):
        """Initialize."""
        self.set = []
        self.n = 0

    def __repr__(self):
        """Return String representation."""
        s = '{'
        for i in range(self.n):
            s += str(self.set[i])
            if i < self.n - 1:
                s += ', '
        s += '}'

        return s

    def __len__(self):
        """Return number of elements."""
        return self.n

    def add(self, elem):
        """Add element to the set if it doesn't exist."""
        if not self.set.__contains__(elem):
            self.set.append(elem)
            self.n += 1

    def remove(self, elem):
        """Remove an element from the set if it exist. Raises keyError if element doesn't exist."""
        self.set.remove(elem)

        self.n -= 1

    def discard(self, elem):
        """Remove element from the set if it's present."""
        if self.set.__contains__(elem):
            self.set.remove(elem)
            self.n -= 1

    def pop(self):
        """Remove and return an arbitrary element from the set. Raise Error if set is empty."""
        if self.n == 0:
            raise KeyError('Set empty.')
        self.n -= 1
        popped = self.set[np.random.randint(self.n)]
        self.set.remove(popped)
        return popped

    def clear(self):
        """Remove all elements."""
        self.set.clear()
        self.n = 0

    def xinset(self, elem):
        """Return true if element is in set."""
        pass

    def xnotinset(self, elem):
        """Return true if element is not in set."""
        pass

    def isdisjoint(self, other):
        """Return true if the intersection between other and self.set is zero."""
        pass

    def issubset(self, other):
        """Test if every element in myset is in other."""
        pass

    def issuperset(self, other):
        """Test if every element in other is in myset."""
        pass

    def union(self, other):
        """Return a new set with all the elements from myset and other."""
        pass

    def intersection(self, other):
        """Return a new set with the common elements between myset and other."""
        pass

    def difference(self, other):
        """Return a new set with the elements in myset that are not in other."""
        pass

    def symmetric_difference(self, other):
        """Return a new set with elements that are in either set or other but not in both."""
        pass

if __name__ == '__main__':
    myset = MySet()
    myset.add(2)
    myset.add(3)
    myset.add(3)
