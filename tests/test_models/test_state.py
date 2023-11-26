#!/usr/bin/python3
""" Module for testing class State"""
import unittest
from models.state import State
import os


class TestState(unittest.TestCase):
    """ Individual test methods for class State"""

    def __init__(self, *args, **kwargs):
        """ state test class init"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ testing state name attr"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
