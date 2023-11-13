#!/usr/bin/python3
"""UnitTests for base class"""
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases to Base class"""

    def test_init_with_too_many_args(self):
        """Test initialization with too many args"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_init_with_no_id(self):
        """Test initialization with no id"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_init_with_id_set(self):
        """Test initialization with id set"""
        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def test_init_with_no_id_after_set(self):
        """Test initialization with no id aftr setting id"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_nb_objects_private(self):
        """Test nb_objects as a private instance attrbte"""
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)

    def test_to_json_string(self):
        """Test conversion to a JSON string"""
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_to_json_string_with_empty_list(self):
        """Test conversion to JSON string with an empty list"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_to_json_string_with_none(self):
        """Test conversion to JSON string with None"""
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """Test conversion from a JSON string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
                     {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_from_json_string_with_empty_string(self):
        """Test conversion from an empty JSON string"""
        self.assertEqual([], Base.from_json_string(""))

    def test_from_json_string_with_none(self):
        """Test conversion from None JSON string"""
        self.assertEqual([], Base.from_json_string(None))


if __name__ == '__main__':
    unittest.main()
