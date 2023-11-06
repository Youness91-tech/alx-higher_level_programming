#!/usr/bin/python3
"""rectangle module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square"""

    def __init__(self, size):
        """initialize the attributes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.area()
