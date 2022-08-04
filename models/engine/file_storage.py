#!/usr/bin/python3
"""file_storage module for Serializing instances to a JSON file
and Deserializing JSON file to instances"""

import json
import os
import os.path


class FileStorage:
    """Storage Class for object serialization and deserialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the __objects dict"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        name = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[name] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        my_dict = {}
        for keys, val in self.__objects.items():
            my_dict[keys] = val.to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dump(my_dict, json_file)

    def reload(self):
        """Deserializes/load the json_file to objects"""
        from models.base_model import BaseModel
        from models.user import User

        my_dict = {
                "BaseModel": BaseModel,
                "User": User
                }
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r") as file_path:
            objects = json.load(file_path)
            self.__objects = {}
            for key in objects:
                name = key.split(".")[0]
                self.__objects[key] = my_dict[name](**objects[key])
