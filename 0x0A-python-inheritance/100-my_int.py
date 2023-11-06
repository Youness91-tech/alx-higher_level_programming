#!/usr/bin/python3
"""my_int module"""


class MyInt(int):
    """MyInt class"""

    def __ne__(self, next):
        return super().__eq__(next)

    def __eq__(self, next):
        return super().__ne__(next)
