

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

    def __init__(self, candlesticks, sma_period=BacktesterService.SMA_PERIOD, buy_target_1=BacktesterService.BUY_TARGET_1, buy_target_2=BacktesterService.BUY_TARGET_2, profit_target_1=BacktesterService.PROFIT_TARGET_1, profit_target_2=BacktesterService.PROFIT_TARGET_2):
        self.sma_period = sma_period
        self.buy_target_1 = (1 - buy_target_1) / 100
        self.buy_target_2 = (1 - buy_target_2) / 100
        self.profit_target_1 = (1 + profit_target_1) / 100
        self.profit_target_2 = (1 + profit_target_2) / 100
        self.cursor = 0
    
    def start(self): 
        if self.__has_enough_candlesticks() == False:
            return 0

        while self.cursor < len(self.candlesticks):
            sma = self.__compute_sma()
            self.cursor += 1


    pass

    # private functions

    def __has_enough_candlesticks(self):
        return len(self.candlesticks) > self.sma_period
    

    def __compute_sma(self):
        sum([candlestick.close for candlestick in self.candlesticks]) / BacktesterService.SMA_PERIOD
