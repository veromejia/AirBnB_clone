#!/usr/bin/python3
"""Unittest for User class"""

import unittest
from models.user import User
import os


class TestUser(unittest.TestCase):

    """Test Cases for User Class"""

    def test_inheritance(self):
        my_user = User()
        self.assertTrue(hasattr(User(), "created_at"))
        self.assertTrue(hasattr(User(), "updated_at"))
        self.assertTrue(hasattr(User(), "id"))

if __name__ == "__main__":
    unittest.main()
