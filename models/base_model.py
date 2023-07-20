#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for models.

    Attributes:
        id (str):
        Unique identifier generated using UUID.
        created_at (datetime):
        Datetime object representing the creation time of the instance.
        updated_at (datetime):
        Datetime object representing the last update time of the instance.

    Methods:
        __init__(): Initializes a new instance of the BaseModel class.
        __str__(): Returns a string representation of the instance.
        save(): Updates the updated_at attribute with the current datetime.
        to_dict(): Converts the instance to a dictionary representation.

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        It generates a unique ID using UUID,
        and sets the created_at and updated_at attributes
        with the current datetime.
        if kwargs is provided:
            Initialize a new instance using the dict passed to init
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: String representation of the instance in the format
            "[ClassName] (id) attribute_dict".
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the instance.
        """
        dict_repr = {}
        dict_repr['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ('created_at', 'updated_at'):
                dict_repr[key] = value.isoformat()
            else:
                dict_repr[key] = value
        return dict_repr
