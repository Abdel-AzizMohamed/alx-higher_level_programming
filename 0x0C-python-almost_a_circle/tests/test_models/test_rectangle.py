#!/usr/bin/python3
"""Define a unittest for base class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle_init(unittest.TestCase):
    def test_normal(self):
        rect_1 = Rectangle(5, 10, 2, 4, 5)
        self.assertEqual(rect_1.width, 5)
        self.assertEqual(rect_1.height, 10)
        self.assertEqual(rect_1.x, 2)
        self.assertEqual(rect_1.y, 4)
        self.assertEqual(rect_1.id, 5)

    def test_pos(self):
        rect_1 = Rectangle(5, 10)
        self.assertEqual(rect_1.x, 0)
        self.assertEqual(rect_1.y, 0)

    def test_id(self):
        rect_1 = Rectangle(5, 10)
        self.assertEqual(rect_1.id, 3)
        rect_2 = Rectangle(5, 10, 2, 3, None)
        self.assertEqual(rect_2.id, 4)


class TestRectangle_setters(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_width(self):
        with self.assertRaises(TypeError):
            rect_1 = Rectangle("1", 2)
        with self.assertRaises(ValueError):
            rect_1 = Rectangle(0, 2)

    def test_height(self):
        with self.assertRaises(TypeError):
            rect_1 = Rectangle(1, "2")
        with self.assertRaises(ValueError):
            rect_1 = Rectangle(1, 0)

    def test_x(self):
        with self.assertRaises(TypeError):
            rect_1 = Rectangle(1, 2, "3")
        with self.assertRaises(ValueError):
            rect_1 = Rectangle(1, 2, -1)

    def test_y(self):
        with self.assertRaises(TypeError):
            rect_1 = Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            rect_1 = Rectangle(1, 2, 3, -1)


class TestRectangle_methods(unittest.TestCase):
    def test_area(self):
        rect_1 = Rectangle(5, 5)
        self.assertTrue(rect_1.area() == 25)

    def test_str(self):
        rect_1 = Rectangle(10, 15)
        str_rep = "[Rectangle] (7) 0/0 - 10/15"
        self.assertEqual(str(rect_1), str_rep)

    def test_update(self):
        rect_1 = Rectangle(10, 15)
        rect_1.update(50)
        self.assertEqual(rect_1.id, 50)
        rect_1.update(50, 20)
        self.assertEqual(rect_1.width, 20)
        rect_1.update(50, 20, 25)
        self.assertEqual(rect_1.height, 25)
        rect_1.update(50, 20, 25, 5)
        self.assertEqual(rect_1.x, 5)
        rect_1.update(50, 20, 25, 5, 2)
        self.assertEqual(rect_1.y, 2)
