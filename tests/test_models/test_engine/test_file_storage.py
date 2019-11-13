#!/usr/bin/python3
"""Unittest for FileStorage class"""

import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json
import os


class TestFileStorage(unittest.TestCase):

    """Test Cases for FileStorage Class"""
    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    # ---------------task 5 ----------------
    def test_file_path(self):
        my_storage = FileStorage()
        self.assertTrue(isinstance(my_storage._FileStorage__file_path, str))

    def test_all(self):
        my_storage = FileStorage()
        objects = my_storage.all()
        self.assertTrue(isinstance(objects, dict))

    def test_all_not_none(self):
        my_storage = FileStorage()
        objects = my_storage.all()
        self.assertIsNotNone(objects)

    def test_all_object_attr(self):
        my_storage = FileStorage()
        objects = my_storage.all()
        self.assertIs(objects, my_storage._FileStorage__objects)

    def test_new(self):
        my_storage = FileStorage()
        my_base = BaseModel()
        my_storage.new(my_base)
        key = my_base.__class__.__name__ + '.' + str(my_base.id)
        self.assertIn(key, my_storage._FileStorage__objects.keys())

    def test_save(self):
        my_storage = FileStorage()
        my_base = BaseModel()
        my_storage.new(my_base)
        my_storage.save()
        key = my_base.__class__.__name__ + '.' + my_base.id
        with open("file.json", mode='r') as f:
            my_dict = json.load(f)
        self.assertIn(key, my_dict.keys())

    def test_reload(self):
        my_storage = FileStorage()
        my_base = BaseModel()
        my_storage.new(my_base)
        my_storage.save()
        my_storage.reload()
        key = my_base.__class__.__name__ + '.' + my_base.id
        with open("file.json", mode='r') as f:
            my_dict = json.load(f)
        self.assertIn(key, my_dict.keys())

if __name__ == "__main__":
    unittest.main()
