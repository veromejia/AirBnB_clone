#!/usr/bin/python3
"""base Module for the AirBnB clone"""


import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes in the project"""

    def __init__(self, *args, **kwargs):
        """inicializating BaseModel instance"""

        if kwargs and len(kwargs) > 0:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime\
                    (kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime\
                    (kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of BaseModel class"""

        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Update the updated_at attribute with new"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of BaseModel class"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.updated_at.isoformat()
        my_dict["updated_at"] = self.created_at.isoformat()
        return my_dict
