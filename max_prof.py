class StockMasta:
    def __init__(self, input):
        self.stocks2 = input
        self.stocks = input
        self.min_index = []
        self.max_index = []
        self.min_index2 = []
        self.max_index2 = []

    def find_min_and_max(self):
        arr = sort_array(self.stocks)
        min = arr[0]
        max = arr[-1]
        while not self.index_check(self.min_index, self.max_index):
            self.loop_thru_array(
                self.stocks, self.min_index, self.max_index, min, max)
            if self.stocks.index(min) > (len(self.stocks) - (self.stocks[::-1].index(max)+1)):
                del self.stocks[self.stocks.index(min)]
                del arr[0]
                del self.min_index[0]
                del self.max_index[0]
                min = arr[0]
        if self.index_check(self.min_index, self.max_index):
            self.min_index = [self.min_index[0]]
            self.max_index = [self.max_index[-1]]
            return(arr[-1] - arr[0])

    def find_min_and_max2(self):
        arr = sort_array(self.stocks2)
        min = arr[0]
        max = arr[-1]
        while not self.index_check(self.min_index2, self.max_index2):
            self.loop_thru_array(
                self.stocks2, self.min_index2, self.max_index2, min, max)
            if self.stocks2.index(max) < self.stocks2.index(min):
                del self.stocks2[self.stocks2.index(max)]
                del arr[-1]
                print(arr)
                del self.min_index2[0]
                del self.max_index2[0]
                max = arr[-1]
        if self.index_check(self.min_index2, self.max_index2):
            self.min_index2 = [self.min_index2[0]]
            self.max_index2 = [self.max_index2[-1]]
            print(arr)
            print(self.stocks2)
            print(arr[-1])
            print(arr[0])
            return (arr[-1] - arr[0])

    def loop_thru_array(self, array, min_index, max_index, min, max):
        for i, x in enumerate(self.stocks):
            if (x == max) and (i != 0):
                max_index.append(i)
            elif (x == min):
                min_index.append(i)

    def index_check(self, min_index, max_index):
        for i in max_index:
            for index in min_index:
                if index - i < 0:
                    return True
        return False

    def calculator(self):
        x = self.find_min_and_max()
        y = self.find_min_and_max2()
        print("yyyyyyy")
        print(y)
        if x < y:
            return y
        else:
            return x


def sort_array(array1):
    sorted_arr = sorted(array1)
    return sorted_arr
