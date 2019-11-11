#!/usr/bin/python3
"""Review Module for AirbnB clone"""


from models.base_model import BaseModel


class Review(Base_model):
    """Review inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
