#!/usr/bin/python3
"""Unittest for City class"""

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

    def test_instantiation(self):
        """Test proper instantiation of object 'User()'"""

        ci = City()
        self.assertIsInstance(ci, City)
        self.assertIsInstance(ci.id, str)
        self.assertIsInstance(ci.created_at, datetime.datetime)
        self.assertIsInstance(ci.updated_at, datetime.datetime)
        self.assertIsInstance(ci.__class__, type)

        ci.size = "tall"
        l1 = dir(ci)
        self.assertIn('size', l1)
        self.assertEqual(ci.__dict__['size'], 'tall')

        ci.size = 'tall'
        l2 = dir(ci)
        self.assertIn('size', l2)
        self.assertEqual(ci.__dict__['size'], 'tall')

        ci.age = 28
        l3 = dir(ci)
        self.assertIn('age', l3)
        self.assertEqual(ci.__dict__['age'], 28)

        ci.age = 28.5
        l4 = dir(ci)
        self.assertIn('age', l4)
        self.assertEqual(ci.__dict__['age'], 28.5)

        ci.age = None
        l5 = dir(ci)
        self.assertIn('age', l5)
        self.assertEqual(ci.__dict__['age'], None)

        ci_kw1 = City(**{})
        self.assertIsInstance(ci_kw1, City)
        self.assertIsInstance(ci_kw1.id, str)
        self.assertIsInstance(ci_kw1.created_at, datetime.datetime)
        self.assertIsInstance(ci_kw1.updated_at, datetime.datetime)
        self.assertIsInstance(ci_kw1.__class__, type)

        ci_kw2 = City(**{"first_name": "John", "age": 25})
        l6 = dir(ci_kw2)
        self.assertIn('first_name', l6)
        self.assertIn('age', l6)
        self.assertEqual(ci_kw2.__dict__['first_name'], 'John')
        self.assertEqual(ci_kw2.__dict__['age'], 25)

    def test_save(self):
        """Test save method"""

        storage = FileStorage()

        ci = City()
        temp = ci.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        ci.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(ci.__dict__['updated_at'], temp)
        temp = ci.__dict__['updated_at']
        storage.reload()
        self.assertEqual(ci.__dict__['updated_at'], temp)

    def test_to_dict(self):
        """Test to_dict method"""

        ci = City()
        ci.age = 28
        ci.size = "tall"
        for k, v in ci.__dict__.items():
            if k != 'updated_at' and k != 'created_at':
                self.assertIn(k, ci.to_dict())
                self.assertEqual(v, ci.to_dict()[k])
        self.assertEqual(ci.to_dict()['__class__'], ci.__class__.__name__)
        self.assertEqual(ci.to_dict()['updated_at'], ci.updated_at.isoformat())
        self.assertEqual(ci.to_dict()['created_at'], ci.created_at.isoformat())
        self.assertEqual(ci.to_dict()['age'], 28)
        self.assertEqual(ci.to_dict()['size'], 'tall')
        self.assertIsInstance(ci.to_dict(), dict)

    def test_str(self):
        """Test __str__ method"""

        ci = City()
        string = '['+ci.__class__.__name__+']'+' ('+ci.id+') '+str(ci.__dict__)
        self.assertEqual(string, ci.__str__())

if __name__ == "__main__":
    unittest.main()
