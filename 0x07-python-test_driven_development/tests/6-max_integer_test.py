#!/usr/bin/python3
"""Unittests for 6-max_integer_test."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for 6-max_integer_test."""

    def test_list(self):
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [3]
        self.assertEqual(max_integer(one_element), 3)

    def test_oneNeg_list(self):
        oneNeg = [1, -2, 3, 4]
        self.assertEqual(max_integer(oneNeg), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

