#!/usr/bin/python3
"""Test Module for Place"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test for Place Class"""

    def test_instantiation(self):
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attr(self):
        """test attributes/properties of Place class"""
        self.place = Place()
        self.assertTrue(hasattr(self.place, "id"))
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertFalse(hasattr(self.place, "randomAttr"))
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_save(self):
        """ test save method """
        place = Place()
        place.save()
        self.assertTrue(hasattr(place, "updated_at"))

    def test_str(self):
        """ test __str__ method """
        place = Place()
        place_str = "[{}] ({}) {}".format(
                place.__class__.__name__,
                str(place.id),
                place.__dict__)
        self.assertEqual(print(place_str), print(place))


if __name__ == "__main__":
    unittest.main()
