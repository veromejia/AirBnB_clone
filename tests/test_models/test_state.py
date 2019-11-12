#!/usr/bin/python3
"""Unittest for State class"""

import unittest
from models.state import State
import os


class TestState(unittest.TestCase):

    """Test Cases for State Class"""

    def setUp(self):
        """Imports module"""
        pass

    # ---------------task 8 ----------------
    def test_init(self):
        my_state = State()
        self.assertTrue(isinstance(my_state, State))

    def test_sub_class(self):
        my_state = State()
        self.assertTrue(issubclass(my_state.__class__, State))

    def test_inheritance(self):
        my_state = State()
        self.assertTrue(hasattr(my_state, "name"))

if __name__ == "__main__":
    unittest.main()
