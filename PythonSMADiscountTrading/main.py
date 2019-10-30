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

def run_backtest():
    print('Running Backtest')
    pass

def run_strategy():
    print('Running Strategy')
    pass

OPTIONS = [run_backtest, run_strategy]    

def main():
    option = menu_prompt()

    if option is not None:
        OPTIONS[option-1]()
       
    

if __name__ == '__main__':
    main();


