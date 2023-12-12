#!/usr/bin/python3
"""UnitTests for square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        s = Square(5, 2, 3, 7)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 7)

    def test_str(self):
        s = Square(5, 2, 3, 7)
        expected_str = "[Square] (7) 2/3 - 5"
        self.assertEqual(str(s), expected_str)

    def test_size_property(self):
        s = Square(5, 2, 3, 7)
        s.size = 8
        self.assertEqual(s.size, 8)
        self.assertEqual(s.width, 8)
        self.assertEqual(s.height, 8)

    def test_update(self):
        s = Square(5, 2, 3, 7)
        s.update(9, 6, 4, 1)
        self.assertEqual(s.id, 9)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 1)

        s.update(size=10, x=5, y=2)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 2)

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 7)
        expected_dict = {
            "id": 7,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
