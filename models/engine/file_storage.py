#!/usr/bin/python3
"""FileStorage Module"""


import json
import models
import os
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Class that serializes instances to a JSON file
    and deserializes JSON file to instances:"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """sets the obj with id value"""

        key = "{}.{}".format(type(obj).__name__, str(obj.id))
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        my_dictionary = {}
        for key, value in self.__objects.items():
            my_dictionary[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding="UTF8") as f:
            json.dump(my_dictionary, f)

    def reload(self):
        """deserializes the JSON file to __objects"""

        try:
            with open(self.__file_path) as f:
                for key, value in json.load(f).items():
                    self.__objects[key] = eval(value["__class__"])(**(value))
        except:
            pass
