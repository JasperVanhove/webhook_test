from datetime import datetime
import json
import logging

import websocket

socket = "wss://stream.bybit.com/realtime"
interval = 45
ping_start = 0


def _prepare_channel_data():
    return {"op": "subscribe", "args": ["klineV2.240.BTCUSD"]}


def on_open(ws):
    print(f'Start: {datetime.now()}')

    ws.send(json.dumps({'op': 'ping'}))

    channel_data = _prepare_channel_data()

    ws.send(json.dumps(channel_data))


def on_message(ws, message):
    global interval
    global ping_start

    message = json.loads(message)

    print(message)

    # if message and message.get('topic', False) and message.get('data', False):
    #     for i in message['data']:
    #         logging.debug(i)
    # elif message and message.get('success', False):
    #     logging.info(message)

    if ping_start == interval:
        ping_start = 0
        ws.send(json.dumps({'op': 'ping'}))
    else:
        ping_start += 1


def on_close(ws, test1, test2):
    print(f'End: {datetime.now()}')
    print(test1 + '\n---------------\n' + test2)


ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()
