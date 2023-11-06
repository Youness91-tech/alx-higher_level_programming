#!/usr/bin/python3
"""base_geometry module"""


class BaseGeometry:
    """a base geometry class"""

    def area(self):
        """not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
