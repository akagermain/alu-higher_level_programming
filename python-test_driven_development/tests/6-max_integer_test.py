#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_normal_list(self):
        """Test with a normal ascending list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        """Test with an unsorted list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Test with no argument, using the default empty list."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test with a list of only negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_numbers(self):
        """Test with a mix of negative, zero, and positive numbers."""
        self.assertEqual(max_integer([-5, 3, 0, -2, 10]), 10)

    def test_all_same_numbers(self):
        """Test with a list where every element is the same."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_two_elements(self):
        """Test with a list containing two elements, in both orders."""
        self.assertEqual(max_integer([3, 9]), 9)
        self.assertEqual(max_integer([9, 3]), 9)

    def test_max_at_end(self):
        """Test with the maximum value at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 100]), 100)

    def test_max_at_start(self):
        """Test with the maximum value at the start of the list."""
        self.assertEqual(max_integer([100, 2, 3, 1]), 100)

    def test_floats(self):
        """Test with a list containing float values."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == "__main__":
    unittest.main()
