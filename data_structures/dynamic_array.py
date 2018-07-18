import ctypes

class DynamicArray(object):
    
    def __init__(self, capacity=1):
        self.size = 0
        self.capacity = capacity
        self.array = self.make_array(self.capacity)

    def __repr__(self):
        s = '['
        for i in range(self.size):
            s += str(self.array[i])
            if i != self.size - 1:
                s += ', '
        s += ']'
        return s

    def extend(self, array):
        for i in range(len(array)):
            self.append(array[i])

        return self.array
    
    def insert(self, index, value):
        if index <= 0:
            new_array = self.make_array(self.capacity + 1)
            new_array[0] = value
            for i in range(self.size):
                new_array[i + 1] = self.array[i]
            self.array = new_array

        elif index > self.size:
            self.append(value)
        else:
            pass

        self.size += 1
        return self.array

    def index(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return ValueError(str(value) + ' is not in the list')

    def remove(self, value):
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

    def count(self, value):
        count = 0
        for i in range(self.size):
            if self.array[i] == value:
                count += 1
        return count
    
    def reverse(self):
        r_array = self.make_array(self.capacity)
        for i in range(self.size):
            r_array[i] = self.array[self.size - 1 - i]

        self.array = r_array
        return

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def append(self, value):

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
        return self.size
    
    def __getitem__(self, index):
        
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
    
