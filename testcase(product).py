import unittest
from Example import Products

class Bhuvi_methods(unittest.TestCase):
    def setUp(self):
        print("setUp")
        self.obj = Products("Boost",200,5,50)
        self.assertEqual(obj.deal_price, 150)
        obj.deal_price()

if __name__=='__main__':
    unittest.main()