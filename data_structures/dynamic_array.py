"""List class implementation."""
import ctypes


class DynamicArray(object):
    """List class."""

    def __init__(self, capacity=1):
        """Initialize."""
        self.size = 0
        self.capacity = capacity
        self.array = self.make_array(self.capacity)

    def __repr__(self):
        """String representation."""
        s = '['
        for i in range(self.size):
            s += str(self.array[i])
            if i != self.size - 1:
                s += ', '
        s += ']'
        return s

    def __eq__(self, other):
        """Check equality."""
        for i in range(self.size):
            if other[i] != self.array[i]:
                return False
        return True

    def extend(self, array):
        """Concatenate one array to self."""
        for i in range(len(array)):
            self.append(array[i])

        return self.array

    def insert(self, index, value):
        """Insert a value at a specific index."""
        if index <= 0:
            new_array = self.make_array(self.capacity + 1)
            new_array[0] = value
            for i in range(self.size):
                new_array[i + 1] = self.array[i]
            self.array = new_array

        elif index > self.size:
            self.append(value)
        else:
            new_array = self.make_array(self.capacity + 1)
            for i in range(index):
                new_array[i] = self.array[i]

            new_array[i + 1] = value

            for j in range(i + 2, self.size + 1):
                new_array[j] = self.array[j - 1]

            self.array = new_array

        self.size += 1
        return self.array

    def index(self, value):
        """Return the index of a value from the array. Raise an exception if it is not in the array."""
        for i in range(self.size):
            if self.array[i] == value:
                return i
        raise ValueError(str(value) + ' is not in the list')

    def remove(self, value):
        """Remove the first instance of a value."""
        value_index = self.index(value)
        removed_array = self.make_array(self.capacity)

        for i in range(self.size - 1):
            if i >= value_index:
                j = i + 1
            else:
                j = i
            removed_array[i] = self.array[j]

        self.array = removed_array
        self.size -= 1
        return self.array

    def count(self, value):
        """Count the number instances of value."""
        count = 0
        for i in range(self.size):
            if self.array[i] == value:
                count += 1
        return count

    def reverse(self):
        """Reverse the array."""
        r_array = self.make_array(self.capacity)
        for i in range(self.size):
            r_array[i] = self.array[self.size - 1 - i]

        self.array = r_array
        return self.array

    def make_array(self, capacity):
        """Make an array with type python objects with length capacity."""
        return (capacity * ctypes.py_object)()

    def append(self, value):
        """Add a value to the end of the array."""
        if self.capacity <= self.size:
            self._resize(2 * self.capacity)

        self.array[self.size] = value
        self.size += 1

    def _resize(self, new_capactity):

        self.temp_array = self.make_array(2 * self.capacity)

        for i in range(self.size):
            self.temp_array[i] = self.array[i]

        self.array = self.temp_array
        self.capacity = new_capactity

    def __len__(self):
        """Return the number of elements in the array."""
        return self.size

    def __getitem__(self, index):
        """Return an element from a specific index."""
        if index < 0 or index > self.size:
            raise IndexError("index is out of bounds")

        return self.array[index]

if __name__ == '__main__':
    l = DynamicArray()
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    print(l)
    l.remove(3)
    print(l)
    l.insert(-1, 1)
    print(l)
