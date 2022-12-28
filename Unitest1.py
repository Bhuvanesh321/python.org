from student import Student
import unittest

class New(unittest.TestCase):
    def setUpClass(self):
        print('setupclass')

    def tearDownClass(self):
        print('teardownclass')

    def setUp(self):
        print("\nsetup")

    def tearDown(self):
        print("\nteardown")
