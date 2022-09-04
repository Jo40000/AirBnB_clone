#!/usr/bin/python3
"""

import unittest
from models.engine.file_storage import Objects
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    ""Test cases"""

    def test_create_isntance(self):
        """create a new instance"""
        new_city = BaseModel()
        new_o = Objects(new_city.__dict__)
        self.assertInstance(new_o, Objects)


        if __name__ == '__main__':
            unittest.main()
