#!/usr/bin/python3
"""Test Module for Review"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """ tests for review class"""

    def test_instantiation(self):
        """ test instances of a review object """
        obj = Review()
        self.assertIsInstance(obj, Review)

    def test_attributes(self):
        """self attr/properties of a review object """
        self.obj = Review()
        self.assertTrue(hasattr(self.obj, "id"))
        self.assertTrue(hasattr(self.obj, "updated_at"))
        self.assertTrue(hasattr(self.obj, "created_at"))
        self.assertFalse(hasattr(self.obj, "someRandomAttr"))
        self.assertTrue(hasattr(self.obj, "text"))
        self.assertTrue(self.obj.__class__.__name__, "Review")

    def test_save(self):
        """test save method"""
        obj = Review()
        obj.save()
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_str(self):
        """test __str__ method"""
        obj = Review()
        obj_str = "[{}] ({}) {}".format(
                obj.__class__.__name__,
                obj.id,
                obj.__dict__)


if __name__ == "__main__":
    unittest.main()
