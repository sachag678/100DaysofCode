"""Implement Dict."""
import unittest


class HashMap():
    """Implement dictionary."""

    def __init__(self, list=None):
        """Initialize."""
        self.keys = []
        self.values = []
        self.n = 0
        if list is not None:
            for k,v in list:
                self.__setitem__(k, v)
    
    def __len__(self):
        """Get length."""
        return self.n

    def __repr__(self):
        """String representation."""
        s = '{'

        for i, (key, value) in enumerate(zip(self.keys, self.values)):
            s += '\''
            s += str(key)
            s += '\': '
            s += str(value)
            if i < self.n - 1:
                s += ', '

        s += '}'

        return s

    def __setitem__(self, key, value):
        """Set item.
           Checks if the dict contains the name or not and adds it in accordingly.
        """
        if not self.keys.__contains__(key):
            self.keys.append(key)
            self.values.append(value)
        else:
            self.values[self.keys.index(key)] = value
        self.n += 1

    def __getitem__(self, key):
        """Get an item."""
        if not self.keys.__contains__(key):
            raise KeyError('Keys does not contain ' + key)
        return self.values[self.keys.index(key)]
    
    def __delitem__(self, key):
        """Delete an item."""
        if not self.keys.__contains__(key):
            raise KeyError('Keys does not contain ' + key)
        self.values.pop(self.keys.index(key))
        self.keys.remove(key)
        self.n -=1
    
    def __contains__(self, item):
        """Check if a key exists."""
        return self.keys.__contains__(item)

    def __eq__(self, other):
        """Check equality between other and self."""
        for (k, v) in other.items():
            if k in self.keys:
                if not self.values[self.keys.index(k)] == v:
                    return False
            else:
                return False
        
        return True
    
    def items(self):
        """Return generator of items."""
        for k, v in zip(self.keys, self.values):
            yield (k, v)
    
    def ___iter__(self):
        """Return generator of keys."""
        for k in self.keys:
            yield k
    
class TestHashMap(unittest.TestCase):
    """Test HashMap."""

    def setUp(self):
        """Initialize dict."""
        self.hashmap = HashMap()

    def test_add_item(self):
        """Test adding and retrieving."""
        self.hashmap['john'] = 25
        self.assertEqual(self.hashmap['john'], 25)
    
    def test_modify_value_of_an_existing_key(self):
        """Modifying the value of the existing key."""
        self.hashmap['john'] = 25
        self.hashmap['john'] = 50
        self.assertEqual(self.hashmap['john'], 50)
    
    def test_deletion(self):
        """Deleting key:value pair."""
        self.hashmap['john'] = 25
        del self.hashmap['john']
        self.assertEqual(len(self.hashmap), 0)
    
    def test_contains(self):
        """Checks whether the key exists."""
        self.assertEqual('john' in self.hashmap, False)

    def test_list(self):
        """Test the list functionality."""
        self.assertEqual(list(self.hashmap),[])
    
    def test_init(self):
        """Test initialize."""
        hashmap_ = HashMap([('sape', 4139)])
        self.assertEqual(hashmap_['sape'], 4139)

    def test_equality(self):
        """Test equality."""
        hashmap_ = HashMap([('sape', 4139)])
        self.hashmap['sape'] = 4139
        self.assertEqual(self.hashmap, hashmap_)
    
if __name__ == '__main__':
    h = HashMap(list=[('john', 20),('greg', 50)])
  #  list(h)
    for i in h:
        print(h)