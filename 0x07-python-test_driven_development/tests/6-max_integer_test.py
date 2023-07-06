#!/usr/bin/python3
"""Define a unittest for max_integer function"""


import unittest
fun = __import__('6-max_integer').max_integer

class TextMax(unittest.TestCase):

    def test_max_integer(self):
        result = fun([1, 2, 3])
        self.assertEqual(result, 3)
        result = fun([3, 1, 2])
        self.assertEqual(result, 3)
        result = fun([-3, 1, -5])
        self.assertEqual(result, 1)
        result = fun([])
        self.assertEqual(result, None)
        result = fun([3.3, 4.55, 6.99, 2])
        self.assertEqual(result, 6.99)
        result = fun(["test1", "test2", "big text", "test3"])
        self.assertEqual(result, "test3")
        result = fun("")
        self.assertEqual(result, None)
