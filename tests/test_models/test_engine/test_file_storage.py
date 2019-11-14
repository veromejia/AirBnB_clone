#!/usr/bin/python3
"""Unittest for FileStorage class"""

import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import pep8
import json
import os


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """sepup class"""
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        """teardownclass"""
        print('teardownClass')

    def setUp(self):
        """setup method"""
        self.my_storage = FileStorage()

    def tearDown(self):
        """tearDown"""
        print('tearDown\n')

# ---------------task 5 ----------------
    def test_file_path(self):
        self.assertTrue(isinstance(self.my_storage._FileStorage__file_path, str))

    def test_all(self):
        objects = self.my_storage.all()
        self.assertTrue(isinstance(objects, dict))

    def test_all_not_none(self):
        objects = self.my_storage.all()
        self.assertIsNotNone(objects)

    def test_all_object_attr(self):
        objects = self.my_storage.all()
        self.assertIs(objects, self.my_storage._FileStorage__objects)

    def test_new(self):
        my_base = BaseModel()
        self.my_storage.new(my_base)
        key = my_base.__class__.__name__ + '.' + str(my_base.id)
        self.assertIn(key, self.my_storage._FileStorage__objects.keys())

    def test_save(self):
        my_base = BaseModel()
        self.my_storage.new(my_base)
        self.my_storage.save()
        key = my_base.__class__.__name__ + '.' + my_base.id
        with open("file.json", mode='r') as f:
            my_dict = json.load(f)
        self.assertIn(key, my_dict.keys())

    def test_reload(self):
        my_base = BaseModel()
        self.my_storage.new(my_base)
        self.my_storage.save()
        self.my_storage.reload()
        key = my_base.__class__.__name__ + '.' + my_base.id
        with open("file.json", mode='r') as f:
            my_dict = json.load(f)
        self.assertIn(key, my_dict.keys())

    def test_pep8(self):
        style_test = pep8.StyleGuide(quiet=True).check_files(['models/engine/file_storage.py'])
        self.assertEqual(style_test.total_errors, 0, "Fix pep8 errors")
if __name__ == "__main__":
    unittest.main()
