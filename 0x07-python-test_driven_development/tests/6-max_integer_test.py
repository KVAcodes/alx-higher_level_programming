#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_output(self):
        self.assertTrue(max_integer([1, 2, 3, 4]) == 4)
        self.assertTrue(max_integer([1, 3, 4, 3]) == 4)
        self.assertTrue(max_integer([]) == None)
        self.assertTrue(max_integer() == None)
        self.assertTrue(max_integer([16, 2, 3, 4]) == 16)
        self.assertTrue(max_integer([-1, -2, -3, -4]) == -1)
        self.assertTrue(max_integer([-1, 2, 3, 4]) == 4)
        self.assertTrue(max_integer([12]) == 12)
