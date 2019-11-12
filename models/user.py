#!/usr/bin/python3
"""user Module for AirbnB clone"""


from models.base_model import BaseModel


class User:
    """User inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
