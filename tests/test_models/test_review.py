#!/usr/bin/python3
"""
Unit tests for the Review class in the HBNB project.
"""

import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class ReviewTestCase(unittest.TestCase):
    """Tests for the Review class functionality."""

    @classmethod
    def setUpClass(cls):
        """Initial setup for Review tests."""
        cls.review_instance = Review()
        cls.review_instance.place_id = "4321-dcba"
        cls.review_instance.user_id = "123-bca"
        cls.review_instance.text = "The strongest in the Galaxy"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after all tests have run."""
        del cls.review_instance

    def tearDown(self):
        """Clean up files after each test."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_presence(self):
        """Test if docstrings are present."""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_existence(self):
        """Test the existence of Review attributes."""
        self.assertTrue(hasattr(self.review_instance, 'id'))
        self.assertTrue(hasattr(self.review_instance, 'created_at'))
        self.assertTrue(hasattr(self.review_instance, 'updated_at'))
        self.assertTrue(hasattr(self.review_instance, 'place_id'))
        self.assertTrue(hasattr(self.review_instance, 'user_id'))
        self.assertTrue(hasattr(self.review_instance, 'text'))

    def test_is_subclass_of_base_model(self):
        """Test if Review is a subclass of BaseModel."""
        self.assertIsInstance(self.review_instance, BaseModel)

    def test_attributes_type(self):
        """Verify the attribute types for Review."""
        self.assertIsInstance(self.review_instance.place_id, str)
        self.assertIsInstance(self.review_instance.user_id, str)
        self.assertIsInstance(self.review_instance.text, str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', "Skipping file storage tests")
    def test_save_functionality(self):
        """Test the functionality of the save method."""
        self.review_instance.save()
        self.assertNotEqual(self.review_instance.created_at,
                            self.review_instance.updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method converts to dictionary correctly."""
        self.assertIsInstance(self.review_instance.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
