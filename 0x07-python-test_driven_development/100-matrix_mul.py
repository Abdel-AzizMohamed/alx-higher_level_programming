#!/usr/bin/python3
"""Define Matrix multiplication Function

    Functions:
        matrix_mul
"""


def matrix_mul(m_a, m_b):
    """Multipla 2 matrix

        Args:
            m_a(list): first matrix
            m_b(list): second matrix

        Raises:
            TypeError: if m_a or m_b is not list
            TypeError: if m_a or m_b is not list of lists
            ValueError: if m_a or m_b is empty ([], [[]])
            TypeError: if one of elemets in both matrix is not float, integer
            TypeError: if m_a or m_b is not rectangle
            ValueError: if m_a and m_b can't be multiplied

        Return: result of multiplication
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for i in range(len(m_a)):
        new_list = []
        for j in range(len(m_b[0])):
            result = 0
            for k in range(len(m_b)):
                result += m_a[i][k] * m_b[k][j]
            new_list.append(result)
        new_matrix.append(new_list)
    return new_matrix
