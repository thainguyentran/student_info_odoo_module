import unittest
from odoo.tests import tagged
    

def rotate_matrix(m):
    if not m:
        return False
    for row in m:
        if len(row) != len(m):
            return False
    # list comprehension
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]
    # non list comprehension way
    n = []
    O(n2)
    for i in range(len(m[0]) - 1, len(m)):
        temp = []
        for j in range(len(m)):
            temp.append(m[j][i])
        n.append(temp)
    return n

    # rotate in place
    l, r = 0, len(m) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            # save topleft
            topleft = m[top][l + i]
            # top left will be replaced with top right
            # left + i => means direction is going from left to right
            # top + i => means direction is going from top to bottom
            m[top][l + i] = m[top + i][r]
            # top right will be replaced with bottom right
            m[top + i][r] = m[bottom][r - i]
            # bottom right will be replaced with bottom left
            m[bottom][r - i] = m[bottom - i][l]
            # bottom left will be replaced with top left
            m[bottom - i][l] = topleft
        r -= 1
        l += 1
    return m


class TestMatrixRotation(unittest.TestCase):
    def test_rotate_success_2x2(self):
        A = [
            [1, 2],
            [3, 4],
        ]
        actual = rotate_matrix(A)
        expected = [
            [2, 4],
            [1, 3]
        ]
        self.assertEqual(actual, expected)

    def test_rotate_success_3x3(self):
        A = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        actual = rotate_matrix(A)
        expected = [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7],
        ]
        self.assertEqual(actual, expected)

    def test_rotate_success_4x4(self):
        A = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        actual = rotate_matrix(A)
        expected = [
            [4, 8, 12, 16],
            [3, 7, 11, 15],
            [2, 6, 10, 14],
            [1, 5, 9, 13],
        ]
        self.assertEqual(actual, expected)

    def test_rotate_success_1x1(self):
        A = [
            [1]
        ]
        actual = rotate_matrix(A)
        expected = [
            [1]
        ]
        self.assertEqual(actual, expected)

    def test_rotate_wrong_matrix_size(self):
        A = [
            [1, 2],
            [3, 4],
            [5, 6],
        ]
        actual = rotate_matrix(A)
        expected = False
        self.assertEqual(actual, expected)

    def test_empty_matrix(self):
        A = [
            []
        ]
        actual = rotate_matrix(A)
        expected = False
        self.assertEqual(actual, expected)

    def test_missing_value_matrix(self):
        A = [
            [1,2],
            [3,]
        ]
        actual = rotate_matrix(A)
        expected = False
        self.assertEqual(actual, expected)
