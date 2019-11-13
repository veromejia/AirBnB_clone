#!/usr/bin/python3
"""Unittest for Amenity class"""

import unittest
from models.amenity import Amenity
import os


class TestAmenity(unittest.TestCase):

    """Test Cases for Amenity Class"""
    def setUp(self):
        """Imports module"""
        pass

    # ---------------task 9 ----------------
    def test_pep8(self):
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_init(self):
        my_amenity = Amenity()
        self.assertTrue(isinstance(my_amenity, Amenity))

    def test_sub_class(self):
        my_amenity = Amenity()
        self.assertTrue(issubclass(my_amenity.__class__, Amenity))

    def test_inheritance(self):
        my_amenity = Amenity()
        self.assertTrue(hasattr(my_amenity, "name"))

if __name__ == "__main__":
    unittest.main()
