#!/usr/bin/python3
"""
FileStorage Engine for storing and managing AirBnB objects
"""
import json
from models.base_model import BaseModel

class FileStorage:
    """
    FileStorage class that handles storage of objects in a JSON file
    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """
        Returns the dictionary of all stored objects
        """
        return self.__objects

    def reload(self):
        """
        Reloads data from the JSON file and updates __objects
        """
        try:
            with open(self.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass

    def close(self):
        """
        Calls the reload method to deserialize the JSON file to objects
        """
        self.reload()
