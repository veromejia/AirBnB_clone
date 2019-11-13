#!/usr/bin/python3
"""Unittest for Place class"""

import unittest
from models.place import Place
import pep8


class TestPlace(unittest.TestCase):

    """Test Cases for Place Class"""
    def setUp(self):
        """Imports module"""
        pass

    # ---------------task 9 ----------------
    def test_pep8(self):
        style_test = pep8.StyleGuide(quiet=True).check_files(['models/user.py'])
        self.assertEqual(style_test.total_errors, 0, "Fix pep8 errors")

    def test_init(self):
        my_place = Place()
        self.assertTrue(isinstance(my_place, Place))

    def test_sub_class(self):
        my_place = Place()
        self.assertTrue(issubclass(my_place.__class__, Place))

    def test_attr(self):
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

    def test_none(self):
        my_place = Place()
        self.assertIsNotNone(my_place.id)
        self.assertIsNotNone(my_place.created_at)
        self.assertIsNotNone(my_place.updated_at)

if __name__ == "__main__":
    unittest.main()
