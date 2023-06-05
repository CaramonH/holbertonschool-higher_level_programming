#!/usr/bin/python3
""" This module is a unittest for the Base class """

import unittest
import os
import io
import sys
from models.base import Base


class TestBase(unittest.TestCase):
    """ test class for Base class """
    def setUp(self):
        """ Reset the __nb_objects counter. """
        print("Base setUp")
        self.capture_output = io.StringIO()
        sys.stdout = self. capture_output

        Base._Base__nb_objects = 0
