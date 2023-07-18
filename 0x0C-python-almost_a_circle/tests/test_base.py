#!/usr/bin/python3
"""Define a unittest for base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base(self):
        base_1 = Base()
        self.assertEqual(base_1.id, 1)
        base_1 = Base(None)
        self.assertEqual(base_1.id, 2)

        base_2 = Base(10)
        self.assertEqual(base_2.id, 10)
