#!/usr/bin/python3
"""Unittesting the Rectangle class.
"""


import unittest
from models import Base
from models import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class.
    """
    @classmethod
    def setUpClass(cls):
        cls.rec1 = Rectangle(10, 2)
        cls.rec2 = Rectangle(2, 10)
        cls.rec3 = Rectangle(10, 2, 0, 0, 12)

    def test_inheritance(self):
        """tests if the rectangle instance inherits from the Base class.
        """
        self.assertTrue(issubclass(type(self.rec1), Base))

    def test_id(self):
        """tests if id attribute is stored with the Base class __init__
        logic.
        """
        self.assertEqual(self.rec1.id, 5)
        self.assertEqual(self.rec2.id, 6)
        self.assertEqual(self.rec3.id, 12)

    def test_setter_validation(self):
        """tests if the setter methods and attribute instantiation are done
        right.
        """
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3, 1)
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_area(self):
        """tests the area method of the Rectangle class.
        """
        self.assertEqual(self.rec1.area(), 20)
        self.assertEqual(Rectangle(5, 5).area(), 25)
