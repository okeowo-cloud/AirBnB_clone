#!/usr/bin/python3
"""City Module"""

from models.base_model import BaseModel


class City(BaseModel):
    """class representation of city module"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize class instance with base class"""
        super().__init__(self, *args, **kwargs)
