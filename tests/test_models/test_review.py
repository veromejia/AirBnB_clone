#!/usr/bin/python3
"""Unittest for Review class"""

import unittest
from models.review import Review
import os


class TestReview(unittest.TestCase):

    """Test Cases for Review Class"""
    def setUp(self):
        """Imports module"""
        pass

    # ---------------task 9 ----------------
    def test_init(self):
        my_review = Review()
        self.assertTrue(isinstance(my_review, Review))

    def test_sub_class(self):
        my_review = Review()
        self.assertTrue(issubclass(my_review.__class__, Review))

    def test_inheritance(self):
        my_review = Review()
        self.assertTrue(hasattr(my_review, "place_id"))
        self.assertTrue(hasattr(my_review, "user_id"))
        self.assertTrue(hasattr(my_review, "text"))

if __name__ == "__main__":
    unittest.main()
