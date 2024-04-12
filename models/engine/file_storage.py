#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        if not cls:
            return self.__objects
        return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review
        }
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                for k, v in json.load(f).items():
                    cls = classes[v['__class__']]
                    self.__objects[k] = cls(**v)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj:
            self.__objects.pop(f"{type(obj).__name__}.{obj.id}", None)

    def close(self):
        self.reload()


if __name__ == "__main__":
    fs = FileStorage()
    fs.reload()
