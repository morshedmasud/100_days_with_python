from main import *
import unittest

class MyTest(unittest.TestCase):

    def test_mkdir(self):
        self.assertEqual(create_directory("masud"), None)



if __name__ == "__main__":
    unittest.main()


