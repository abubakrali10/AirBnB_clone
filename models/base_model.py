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
