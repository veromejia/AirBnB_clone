#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import time
from datetime import datetime, date, time
from time import sleep
import models
import os


class TestBaseModel(unittest.TestCase):
    """Test Cases for BaseModel Class"""

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

    def test_id_uuid(self):
        """ checks the type of id is string uuid"""

        my_model = BaseModel()
        self.assertEqual(str(type(my_model)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(my_model), BaseModel))

    def test_id_args(self):
        """check id is not none, and type string"""

        my_model = BaseModel()
        self.assertNotEqual(len(my_model.id), 0)
        self.assertEqual(len(my_model.id), 36)
        self.assertEqual(type(my_model.id), str)

    def test_different_id(self):
        """ testing option with dif id"""
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)
        self.assertEqual(len(id1.id), len(id2.id))

    def test_type(self):
        """ testing the type of the attributes """
        my_model = BaseModel()
        self.assertTrue(type(my_model), BaseModel)
        my_model.name = "Holberton"
        self.assertEqual(my_model.name, "Holberton")
        self.assertTrue(type(my_model.name), str)
        my_model.my_number = 89
        self.assertEqual(my_model.my_number, 89)
        self.assertTrue(type(my_model.my_number), int)
        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)

    def test_create_at_str(self):
        """ check is if a str"""

        my_model = BaseModel()
        temp = my_model.to_dict()['created_at']
        self.assertEqual(type(temp), str)

    def test_create_at_datetime(self):
        """ test datetime in create attribute"""

        my_model = BaseModel()
        my_dict = my_model.to_dict()
        new_model = BaseModel(my_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime))

    def test_str(self):
        """ test str attribute"""

        my_model = BaseModel()
        a = "[{}] ({}) {}".\
            format(my_model.__class__.__name__, my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), a)

    def test_save(self):
        """ testing save method"""

        my_model = BaseModel()
        new_time = datetime.now()
        my_model.save()
        self.assertNotEqual(my_model.updated_at, new_time)

    def test_class(self):
        """testing BaseModel"""

        my_model = BaseModel()
        self.assertEqual(my_model.__class__.__name__, 'BaseModel')

    def test_to_dict(self):
        """ dictionary conversion """
        my_modl = BaseModel()
        my_modl.name = "Holberton"
        my_modl.my_number = 89
        my_json = my_modl.to_dict()
        self.assertEqual(my_json["id"], my_modl.id)
        self.assertEqual(my_json["name"], "Holberton")
        self.assertEqual(my_json["my_number"], 89)
        self.assertEqual(my_json["__class__"], "BaseModel")
        self.assertEqual(my_json["created_at"], my_modl.created_at.isoformat())
        self.assertEqual(my_json["updated_at"], my_modl.updated_at.isoformat())

    def test_to_dict_attr(self):
        """ created_at, updated_at values """

        b = BaseModel()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        d = b.to_dict()
        self.assertEqual(d["created_at"], b.created_at.strftime(time_format))
        self.assertEqual(d["updated_at"], b.updated_at.strftime(time_format))
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(type(d["created_at"]), str)
        self.assertEqual(type(d["updated_at"]), str)

    # -----------task 4 --------------------

    def test_init(self):
        """testing init method"""

        my_model = BaseModel()
        self.assertTrue(isinstance(my_model, BaseModel))

    def test_init_id(self):
        """testing init id"""

        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, my_model.id)

if __name__ == "__main__":
    unittest.main()
