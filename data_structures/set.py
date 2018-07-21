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

if __name__ == '__main__':
    myset = MySet()
    myset.add(2)
    myset.add(3)
    myset.add(3)
