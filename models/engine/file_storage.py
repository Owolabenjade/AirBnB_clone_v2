#!/usr/bin/python3
"""
Contains the FileStorage class model
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class for serializing instances to JSON file
    and deserializing JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns dictionary of all objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = eval(jo[key]["__class__"])(**jo[key])
        except:
            pass

    def close(self):
        """Method for deserializing the JSON file to objects"""
        self.reload()