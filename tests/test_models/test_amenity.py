#!/usr/bin/python3
"""Unittest for Amenity class"""

import unittest
import pep8
from os import path, remove
import datetime
from models import base_model
from models import amenity
from models.base_model import BaseModel
from models.amenity import Amenity
from models import engine
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):

    """Test Cases for Amenity Class"""
    def setUp(self):
        """Imports module"""
        pass

    # ---------------task 9 ----------------
    def test_pep8(self):
        style_test = pep8.StyleGuide(quiet=True).check_files(['models/user.py'])
        self.assertEqual(style_test.total_errors, 0, "Fix pep8 errors")

    def test_init(self):
        my_amenity = Amenity()
        self.assertTrue(isinstance(my_amenity, Amenity))

    def test_sub_class(self):
        my_amenity = Amenity()
        self.assertTrue(issubclass(my_amenity.__class__, Amenity))

    def test_attr(self):
        my_amenity = Amenity()
        self.assertTrue(hasattr(my_amenity, "name"))

    def test_none(self):
        my_amenity = Amenity()
        self.assertIsNotNone(my_amenity.id)
        self.assertIsNotNone(my_amenity.created_at)
        self.assertIsNotNone(my_amenity.updated_at)

    def test_inheritance(self):
        my_amenity = Amenity()
        self.assertTrue(hasattr(my_amenity, "created_at"))
        self.assertTrue(hasattr(my_amenity, "updated_at"))
        self.assertTrue(hasattr(my_amenity, "id"))

    def test_dict(self):
        my_amenity = Amenity()
        self.assertTrue("to_dict" in dir(my_amenity))

if __name__ == "__main__":
    unittest.main()
