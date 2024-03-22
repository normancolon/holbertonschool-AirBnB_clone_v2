#!/usr/bin/python3
"""
Defines unittests for the Place class of the HBNB project.
This includes testing basic functionality, attribute assignments,
and inheritance.
"""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class PlaceTests(unittest.TestCase):
    """Conducts tests on the Place class from the HBNB model."""

    @classmethod
    def setUpClass(cls):
        """Initializes a Place instance for testing."""
        cls.test_place = Place()
        cls.test_place.city_id = "1234-abcd"
        cls.test_place.user_id = "4321-dcba"
        cls.test_place.name = "Death Star"
        cls.test_place.description = "UNLIMITED POWER!!!!!"
        cls.test_place.number_rooms = 1000000
        cls.test_place.number_bathrooms = 1
        cls.test_place.max_guest = 607360
        cls.test_place.price_by_night = 10
        cls.test_place.latitude = 160.0
        cls.test_place.longitude = 120.0
        cls.test_place.amenity_ids = ["1324-lksdjkl"]

    @classmethod
    def tearDownClass(cls):
        """Cleans up the test_place instance after all tests have run."""
        del cls.test_place

    def tearDown(self):
        """Removes the 'file.json' file after each test method."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_docstring_presence(self):
        """Checks for the presence of docstrings."""
        self.assertIsNotNone(Place.__doc__)

    def test_attribute_existence(self):
        """Checks if the necessary attributes exist."""
        self.assertTrue(hasattr(self.test_place, 'id'))
        self.assertTrue(hasattr(self.test_place, 'created_at'))
        self.assertTrue(hasattr(self.test_place, 'updated_at'))
        self.assertTrue(hasattr(self.test_place, 'city_id'))
        # Continue for all attributes...

    def test_place_is_subclass_of_base_model(self):
        """Verifies that Place is a subclass of BaseModel."""
        self.assertIsInstance(self.test_place, BaseModel)

    def test_attribute_types(self):
        """Checks the attribute types of Place instance."""
        self.assertIsInstance(self.test_place.city_id, str)
        # Continue for all attributes...

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db', "Skipping file storage tests")
    def test_save_method(self):
        """Tests the save method of Place."""
        self.test_place.save()
        self.assertNotEqual(self.test_place.created_at,
                            self.test_place.updated_at)

    def test_to_dict_method(self):
        """Tests the to_dict method of Place."""
        self.assertIsInstance(self.test_place.to_dict(), dict)


if __name__ == "__main__":
    unittest.main()
