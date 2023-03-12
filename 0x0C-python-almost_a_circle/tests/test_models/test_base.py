#!/usr/bin/python3
"""Unittesting the base Class.
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Executes code within it at the beginning of the testing.
        """
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base()
        cls.b4 = Base(12)
        cls.b5 = Base()

    def test_id(self):
        """A test for the id attribute.
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)
