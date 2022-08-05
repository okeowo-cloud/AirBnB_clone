#!/usr/bin/python3
"""Test module for FileStorage"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.user import User
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unittest for FileStorage class"""

    def test_instantiation(self):
        """test if instance of class FileStorage"""

        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_accessibility(self):
        """ test the read, write and executable access
        of file_storage"""

        path = "models/engine/file_storage.py"
        rd = os.access(path, os.R_OK)
        self.assertTrue(rd)
        wr = os.access(path, os.W_OK)
        self.assertTrue(wr)
        ex = os.access(path, os.X_OK)
        self.assertTrue(ex)

    def test_new(self):
        """test new object creation"""
        storage = FileStorage()
        obj_dict = storage.all()
        user = User()
        user.id = 1
        user.name = "Sharon"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj_dict[key])

    def test_reload(self):
        """ test object load from file """
        storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as f:
            for line in f:
                self.assertEqual(line, "{}")
        self.assertIs(storage.reload(), None)

    def test_save(self):
        """ test object created are save to file """
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        dict1 = storage.all()
        storage.save()
        storage.reload()
        dict2 = storage.all()
        for key in dict1:
            key1 = key
        for key in dict2:
            key2 = key
        self.assertEqual(dict1[key1].to_dict(), dict2[key2].to_dict())

    def test_doc(self):
        """ test FileStorage contains documentation """
        for attr in dir(FileStorage):
            self.assertTrue(len(attr.__doc__) > 0)


if __name__ == "__main__":
    unittest.main()
