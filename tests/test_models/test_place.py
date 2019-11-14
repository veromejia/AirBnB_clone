#!/usr/bin/python3
"""Unittest for Place class"""

import unittest
import pep8
from os import path, remove
import datetime
from models import base_model
from models import place
from models.base_model import BaseModel
from models.place import Place
from models import engine
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):

    """Test Cases for Place Class"""
    def setUp(self):
        """Imports module"""
        pass

    # ---------------task 9 ----------------

    def test_pep8_conformance(self):
        """Test that City conforms to PEP8"""
        style_test= pep8.StyleGuide(quiet=True).check_files(['models/city.py'])
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

    def test_inheritance(self):
        my_place = Place()
        self.assertTrue(hasattr(my_place, "created_at"))
        self.assertTrue(hasattr(my_place, "updated_at"))
        self.assertTrue(hasattr(my_place, "id"))

    def test_dict(self):
        my_place = Place()
        self.assertTrue("to_dict" in dir(my_place))

if __name__ == "__main__":
    unittest.main()
