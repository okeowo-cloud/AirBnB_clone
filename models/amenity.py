#!/usr/bin/python3
"""Amenity module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class representation of Amenity object"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize class instance with base class"""
        super().__init__(self, *args, **kwargs)
