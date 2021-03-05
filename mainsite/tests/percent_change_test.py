import unittest
from models.py import Asset


class TestPercentChange(unittest.TestCase):
    def setUp(self):
        asset_name = 'AAPL'
        buy_price = 100
        modified_buy_price = 110
        count = 2

    t1 = percent_changing(buy_price = 100,modified_buy_price = 110  )
         
    self.assertNotEqual(t1,-10)

if __name__ == '__main__':
    unittest.main