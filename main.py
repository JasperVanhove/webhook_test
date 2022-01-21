from datetime import datetime
import json
import logging

import websocket

socket = "wss://phemex.com/ws"
interval = 10
ping_start = 0


def _prepare_channel_data():
    return {
        "id": 1234,
        "method": "kline.subscribe",
        "params": [
            "BTCUSD",
            14400
        ]
    }

def _get_ping_payload():
    return json.dumps({
        'id': 1234,
        'method': 'server.ping',
        'params': []
    })

def on_open(ws):
    print(f'Start: {datetime.now()}')

    ws.send(json.dumps({
        'id': 1234,
        'method': 'server.ping',
        'params': []
    }))

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

    # if ping_start == interval:
    #     ping_start = 0
    #     ws.send(json.dumps({
    #         "id": 1234,
    #         "method": "server.ping",
    #         "params": []
    #     }))
    # else:
    #     ping_start += 1

def on_close(ws, test1, test2):
    print(f'End: {datetime.now()}')
    print(test1 + '\n---------------\n' + test2)

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever(ping_interval=interval, ping_payload=_get_ping_payload())
