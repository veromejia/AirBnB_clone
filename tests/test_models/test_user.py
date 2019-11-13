#!/usr/bin/python3
"""
Unittest for User class
"""

import unittest
from models.user import User
from models.base_model import BaseModel
import pep8

class TestUser(unittest.TestCase):

    """Test Cases for User Class"""
    def setUp(self):
        """Imports module"""
        pass

    def test_pep8(self):
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_init(self):
        my_user = User()
        self.assertTrue(isinstance(my_user, User))

    def test_sub_class(self):
        my_user = User()
        self.assertTrue(issubclass(my_user.__class__, User))

    def test_inheritance(self):
        my_user = User()
        self.assertTrue(hasattr(my_user, "created_at"))
        self.assertTrue(hasattr(my_user, "updated_at"))
        self.assertTrue(hasattr(my_user, "id"))

    def test_none(self):
        my_user = User()
        self.assertIsNotNone(my_user.id)
        self.assertIsNotNone(my_user.created_at)
        self.assertIsNotNone(my_user.updated_at)

    def test_attr(self):
        my_user = User()
        self.assertTrue(hasattr(my_user, "email"))
        self.assertTrue(hasattr(my_user, "password"))
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertTrue(hasattr(my_user, "last_name"))

    def test_dict(self):
        my_user = User()
        self.assertTrue("to_dict" in dir(my_user))

if __name__ == "__main__":
    unittest.main()
