"""Understand how iterators function."""


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

if __name__ == '__main__':
    r = ReverseList([1, 2, 3, 4])
    for val in r:
        print(val)
