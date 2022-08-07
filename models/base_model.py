#!/usr/bin/python3
"""
Module base_model
Class defines all common attributes or methods for other classes
"""

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """ Defines a base class for other classes """

    def __init__(self, *args, **kwargs):
        """ Initialize a base model """
        dtf = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key in kwargs:
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(kwargs[key], dtf))
                elif key != '__class__':
                    setattr(self, key, kwargs[key])

    def save(self):
        """ update "updated_at" to recent time object was modified """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        dictionary representation of base object
        """
        dic = {"__class__": self.__class__.__name__}
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic

    def __str__(self):
        """
        string representation of base object
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)
