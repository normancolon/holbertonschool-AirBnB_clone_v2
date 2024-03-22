#!/usr/bin/python3
"""
Unit test module for the State class in the HBNB project.
Tests the State class' behavior and functionalities.
"""

import unittest
import os
from models.state import State
from models.base_model import BaseModel


class StateTestCase(unittest.TestCase):
    """Defines the test cases for the State class."""

    @classmethod
    def setUpClass(cls):
        """Initial setup for State class tests."""
        cls.test_state = State()
        cls.test_state.name = "New York"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after all tests have run."""
        del cls.test_state

    def tearDown(self):
        """Remove temporary files created during tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_presence(self):
        """Test for existence of docstrings in the State class."""
        self.assertIsNotNone(State.__doc__)

    def test_state_attributes(self):
        """Test if the State class has certain attributes."""
        self.assertTrue(hasattr(self.test_state, 'id'))
        self.assertTrue(hasattr(self.test_state, 'created_at'))
        self.assertTrue(hasattr(self.test_state, 'updated_at'))
        self.assertTrue(hasattr(self.test_state, 'name'))

    def test_state_inheritance(self):
        """Test if State is a subclass of BaseModel."""
        self.assertIsInstance(self.test_state, BaseModel)

    def test_state_attribute_type(self):
        """Test the type of State attributes."""
        self.assertIsInstance(self.test_state.name, str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', "Skipping tests for file storage")
    def test_state_save(self):
        """Test the functionality of the save method."""
        self.test_state.save()
        self.assertNotEqual(self.test_state.created_at,
                            self.test_state.updated_at)

    def test_state_to_dict(self):
        """Test the conversion of State attributes to a dictionary."""
        self.assertTrue('to_dict' in dir(self.test_state))


if __name__ == "__main__":
    unittest.main()
