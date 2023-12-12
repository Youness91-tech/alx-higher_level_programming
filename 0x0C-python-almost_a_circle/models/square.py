#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size settet"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the attrbtes of the square"""
        if args:
            att_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(att_names):
                    setattr(self, att_names[i], arg)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
