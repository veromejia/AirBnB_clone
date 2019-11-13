#!/usr/bin/python3
"""
Unittest for the City class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_city.py
"""
import unittest
import pep8
# import sys
# import io
from os import path, remove
import datetime
from models import base_model
from models import city
from models.base_model import BaseModel
from models.city import City
from models import engine
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """define variables and methods"""

    def setUp(self):
        """Imports module"""
        pass

    def test_pep8_conformance(self):
        """Test that City conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_init(self):
        my_city = City()
        self.assertTrue(isinstance(my_city, City))

    def test_sub_class(self):
        my_city = City()
        self.assertTrue(issubclass(my_city.__class__, City))

    def test_inheritance(self):
        my_city = City()
        self.assertTrue(hasattr(my_city, "created_at"))
        self.assertTrue(hasattr(my_city, "updated_at"))
        self.assertTrue(hasattr(my_city, "id"))

    def test_attr(self):
        my_city = City()
        self.assertTrue(hasattr(my_city, "state_id"))
        self.assertTrue(hasattr(my_city, "name"))

    def test_none(self):
        my_city = City()
        self.assertIsNotNone(my_city.id)
        self.assertIsNotNone(my_city.created_at)
        self.assertIsNotNone(my_city.updated_at)

    def test_dict(self):
        my_city = City()
        self.assertTrue("to_dict" in dir(my_city))
