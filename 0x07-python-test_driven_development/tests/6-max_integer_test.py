#!/usr/bin/python3
"""Module for the unit testing of the max integer function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function.
    """
    def test_output(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertTrue(max_integer([16, 2, 3, 4]) == 16)
        self.assertTrue(max_integer([-1, -2, -3, -4]) == -1)
        self.assertTrue(max_integer([-1, 2, 3, 4]) == 4)
        self.assertTrue(max_integer([12]) == 12)
