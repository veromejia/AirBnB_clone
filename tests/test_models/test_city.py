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

    def test_pep8(self):
        style_test = pep8.StyleGuide(quiet=True).check_files(['models/user.py'])
        self.assertEqual(style_test.total_errors, 0, "Fix pep8 errors")

    def test_class_method_presence(self):
        """Test that the City methods are all present"""
        l1 = dir(City)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_class_attribute_presence(self):
        """Test that the City attributes are all present"""
        l1 = dir(City)
        self.assertIn('state_id', l1)
        self.assertIn('name', l1)

    def test_instance_method_presence(self):
        """Test that the City instance has the same methods"""
        l1 = dir(City())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)
