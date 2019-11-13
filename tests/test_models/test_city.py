#!/usr/bin/python3
"""Unittest for City class"""

import unittest
from models.city import City
import pep8


class TestCity(unittest.TestCase):

    """Test Cases for City Class"""
    def setUp(self):
        """Imports module"""
        pass

    # ---------------task 9 ----------------
    def test_pep8(self):
        style_test = pep8.StyleGuide(quiet=True).check_files(['models/user.py'])
        self.assertEqual(style_test.total_errors, 0, "Fix pep8 errors")

    def test_init(self):
        my_city = City()
        self.assertTrue(isinstance(my_city, City))

    def test_sub_class(self):
        my_city = City()
        self.assertTrue(issubclass(my_city.__class__, City))

    def test_attr(self):
        my_city = City()
        self.assertTrue(hasattr(my_city, "state_id"))
        self.assertTrue(hasattr(my_city, "name"))

    def test_none(self):
        my_city = City()
        self.assertIsNotNone(my_city.id)
        self.assertIsNotNone(my_city.created_at)
        self.assertIsNotNone(my_city.updated_at)

if __name__ == "__main__":
    unittest.main()
