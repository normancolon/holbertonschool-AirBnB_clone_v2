#!/usr/bin/python3
"""
Unit tests for the User class in the HBNB project.
"""

import unittest
import os
from models.user import User
from models.base_model import BaseModel


class UserTestCase(unittest.TestCase):
    """Defines test cases for the User class functionality."""

    @classmethod
    def setUpClass(cls):
        """Initial setup for User tests."""
        cls.test_user = User()
        cls.test_user.first_name = "Alex"
        cls.test_user.last_name = "Smith"
        cls.test_user.email = "alex@example.com"
        cls.test_user.password = "secure"

    @classmethod
    def tearDownClass(cls):
        """Clean up resources after tests run."""
        del cls.test_user

    def tearDown(self):
        """Remove temporary files after each test."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_presence(self):
        """Test if there are docstrings."""
        self.assertIsNotNone(User.__doc__)

    def test_user_attributes_existence(self):
        """Test the existence of User attributes."""
        self.assertTrue(hasattr(self.test_user, 'email'))
        self.assertTrue(hasattr(self.test_user, 'id'))
        self.assertTrue(hasattr(self.test_user, 'created_at'))
        self.assertTrue(hasattr(self.test_user, 'updated_at'))
        self.assertTrue(hasattr(self.test_user, 'password'))
        self.assertTrue(hasattr(self.test_user, 'first_name'))
        self.assertTrue(hasattr(self.test_user, 'last_name'))

    def test_user_inheritance(self):
        """Test if User is a subclass of BaseModel."""
        self.assertIsInstance(self.test_user, BaseModel)

    def test_user_attribute_types(self):
        """Verify the type of User attributes."""
        self.assertIsInstance(self.test_user.email, str)
        self.assertIsInstance(self.test_user.password, str)
        self.assertIsInstance(self.test_user.first_name, str)
        self.assertIsInstance(self.test_user.last_name, str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', "Skipping file storage test")
    def test_save_method(self):
        """Test the save method of a User."""
        self.test_user.save()
        self.assertNotEqual(self.test_user.created_at,
                            self.test_user.updated_at)

    def test_to_dict_method(self):
        """Test conversion of User attributes to dictionary."""
        self.assertIsInstance(self.test_user.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
