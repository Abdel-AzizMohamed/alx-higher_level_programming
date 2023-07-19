#!/usr/bin/python3
"""Define a unittest for base class"""
import unittest
from models.square import Square


class TestRectangle_init(unittest.TestCase):
    def test_normal(self):
        sq_1 = Square(10, 2, 4)
        self.assertEqual(sq_1.width, 10)
        self.assertEqual(sq_1.height, 10)
        self.assertEqual(sq_1.x, 2)
        self.assertEqual(sq_1.y, 4)
        self.assertEqual(sq_1.id, 17)

    def test_str(self):
        sq_1 = Square(10, 2, 4, 3)
        self.assertEqual(str(sq_1), "[Square] (3) 2/4 - 10")
