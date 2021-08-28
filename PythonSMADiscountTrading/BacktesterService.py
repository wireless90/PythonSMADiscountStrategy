

class BacktesterService:
    
    #Number of candles to count for computing the average
    SMA_PERIOD = 100
    #% of profit from buy target
    PROFIT_TARGET = 10

    #%below sma
    BUY_TARGET_1 = 2.5
    PROFIT_TARGET_1 = 2.5
    BUY_TARGET_2 = 5
    PROFIT_TARGET_2 = 5

    def __init__(self, candlesticks, sma_period=SMA_PERIOD, buy_target_1=BUY_TARGET_1, buy_target_2=BUY_TARGET_2, profit_target_1=PROFIT_TARGET_1, profit_target_2=PROFIT_TARGET_2):
        self.candlesticks = candlesticks
        self.sma_period = sma_period
        self.buy_target_1 = (1 - buy_target_1) / 100
        self.buy_target_2 = (1 - buy_target_2) / 100
        self.profit_target_1 = (1 + profit_target_1) / 100
        self.profit_target_2 = (1 + profit_target_2) / 100
        self.cursor = 0
        self.sma = 0.0;
        self.trades = []
        self.buy_1_allowed = True
        self.buy_2_allowed = True

    def start(self): 
        while self.sma != -1:
            self.__compute_sma()
            print(self.sma)
            # Code here


            self.cursor += 1


    pass

    # private functions

    def __has_enough_candlesticks(self):
        candlesticks_left = len(self.candlesticks) - self.cursor
        return candlesticks_left > self.sma_period
    

    def __compute_sma(self):
        if self.__has_enough_candlesticks() == False:
            self.sma = -1
            return self.sma;

        candlesticks = self.candlesticks[self.cursor:(self.cursor+self.sma_period)]
        computed_sum = sum([candlestick.close for candlestick in candlesticks])
        self.sma = computed_sum / self.sma_period
