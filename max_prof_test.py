import unittest
from max_prof import StockMasta


class TestStockMasta(unittest.TestCase):

    # def test_if_stockMasta_finds_min_and_max(self):
    #     stocks = StockMasta([10, 7, 5, 8, 11, 9])
    #     stocks.find_min_and_max()
    #     self.assertEqual(stocks.min_index, [2])
    #     self.assertEqual(stocks.max_index, [4])

    # def test_if_stockMasta_finds_max_difference_before(self):
    #     stocks = StockMasta([10, 11, 12, 1, 2, 11, 10])
    #     stocks.find_min_and_max()
    #     self.assertEqual(stocks.min_index, [0])
    #     self.assertEqual(stocks.max_index, [2])

    # def test_if_stockMasta_finds_max_difference_after(self):
    #     stocks = StockMasta([10, 11, 12, 1, 2, 11, 10])
    #     stocks.find_min_and_max2()
    #     self.assertEqual(stocks.min_index2, [1])
    #     self.assertEqual(stocks.max_index2, [3])

    # def test_if_stockMasta_finds_max_difference_before2(self):
    #     stocks = StockMasta([10, 10, 10, 10, 10, 10, 10])
    #     stocks.find_min_and_max()
    #     self.assertEqual(stocks.calculator(), 0)

    # def test_if_stockMasta_finds_min_and_max3(self):
    #     stocks = StockMasta([3, 12, 4, 5, 2, 12])
    #     stocks.find_min_and_max()
    #     self.assertEqual(stocks.min_index, [4])
    #     self.assertEqual(stocks.max_index, [5])

    def test_if_stockMasta_finds_max(self):
        stocks = StockMasta([10, 11, 12, 1, 2, 11, 10])
        self.assertEqual(stocks.max_diff(), 10)

    def test_if_stockMasta_finds_max2(self):
        stocks = StockMasta([1, 11, 12, 1, 2, 11, 10])
        self.assertEqual(stocks.max_diff(), 11)


if __name__ == '__main__':
    unittest.main()
