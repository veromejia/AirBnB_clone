#!/usr/bin/python3
"""Unittest for City class"""

import unittest
from models.city import City
import os

class TestCity(unittest.TestCase):

    """Test Cases for City Class"""

    def setUp(self):
        """Imports module"""
        pass

    # ---------------task 9 ----------------
    def test_init(self):
        my_city = City()
        self.assertTrue(isinstance(my_city, City))

    def test_sub_class(self):
        my_city = City()
        self.assertTrue(issubclass(my_city.__class__, City))

    def test_inheritance(self):
        my_city = City()
        self.assertTrue(hasattr(my_city, "state_id"))
        self.assertTrue(hasattr(my_city, "name"))

if __name__ == "__main__":
    unittest.main()
