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

    def test_instance_attribute_presence(self):
        """Test that the City instance attributes are all present"""
        l1 = dir(City())
        self.assertIn('id', l1)
        self.assertIn('updated_at', l1)
        self.assertIn('created_at', l1)
        self.assertIn('__class__', l1)
        self.assertIn('state_id', l1)
        self.assertIn('name', l1)

    def test_docstring_presence(self):
        """Test that Module, Class, and methods all have a docstring"""
        self.assertIsNot(City.__doc__, None)
        self.assertIsNot(City.__doc__, None)
        self.assertIsNot(City.__init__.__doc__, None)
        self.assertIsNot(City.save.__doc__, None)
        self.assertIsNot(City.to_dict.__doc__, None)
        self.assertIsNot(City.__str__.__doc__, None)

if __name__ == "__main__":
    unittest.main()
