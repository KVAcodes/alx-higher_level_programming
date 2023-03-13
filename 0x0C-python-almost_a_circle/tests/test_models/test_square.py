# test for square.py

import unittest
import pep8
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareModule(unittest.TestCase):
    """Testcase for the square.py module."""

    def test_pep8_conformance_square(self):
        """Test that square.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/square.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_square(self):
        """Test that square.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_square.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestSquare(unittest.TestCase):
    """Testcase for the square class."""

    @classmethod
    def setUpClass(cls):
        """Gets executed before the first testcase."""

        cls.s1 = Square(5)
        cls.s2 = Square(2, 2)
        cls.s3 = Square(3, 1, 3)

    def test_inheritance(self):
        """Testing if Square inherits from the Rectangle and Base classes."""

        self.assertTrue(isinstance(self.s1, Rectangle))
        self.assertTrue(isinstance(self.s1, Base))

    def test_str(self):
        """Testing the string representation of square objects."""

        self.assertEqual(str(self.s1), "[Square] (17) 0/0 - 5")
        self.assertEqual(str(self.s2), "[Square] (18) 2/0 - 2")
        self.assertEqual(str(self.s3), "[Square] (19) 1/3 - 3")
