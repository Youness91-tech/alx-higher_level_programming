#!/usr/bin/python3
"""
UnitTests for the Rectangle class
"""

import unittest
import json
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """Test the functionality of the class"""
    @classmethod
    def setUpClass(cls):
        """setting the class"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 10)
        cls.r2 = Rectangle(2, 3, 4)

    def test_id(self):
        """Testing for ID"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)

    def test_width(self):
        """Testing for width"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)

    def test_height(self):
        """Testing for height"""
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 3)

    def test_x(self):
        """Test for x"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 4)

    def test_y(self):
        """Test for y"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)

    def test_width(self):
        """width check"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_height(self):
        """height check"""
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def width_typeerror(self):
        """Test not int width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("H", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(False, 1)

    def height_typeerror(self):
        """Test not int height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "H")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, False)

    def x_typeerror(self):
        """Test not int x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "H")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, False)

    def y_typeerror(self):
        """Test not int for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, "H")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, False)

    def width_valueerror(self):
        """Test int <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-2, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def height_valueerror(self):
        """Test int <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def x_valueerror(self):
        """Test int < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -2)

    def y_valueerror(self):
        """Test int <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -2)

    def test_area(self):
        """Test for area"""
        self.assertEqual(self.r1.area(), 100)
        self.assertEqual(self.r2.area(), 6)

    def area_arg(self):
        """Test many args for area()"""
        with self.assertRaises(TypeError):
            r = self.r1.area(2)

    def display_too_many_args(self):
        """Test many args display"""
        with self.assertRaises(TypeError):
            self.r1.display(2)

    def test_strmethod(self):
        """Test for the __str__ method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/10")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 2/3")

    def test_update_arg(self):
        """Test the udpate method"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_setter(self):
        """tests that the update method uses setter with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, 1, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(1, 1, 1, 1, -1)

    def update_too_many_args(self):
        """too many args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(1, 1, 1, 1, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def update_no_args(self):
        """no args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def mix_args_kwargs(self):
        """output for mixed args and kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")
