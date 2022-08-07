#!/usr/bin/python3
"""State module"""

from models.base_model import BaseModel


class State(BaseModel):
    """class representation of the state object"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize class instance with base class"""
        super().__init__(self, *args, **kwargs)
