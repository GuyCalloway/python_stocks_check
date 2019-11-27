import unittest
from max_prof import StockMasta


class TestStockMasta(unittest.TestCase):

    def test_if_stockMasta_finds_min(self):
        stocks = StockMasta([10, 7, 5, 8, 11, 9])
        stocks.find_min_and_max()
        self.assertEqual(stocks.min_index, 5)
        self.assertEqual(stocks.max_index, 11)

    # def test_if_stockMasta_finds_max(self):
    #     stocks = StockMasta([10, 7, 5, 8, 11, 9])
    #     self.assertEqual(stocks.max_index, 11)

    # def test_if_sum_work(self):
    #     result = Hello("whaterver")
    #     result.calculator(1, 2)
    #     self.assertEqual(result.sum, 3)


if __name__ == '__main__':
    unittest.main()
