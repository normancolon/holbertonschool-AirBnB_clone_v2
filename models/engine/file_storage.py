#!/usr/bin/python3
"""
Defines the FileStorage class for handling serialization and deserialization
of JSON file storage.
"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    Represents an abstracted storage engine for serializing instances to
    a JSON file and deserializing JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file for storing objects.
        __objects (dict): Dictionary to store objects by '<class name>.id'.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Return a dictionary of all stored objects, or all objects of a specific type.

        Args:
            cls (str or type): Class type or name of the objects to return.

        Returns:
            dict: A dictionary of stored objects, possibly filtered by class type.
        """
        if cls:
            cls = eval(cls) if isinstance(cls, str) else cls
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects.copy()

    def new(self, obj):
        """
        Add a new object to the storage dictionary.

        Args:
            obj (BaseModel): Object to add to storage.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serialize the objects in the storage dictionary to the JSON file.
        """
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserialize the JSON file to objects if the file exists.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o.pop('__class__', None)
                    if cls_name:
                        self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delete obj from __objects if it’s inside.

        Args:
            obj (BaseModel): Object to delete from storage.
        """
        obj_key = f"{type(obj).__name__}.{obj.id}"
        self.__objects.pop(obj_key, None)

    def close(self):
        """
        Method for deserialization, alias for reload.
        """
        self.reload()
