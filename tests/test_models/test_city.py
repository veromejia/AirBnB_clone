#!/usr/bin/python3
"""Unittest for City class"""

import unittest
import pep8
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
    """Test Cases For City Class"""

    def setUp(self):
        """Imports module"""
        pass

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

    def test_pep8(self):
        style_test= pep8.StyleGuide(quiet=True).check_files(['models/city.py'])
        self.assertEqual(style_test.total_errors, 0, "Fix pep8 errors")
        
