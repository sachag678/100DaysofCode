"""Set structure."""
import numpy as np


class MySet():
    """Set structure."""

    def __init__(self, input=None):
        """Initialize."""
        self.set = []
        self.n = 0

        if input is not None:
            for i in range(len(input)):
                self.add(input[i])

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

    def __getitem__(self, index):
        """Return an element from a specific index."""
        if index < 0 or index > self.n:
            raise IndexError("index is out of bounds")

        return self.set[index]

    def add(self, elem):
        """Add element to the set if it doesn't exist."""
        if not self.set.__contains__(elem):
            self.set.append(elem)
            self.n += 1

    def __contains__(self, elem):
        """Generic contains method."""
        return self.set.__contains__(elem)

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
        return self.set.__contains__(elem)

    def xnotinset(self, elem):
        """Return true if element is not in set."""
        return not self.xinset(elem)

    def isdisjoint(self, other):
        """Return true if the intersection between other and self.set is zero."""
        return len(self.intersection(other)) == 0

    def issubset(self, other):
        """Test if every element in myset is in other."""
        for i in range(self.n):
            if not other.__contains__(self.set[i]):
                return False
        return True

    def issuperset(self, other):
        """Test if every element in other is in myset."""
        for i in range(self.n):
            if not self.set.__contains__(other[i]):
                return False
        return True

    def union(self, other):
        """Return a new set with all the elements from myset and other."""
        union = MySet()
        for i in range(self.n):
            union.add(self.set[i])

        for i in range(len(other)):
            union.add(other[i])

        return union

    def intersection(self, other):
        """Return a new set with the common elements between myset and other."""
        intersection = MySet()
        if len(other) > self.n:
            for i in range(len(other)):
                if self.set.__contains__(other[i]):
                    intersection.add(other[i])
        else:
            for i in range(self.n):
                if other.__contains__(self.set[i]):
                    intersection.add(self.set[i])

        return intersection

    def difference(self, other):
        """Return a new set with the elements in myset that are not in other."""
        difference = MySet()
        for elem in self.set:
            if not other.__contains__(elem):
                difference.add(elem)

        return difference

    def symmetric_difference(self, other):
        """Return a new set with elements that are in either set or other but not in both."""
        sym_difference = MySet()
        for i in range(len(other)):
            if not self.set.__contains__(other[i]):
                sym_difference.add(other[i])

        for i in range(self.n):
            if not other.__contains__(self.set[i]):
                sym_difference.add(self.set[i])

        return sym_difference

if __name__ == '__main__':
    myset = MySet([1, 2, 3, 4])
    myset2 = MySet([1, 5, 6, 4])
