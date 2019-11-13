#!/usr/bin/python3
"""Unittest for User class"""

import unittest
from models.user import User
import os


class TestUser(unittest.TestCase):

    """Test Cases for User Class"""
    def setUp(self):
        """Imports module"""
        pass

    # ---------------task 8 ----------------

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
        self.assertTrue(hasattr(User(), "created_at"))
        self.assertTrue(hasattr(User(), "updated_at"))
        self.assertTrue(hasattr(User(), "id"))

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
