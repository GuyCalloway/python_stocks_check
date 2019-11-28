from itertools import combinations


class StockMasta:
    def __init__(self, input):
        self.stocks = input

    def max_diff(self):
        result = max(combinations(self.stocks, 2),
                     key=lambda sub: sub[1]-sub[0])
        return result[1] - result[0]
