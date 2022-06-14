#!/usr/bin/python3
# test_base.py

"""Defines unittests for base.py

Unittest classes:
     TestBase_instantiation - line23
"""
import unittest

class TestBase_instantiation(unittest.TestCase):
     """Unittests for testing instatiation of the Base Class"""

     def _no_arg(self):
          b1 = Base()
          b2 = Base()
          self.assertEqual(b1.id, b2.id - 1)

if __name__ == "__main__":
    unittest.main()
     