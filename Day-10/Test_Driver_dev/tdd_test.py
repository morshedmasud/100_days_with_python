"""Unit Test """

import unittest
import math_class
import s_class

class math_classTestCase(unittest.TestCase):
    def test_add(self):
        total = math_class.add(5, 6)
        self.assertEqual(total, 11)

    def test_sub(self):
        result = math_class.sub(100, 20)
        self.assertEqual(result, 80)

class s_classTestCase(unittest.TestCase):
    def test_show(self):
        n = "masud"
        name = s_class.NameString("masud").show()
        self.assertEqual("my name is masud", name)

if __name__ == '__main__':
    unittest.main()

