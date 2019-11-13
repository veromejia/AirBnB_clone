#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
import uuid
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

    # ---------------task 3 ----------------
