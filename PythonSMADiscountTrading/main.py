from CandleStickService import CandleStickManager
from BinanceService import BinanceService
from CredentialService import CredentialService



def menu_prompt():
    available_options = [1, 2]

    print("1. Backtest Strategy")
    print("2. Execute Strategy")
    
    try:
        option = int(input("Choose an option"))
        if option not in available_options:
            raise ValueError
    except ValueError as ve:
        print("Not an integer...")
        return

    return option

def run_backtest(binance_service):
    client = binance_service.get_client()
    symbols = [symbol_data['symbol'] for symbol_data in binance_service.get_all_symbols()]
    symbol = input('Select a symbol: ').upper()
    if symbol not in symbols:
        print('Invalid Symbol')
        return

    candlesticks = CandleStickManager.get_candle_sticks(client, symbol)
    print('Running Backtest')
    pass

def run_strategy(client):
    print('Running Strategy')
    pass

OPTIONS = [run_backtest, run_strategy]    

def main():
    option = menu_prompt()
    binance_service = BinanceService(CredentialService.API_KEY, CredentialService.API_SECRET)

    if option is not None:
        OPTIONS[option-1](binance_service)
       
    

if __name__ == '__main__':
    main();


