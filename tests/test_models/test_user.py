#!/usr/bin/python3
"""
Unittest for User class
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):

    """
    Test Cases for User Class
    """

    def check_name(self):
        """ banana """
        my_user = User()
        my_model.last_name = "Banana"
