

class BacktesterService:
    
    #Number of candles to count for computing the average
    SMA_PERIOD = 100
    #% of profit from buy target
    PROFIT_TARGET = 10
    #% below buy target to consider for loss
    STOP_LOSS = 10
    #%below sma
    BUY_TARGET = 10
    STOP_LOSS_THRESHOLD = 0

    def __init__(self, candlesticks, sma_period=BacktesterService.SMA_PERIOD, buy_target=BacktesterService.BUY_TARGET, profit_target=BacktesterService.PROFIT_TARGET, stop_loss=BacktesterService.STOP_LOSS, stop_loss_threshold=BacktesterService.STOP_LOSS_THRESHOLD):
        self.candlesticks = candlesticks
        self.sma_period = sma_period
        self.buy_target = (1 - buy_target) / 100
        self.profit_target = (1 + profit_target) / 100
        self.stop_loss = (1 - stop_loss) / 100
        self.stop_loss_threshold = stop_loss_threshold

    
    
