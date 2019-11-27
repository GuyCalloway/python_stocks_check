class StockMasta:
    def __init__(self, input):
        self.stocks = input
        self.min_index = []
        self.max_index = []

    def find_min_and_max(self):
        arr = sort_array(self.stocks)
        min = arr[0]
        max = arr[-1]

        while self.min_index == []:
            self.loop_thru_array(min, max)

    def loop_thru_array(self, min, max):
        print(min)
        print(max)
        for i, x in enumerate(self.stocks):
            if (x == max) and (i != 0):
                self.max_index.append(i)
                print(self.max_index)
            elif (x == min) and (self.index_check()):
                print(self.min_index)
                self.min_index.append(i)

        if self.min_index == []:
            del self.stocks[self.max_index[0]]

    def index_check(self):
        for i in self.max_index:
            for index in self.min_index:
                if index - i < 0:
                    return True
        return False


def sort_array(array1):
    sorted_arr = sorted(array1)
    return sorted_arr
