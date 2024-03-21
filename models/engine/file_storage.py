#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import importlib


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        If cls is provided, returns a dictionary of objects of type cls.
        """
        if cls is not None:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Saves storage dictionary to file"""
        obj_dict = {obj_id: obj.to_dict()
                    for obj_id, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Loads storage dictionary from file.json"""
        classes_dict = {
            'BaseModel': 'base_model.BaseModel',
            'User': 'user.User',
            'Place': 'place.Place',
            'State': 'state.State',
            'City': 'city.City',
            'Amenity': 'amenity.Amenity',
            'Review': 'review.Review'
        }

        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj_id, obj_data in obj_dict.items():
                class_name = obj_data["__class__"]
                module_name, class_name = classes_dict[class_name].split('.')
                module = importlib.import_module(f'models.{module_name}')
                cls = getattr(module, class_name)
                self.__objects[obj_id] = cls(**obj_data)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it’s inside"""
        if obj is not None:
            key = f"{type(obj).__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call reload() method for deserializing the JSON file to objects."""
        self.reload()


storage = FileStorage()
storage.reload()
