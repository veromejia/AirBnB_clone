#!/usr/bin/python3
"""Unittest for Place class"""

import unittest
from models.place import Place
import os


class TestPlace(unittest.TestCase):

    """Test Cases for Place Class"""

    def setUp(self):
        """Imports module"""
        pass

    # ---------------task 8 ----------------
    def test_init(self):
        my_place = Place()
        self.assertTrue(isinstance(my_place, Place))

    def test_sub_class(self):
        my_place = Place()
        self.assertTrue(issubclass(my_place.__class__, Place))

    def test_inheritance(self):
        my_place = Place()
        self.assertTrue(hasattr(my_place, "city_id"))
        self.assertTrue(hasattr(my_place, "user_id"))
        self.assertTrue(hasattr(my_place, "name"))
        self.assertTrue(hasattr(my_place, "description"))
        self.assertTrue(hasattr(my_place, "number_rooms"))
        self.assertTrue(hasattr(my_place, "number_bathrooms"))
        self.assertTrue(hasattr(my_place, "max_guest"))
        self.assertTrue(hasattr(my_place, "price_by_night"))
        self.assertTrue(hasattr(my_place, "latitude"))
        self.assertTrue(hasattr(my_place, "longitude"))
        self.assertTrue(hasattr(my_place, "amenity_ids"))

if __name__ == "__main__":
    unittest.main()
