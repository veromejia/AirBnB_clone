#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Cases for BaseModel Class"""

    def create(self):
        """ banana """
        new = BaseModel()
        new.name = "test"
