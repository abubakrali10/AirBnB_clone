#!/usr/bin/python3
import json
import models
from os import path


class FileStorage():
    """
    The FileStorage class provides:
        storing and retrieving objects in a JSON file.

    Attributes:

    - __file_path: The file path for the JSON file.
    - __objects: A dictionary to store the objects.

    Methods:
    - all(): Returns the dictionary of objects.
    - new(obj): Adds a new object to the dictionary.
    - save(): Saves the dictionary of objects into JSON file.
    - reload(): Reloads the dictionary of objects from JSON file.
    """
    __file_path = 'file.json'
    __objects = {}
    # ex: __objects {'BaseModel.122225454': obj1}

    def all(self):
        """
        Returns:
        - dict: The dictionary of objects (__objects).
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        Adds a new object to the dictionary of objects.

        Args:
        - obj (object): The object to add.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
    
    def save(self):
        """
        Saves the dictionary of objects to the JSON file.
        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            file.write(json.dumps(obj_dict))

    
    def reload(self):
        """
        Reloads the dictionary of objects from the JSON file.
        If the file exists:
            it reads the file and updates the __objects dictionary.
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.loads(file.read())
                for key, value in obj_dict.items():
                    obj = models.classes[value["__class__"]](**value)
                    FileStorage.__objects[key] = obj