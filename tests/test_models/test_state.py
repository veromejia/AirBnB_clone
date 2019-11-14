#!/usr/bin/python3
"""Unittest for State class"""

import unittest
import pep8
from os import path, remove
import datetime
from models import base_model
from models import state
from models.base_model import BaseModel
from models.state import State
from models import engine
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):

    """Test Cases for State Class"""
    def setUp(self):
        """Imports module"""
        pass

    # ---------------task 9 ----------------
    def test_pep8(self):
        style_test = pep8.StyleGuide(quiet=True).check_files(['models/state.py'])
        self.assertEqual(style_test.total_errors, 0, "Fix pep8 errors")

    def test_init(self):
        my_state = State()
        self.assertTrue(isinstance(my_state, State))

    def test_sub_class(self):
        my_state = State()
        self.assertTrue(issubclass(my_state.__class__, State))

    def test_attr(self):
        my_state = State()
        self.assertTrue(hasattr(my_state, "name"))

    def test_none(self):
        my_state = State()
        self.assertIsNotNone(my_state.id)
        self.assertIsNotNone(my_state.created_at)
        self.assertIsNotNone(my_state.updated_at)

    def test_inheritance(self):
        my_state = State()
        self.assertTrue(hasattr(my_state, "created_at"))
        self.assertTrue(hasattr(my_state, "updated_at"))
        self.assertTrue(hasattr(my_state, "id"))


    def test_dict(self):
        my_state = State()
        self.assertTrue("to_dict" in dir(my_state))

if __name__ == "__main__":
    unittest.main()
