#!/usr/bin/python3
"""Test module for User"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """tests for amenity class"""

    def test_instantiation(self):
        """tests instances of user object"""
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

    def test_attr(self):
        """tests attributes of the user object"""
        self.obj = Amenity()
        self.assertTrue(hasattr(self.obj, "id"))
        self.assertTrue(hasattr(self.obj, "created_at"))
        self.assertTrue(hasattr(self.obj, "updated_at"))
        self.assertFalse(hasattr(self.obj, "extra"))
        self.assertTrue(self.obj.__class__.__name__, "User")

    def test_save(self):
        """tests save method"""
        obj = Amenity()
        obj.save()
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_str(self):
        """test __str__ method"""
        obj = Amenity()
        obj_str = "[{} ({}) {}".format(
                obj.__class__.__name__,
                obj.id,
                obj.__dict__)


if __name__ == "__main__":
    unittest.main()
