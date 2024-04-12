#!/usr/bin/python3
"""
This module defines a class that manages JSON file storage for the hbnb clone.
"""

import json


class FileStorage:
    """
    Manages storage of hbnb models in JSON format.
    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): dictionary to store all objects by <class name>.id
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        If a class type is provided, returns a dict of all instances of that class.
        If no class type is provided, returns all objects.
        """
        if cls is not None:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """
        Adds new object to the storage dictionary.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the __objects to the JSON file specified by __file_path.
        """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if FileStorage.__file_path exists.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_data = json.load(f)
                from models import classes  # Importing dictionary of classes
                for obj_id, obj_attrs in obj_data.items():
                    cls_name = obj_attrs['__class__']
                    cls = classes[cls_name]
                    self.__objects[obj_id] = cls(**obj_attrs)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it’s inside.
        """
        if obj:
            obj_key = f"{type(obj).__name__}.{obj.id}"
            if obj_key in self.__objects:
                del self.__objects[obj_key]

    def close(self):
        """
        Calls reload() for deserializing the JSON file to objects.
        """
        self.reload()
