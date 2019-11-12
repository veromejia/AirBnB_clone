#!/usr/bin/python3
"""user Module for AirbnB clone"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User inherits from BaseModel

    Public Attributes:
    (str) email: empty
    (str) password: empty
    (str) first_name: empty
    (str) last_name: empty
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
