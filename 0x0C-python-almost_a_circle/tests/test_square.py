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
        self.assertEqual(sq_1.id, 18)

    def test_str(self):
        sq_1 = Square(10, 2, 4, 3)
        self.assertEqual(str(sq_1), "[Square] (3) 2/4 - 10")

    def test_setter(self):
        sq_1 = Square(1, 1, 1)
        sq_1.size = 15
        sq_1.x = 2
        sq_1.y = 4
        self.assertEqual(sq_1.width, 15)
        self.assertEqual(sq_1.height, 15)
        self.assertEqual(sq_1.size, 15)
        self.assertEqual(sq_1.x, 2)
        self.assertEqual(sq_1.y, 4)

    def test_update(self):
        sq_1 = Square(1, 1, 1)
        sq_1.update(10, 15, 3, 4) 
        self.assertEqual(sq_1.width, 15)
        self.assertEqual(sq_1.height, 15)
        self.assertEqual(sq_1.size, 15)
        self.assertEqual(sq_1.x, 3)
        self.assertEqual(sq_1.y, 4)
        sq_1.update(size=10, x=15, y=3) 
        self.assertEqual(sq_1.width, 10)
        self.assertEqual(sq_1.height, 10)
        self.assertEqual(sq_1.size, 10)
        self.assertEqual(sq_1.x, 15)
        self.assertEqual(sq_1.y, 3)
