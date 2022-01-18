from datetime import datetime
from binance import ThreadedWebsocketManager

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        print(f'Start: {datetime.now()}')
        twm = ThreadedWebsocketManager()
        # start is required to initialise its internal loop
        twm.start()

        def handle_socket_message(msg):
            if bool(msg['k']['x']):
                print(f'Close at: {datetime.now()}')

        twm.start_kline_socket(callback=handle_socket_message, symbol='BTCUSDT', interval='1h')
    except Exception as e:
        print(f'End: {datetime.now()}')
        print(f'{e.message}')
        print(f'{e.args}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
