#!/usr/bin/Python3
"""
Test file for user class
"""

import unittest
from models.amenity import amenity
from models.base_model import BaseModel

class TestClass(unittest.TestCase):
    ""Test case"""
    def test_create_istance(self):
    ""Test cases"""

    def test_create_istance(self):
        """create a new instance"""
        New_state = Amenity()
        self.assertInstance(new_state, Amenity)

        def test_create_istance2(self):
            """create anew instance"""
            new_state = Amenity()
            self.assertIsntance(new_state, BaseModel)


            if __name__ == '__main__':
                unittest.main()
