"""Implement Dict."""
import unittest


class HashMap():
    """Implement dictionary."""

    def __init__(self):
        """Initialize."""
        self.keys = []
        self.values = []
        self.n = 0

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

    def __setitem__(self, name, value):
        """Set item."""
        self.keys.append(name)
        self.values.append(value)
        self.n += 1

    def __getitem__(self, name):
        """Get an item."""
        return self.values[self.keys.index(name)]


class TestHashMap(unittest.TestCase):
    """Test HashMap."""

    def setUp(self):
        """Initialize dict."""
        self.hashmap = HashMap()

    def test_add_item(self):
        """Test adding and retrieving."""
        self.hashmap['john'] = 25
        self.assertEqual(self.hashmap['john'], 25)

if __name__ == '__main__':
    unittest.main()
