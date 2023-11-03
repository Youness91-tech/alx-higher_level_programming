#!/usr/bin/python3

"""module contains a function that multiplies two matrices"""

import numpy as np


def lazy_matrix_mul(a, b):
    """Return the multiplication of two matrices.
    Args:
        a : The first matrix.
        b : The second matrix.
    """

    return (np.matmul(a, b))
