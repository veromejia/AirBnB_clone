#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import models
import os

class TestBaseModel(unittest.TestCase):

    """Test Cases for BaseModel Class"""

    def setUp(self):
        """Imports module"""
        pass

    # ---------------task 3 ----------------

    def test_id_uuid(self):
        """ checks the type of id is string uuid"""

        my_model = BaseModel()
        self.assertEqual(str(type(my_model)), "<class 'models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(my_model), BaseModel))

    def test_id_args(self):
        """check id is not none, and type string"""

        my_model = BaseModel()
        self.assertNotEqual(len(my_model.id), 0)
        self.assertEqual(len(my_model.id), 36)
        self.assertEqual(type(my_model.id), str)

    def test_creat_at_str(self):
        my_model = BaseModel()
        temp = my_model.to_dict()['created_at']
        self.assertEqual(type(temp), str)

    def test_creat_at_datetime(self):
        my_model = BaseModel()
        my_dict = my_model.to_dict()
        new_model = BaseModel(my_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime))

    def test_str(self):
        my_model = BaseModel()
        a = "[{}] ({}) {}".\
            format(my_model.__class__.__name__, my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), a)

    def test_save(self):
        my_model = BaseModel()
        new_time = datetime.now()
        my_model.save()
        self.assertNotEqual(my_model.updated_at, new_time)

    def test_dict_created(self):
        my_model = BaseModel()
        self.assertTrue("created_at" in my_model.to_dict())


    # -----------task 4 --------------------

    def test_init(self):
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, my_model.id)

if __name__ == "__main__":
    unittest.main()