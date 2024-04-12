#!/usr/bin/python3
"""
Manages JSON storage for models.
"""

import json
from models.base_model import BaseModel
from models import classes


class FileStorage:
    """
    Manages storage of hbnb models in JSON format.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns objects by class type or all objects.
        """
        return {k: v for k, v in self.__objects.items() if not cls or isinstance(v, cls)}

    def new(self, obj):
        """
        Adds objects to the storage dictionary.
        """
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serializes objects to the JSON file.
        """
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Reloads objects from the JSON file.
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                for k, v in json.load(f).items():
                    self.__objects[k] = classes[v['__class__']](**v)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes an object from storage.
        """
        if obj:
            self.__objects.pop(f"{obj.__class__.__name__}.{obj.id}", None)

    def close(self):
        """
        Calls reload method for deserialization.
        """
        self.reload()
