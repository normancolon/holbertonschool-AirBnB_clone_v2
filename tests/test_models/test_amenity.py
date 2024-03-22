#!/usr/bin/python3
"""
Unit tests for the Amenity class in the HBNB project.
This module tests all functionalities of the Amenity class.
"""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class AmenityTestSuite(unittest.TestCase):
    """Defines the test suite for the Amenity class."""

    @classmethod
    def setUpClass(cls):
        """Initial setup for the Amenity test suite."""
        cls.test_amenity = Amenity()
        cls.test_amenity.name = "High-Speed Internet"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after the entire test suite has run."""
        del cls.test_amenity

    def tearDown(self):
        """Clean up files created during testing."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstrings_presence(self):
        """Checks for the presence of docstrings in the Amenity class."""
        self.assertIsNotNone(Amenity.__doc__)

    def test_amenity_attributes(self):
        """Tests if the Amenity class has the correct attributes."""
        self.assertTrue(hasattr(self.test_amenity, 'id'))
        self.assertTrue(hasattr(self.test_amenity, 'created_at'))
        self.assertTrue(hasattr(self.test_amenity, 'updated_at'))
        self.assertTrue(hasattr(self.test_amenity, 'name'))

    def test_amenity_inheritance(self):
        """Verifies that the Amenity class is a subclass of BaseModel."""
        self.assertIsInstance(self.test_amenity, BaseModel)

    def test_attribute_types(self):
        """Checks the attribute types in Amenity instances."""
        self.assertIsInstance(self.test_amenity.name, str)

    def test_saving_amenity(self):
        """Tests the save functionality of the Amenity class."""
        previous_update_time = self.test_amenity.updated_at
        self.test_amenity.save()
        self.assertNotEqual(previous_update_time, self.test_amenity.updated_at)

    def test_amenity_to_dict(self):
        """Tests the dictionary representation of Amenity instances."""
        self.assertIsInstance(self.test_amenity.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
