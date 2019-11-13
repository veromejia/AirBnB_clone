#!/usr/bin/python3
"""Unittest for FileStorage class"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json
import os


class TestFileStorage(unittest.TestCase):

    """Test Cases for FileStorage Class"""
