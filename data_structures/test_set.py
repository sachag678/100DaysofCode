"""Test set."""
from set import MySet
import unittest


class TestSet(unittest.TestCase):
    """Test Set."""

    def setUp(self):
        """Setup."""
        self.s1 = MySet([1, 4])
        self.s2 = MySet([1, 5, 6, 4])
        self.s3 = MySet([1, 2, 3, 4])

    def test_xinset(self):
        """Test element in set."""
        self.assertEqual(self.s1.xinset(4), True)

    def test_xnotinset(self):
        """Test x not in set."""
        self.assertEqual(self.s1.xnotinset(5), True)

    def test_issubset(self):
        """Test subset."""
        self.assertEqual(self.s1.issubset(self.s2), True)

    def test_issuperset(self):
        """Test subset."""
        self.assertEqual(self.s2.issuperset(self.s1), True)

    def test_union(self):
        """Test union."""
        self.assertEqual(self.s2.union(self.s1), self.s2)

    def test_intersection(self):
        """Test Intersection."""
        self.assertEqual(self.s2.intersection(self.s1), MySet([1, 4]))

    def test_difference(self):
        """Test difference."""
        self.assertEqual(self.s2.difference(self.s1), MySet([5, 6]))

    def test_sym_difference(self):
        """Test difference."""
        self.assertEqual(self.s2.symmetric_difference(self.s3), MySet([2, 3, 5, 6]))

if __name__ == '__main__':
    unittest.main()
