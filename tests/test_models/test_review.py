#!/usr/bin/python3
""" Module for testing class Review"""
import unittest
from models.review import Review
import os


class TestReview(unittest.TestCase):
    """Indiviual test methods for class Review"""

    def __init__(self, *args, **kwargs):
        """ review class init"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ testing review place_id attr"""
        new = self.value()
        self.assertEqual(type(new.place_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_user_id(self):
        """ testing review user_id attr"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

    def test_text(self):
        """ testing review text attr"""
        new = self.value()
        self.assertEqual(type(new.text), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
