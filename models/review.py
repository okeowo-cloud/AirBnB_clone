#!/usr/bin/python3
"""Review Module"""

from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """class representation of review object"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Initialize class instance with base class"""
        super().__init__(self, *args, **kwargs)
