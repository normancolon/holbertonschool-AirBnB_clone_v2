#!/usr/bin/python3
"""
Module to test the City class functionalities.
"""

import unittest
import os
from models.city import City
from models.base_model import BaseModel


class CityTestSuite(unittest.TestCase):
    """Defines the test suite for the City class."""

    @classmethod
    def setUpClass(cls):
        """Initial setup for the test suite."""
        cls.test_city = City()
        cls.test_city.name = "San Francisco"
        cls.test_city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """Clean up actions after all tests are done."""
        del cls.test_city

    def tearDown(self):
        """Cleans temporary files."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_presence(self):
        """Tests if the docstring is present."""
        self.assertIsNotNone(City.__doc__)

    def test_attribute_existence(self):
        """Tests if City attributes exist."""
        self.assertTrue(hasattr(self.test_city, 'id'))
        self.assertTrue(hasattr(self.test_city, 'created_at'))
        self.assertTrue(hasattr(self.test_city, 'updated_at'))
        self.assertTrue(hasattr(self.test_city, 'state_id'))
        self.assertTrue(hasattr(self.test_city, 'name'))

    def test_inheritance_from_base_model(self):
        """Tests if City is a subclass of BaseModel."""
        self.assertIsInstance(self.test_city, BaseModel)

    def test_attributes_type(self):
        """Tests the type of City attributes."""
        self.assertIsInstance(self.test_city.name, str)
        self.assertIsInstance(self.test_city.state_id, str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', "Skipping file storage tests")
    def test_save_method(self):
        """Tests the functionality of the save method."""
        previous_update = self.test_city.updated_at
        self.test_city.save()
        self.assertNotEqual(previous_update, self.test_city.updated_at)

    def test_to_dict_method(self):
        """Tests if to_dict method is working correctly."""
        self.assertIn('to_dict', dir(self.test_city))


if __name__ == "__main__":
    unittest.main()
