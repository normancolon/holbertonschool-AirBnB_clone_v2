#!/usr/bin/python3
"""
This module defines a class to manage file storage for the hbnb clone.
It allows for serialization and deserialization of the hbnb models.
"""

import json


class FileStorage:
    """Manages storage of hbnb models in JSON format."""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage.
        If cls is provided, returns a dictionary of objects of type cls.
        """
        if cls:
            return {
                k: v for k, v in self.__objects.items() if isinstance(v, cls)
            }
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes the storage dictionary to the JSON file."""
        obj_dict = {
            obj_id: obj.to_dict() for obj_id, obj in self.__objects.items()
        }
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to the storage dictionary."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }

        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
            for key, value in data.items():
                self.__objects[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it's inside.
        If obj is equal to None, the method does not do anything.
        """
        if obj is not None:
            key = f"{type(obj).__name__}.{obj.id}"
            self.__objects.pop(key, None)

    def close(self):
        """Deserializes the JSON file to objects upon closing."""
        self.reload()
