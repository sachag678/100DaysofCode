"""Tests for dyamic array."""

from dynamic_array import DynamicArray
import unittest


class TestDynamicArraymethods(unittest.TestCase):
    """Main Tests."""

    # test size of initialized array
    def test_array_empty(self):
        dynamic_array = DynamicArray()
        self.assertEqual(len(dynamic_array), 0)

    # test append and __getitem__
    def test_array_has_specific_element(self):
        dynamic_array = DynamicArray()
        dynamic_array.append(2)
        self.assertEqual(dynamic_array[0], 2)

    # test append and len
    def test_array_has_one_element(self):
        dynamic_array = DynamicArray()
        dynamic_array.append(2)
        self.assertEqual(len(dynamic_array), 1)

    # test multiple appends
    def test_multiple_appends(self):
        dynamic_array = DynamicArray()
        dynamic_array.append(2)
        dynamic_array.append(3)
        self.assertEqual(len(dynamic_array), 2)

    # error checking
    def test_getting_index(self):
        dynamic_array = DynamicArray()
        dynamic_array.append(2)
        with self.assertRaises(IndexError) as cm:
            dynamic_array[3]

        self.assertEqual("index is out of bounds", cm.exception.args[0])

    def test_count(self):
        dynamic_array = DynamicArray()
        dynamic_array.append(2)
        dynamic_array.append(2)
        dynamic_array.append(3)
        self.assertEqual(dynamic_array.count(2), 2)

    def test_insert(self):
        dynamic_array = DynamicArray()
        dynamic_array.append(1)
        dynamic_array.append(3)

        dynamic_array2 = DynamicArray()
        dynamic_array2.append(1)
        dynamic_array2.append(2)
        dynamic_array2.append(3)

        self.assertEqual(dynamic_array.insert(1, 2), dynamic_array2)

    def test_remove(self):
        dynamic_array = DynamicArray()
        dynamic_array.append(1)
        dynamic_array.append(2)
        dynamic_array.append(3)

        dynamic_array2 = DynamicArray()
        dynamic_array2.append(1)
        dynamic_array2.append(2)

        self.assertEqual(dynamic_array.remove(3), dynamic_array2)

    def test_reverse(self):
        dynamic_array1 = DynamicArray()
        dynamic_array1.append(2)
        dynamic_array1.append(3)
        dynamic_array2 = DynamicArray()
        dynamic_array2.append(3)
        dynamic_array2.append(2)

        self.assertEqual(dynamic_array1.reverse(), dynamic_array2)

    def test_extend(self):
        dynamic_array1 = DynamicArray()
        dynamic_array1.append(2)
        dynamic_array2 = DynamicArray()
        dynamic_array2.append(2)

        dynamic_array3 = DynamicArray()
        dynamic_array3.append(2)
        dynamic_array3.append(2)

        self.assertEqual(dynamic_array1.extend(dynamic_array2), dynamic_array3)


if __name__ == '__main__':
    unittest.main()
