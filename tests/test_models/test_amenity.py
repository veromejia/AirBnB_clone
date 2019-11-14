#!/usr/bin/python3
"""
Unittest for the Amenity class
Test files by using the following command line:
python3 -m unittest tests/test_models/test_amenity.py
"""
import unittest
import pep8
# import sys
# import io
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
    """define variables and methods"""

    def setUp(self):
        """
        Sets the public class attributes of the Amenity class back to ""
        Method called to prepare the test fixture. This is called immediately
        before calling the test method; other than AssertionError or SkipTest
        """
        Amenity.name = ""

    def tearDown(self):
        """
        Sets the public class attributes of the Amenity class back to ""
        Method called immediately after the test method has been called and
        the result recorded
        """
        del Amenity.name
        if path.exists("file.json"):
            remove("file.json")

    def test_pep8_conformance(self):
        """Test that State conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_method_presence(self):
        """Test that the Amenity methods are all present"""
        l1 = dir(Amenity)
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)

    def test_class_attribute_presence(self):
        """Test that the Amenity attributes are all present"""
        l1 = dir(Amenity)
        self.assertIn('name', l1)

    def test_instance_method_presence(self):
        """Test that the Amenity instance has the same methods"""
        l1 = dir(Amenity())
        self.assertIn('__init__', l1)
        self.assertIn('save', l1)
        self.assertIn('to_dict', l1)
        self.assertIn('__str__', l1)
