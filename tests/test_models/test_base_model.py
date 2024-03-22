#!/usr/bin/python3
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from pycodestyle import StyleGuide


class BaseModelTest(unittest.TestCase):
    """Tests the functionality of the BaseModel class."""

    @classmethod
    def setUpClass(cls):
        """Sets up test environment before each class's tests run."""
        cls.rename_file = os.path.isfile("file.json")
        if cls.rename_file:
            os.rename("file.json", "temp_file.json")
        FileStorage._FileStorage__objects = {}
        cls.model = BaseModel()
        cls.model.name = "Holberton"
        cls.model.my_number = 89

    @classmethod
    def tearDownClass(cls):
        """Cleans up after all tests have run in this class."""
        del cls.model
        FileStorage._FileStorage__objects = {}
        if cls.rename_file:
            os.rename("temp_file.json", "file.json")

    def tearDown(self):
        """Cleans up tasks after each test's run."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_base_model(self):
        """Test that models/base_model.py conforms to PEP 8."""
        style = StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstring_presence(self):
        """Test for existence of docstrings."""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_attribute_creation(self):
        """Test that attributes are correctly created."""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "Holberton")

    def test_id_uniqueness(self):
        """Test that each model's id is unique."""
        model_clone = BaseModel()
        self.assertNotEqual(self.model.id, model_clone.id)

    def test_datetime_attributes(self):
        """Test that time attributes are datetime objects."""
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """Test the string representation method of BaseModel."""
        model_str = str(self.model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn("id", model_str)
        self.assertIn("name", model_str)
        self.assertIn("Holberton", model_str)
        self.assertIn("my_number", model_str)

    def test_save_method(self):
        """Test the save method of BaseModel."""
        old_update_time = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_update_time, self.model.updated_at)

    def test_to_dict(self):
        """Test conversion of model attributes to dictionary for JSON."""
        model_dict = self.model.to_dict()
        self.assertEqual(self.model.__class__.__name__,
                         model_dict['__class__'])
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['name'], "Holberton")
        self.assertEqual(model_dict['my_number'], 89)


if __name__ == "__main__":
    unittest.main()
