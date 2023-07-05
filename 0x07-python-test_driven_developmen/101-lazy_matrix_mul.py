#!/usr/bin/python3

import numpy as np

'''
Module that multiplies 2 matrices by using the module NumPy.
'''


def lazy_matrix_mul(m_a, m_b):
    '''
    Function that multiplies 2 matrices by using the module NumPy.

    Args:
        m_a: matrix a.
        m_b: matrix b.

    Returns:
        The matrix multiplied.
    '''
    return np.matmul(m_a, m_b)
