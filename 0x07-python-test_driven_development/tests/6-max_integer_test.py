#!/usr/bin/python3
"""Unittests for 6-max_integer_test."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for 6-max_integer_test."""

    def test_list(self):
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer, 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)
