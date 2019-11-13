#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Cases for BaseModel Class"""

    def check_name(self):
        """check the name"""
        my_model = BaseModel()
