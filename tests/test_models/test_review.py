#!/usr/bin/python3
"""Unittest for Review class"""

import unittest
from models.review import Review
import pep8


class TestReview(unittest.TestCase):

    """Test Cases for Review Class"""
    def setUp(self):
        """Imports module"""
        pass

    # ---------------task 9 ----------------
    def test_pep8(self):
        style_test = pep8.StyleGuide(quiet=True).check_files(['models/user.py'])
        self.assertEqual(style_test.total_errors, 0, "Fix pep8 errors")

    def test_init(self):
        my_review = Review()
        self.assertTrue(isinstance(my_review, Review))

    def test_sub_class(self):
        my_review = Review()
        self.assertTrue(issubclass(my_review.__class__, Review))

    def test_attr(self):
        my_review = Review()
        self.assertTrue(hasattr(my_review, "place_id"))
        self.assertTrue(hasattr(my_review, "user_id"))
        self.assertTrue(hasattr(my_review, "text"))

    def test_none(self):
        my_review = Review()
        self.assertIsNotNone(my_review.id)
        self.assertIsNotNone(my_review.created_at)
        self.assertIsNotNone(my_review.updated_at)

if __name__ == "__main__":
    unittest.main()
