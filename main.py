from datetime import datetime
import websocket, json

socket = "wss://stream.bybit.com/realtime"
interval = 45
ping_start = 0

def _prepare_channel_data():
    return {"op": "subscribe", "args": ["klineV2.1.BTCUSD"]}


def on_open(ws):
    print(f'Start: {datetime.now()}')

    ws.send(json.dumps({'op': 'ping'}))

    channel_data = _prepare_channel_data()

    ws.send(json.dumps(channel_data))


def on_message(ws, message):
    global interval
    global ping_start

    if ping_start == interval:
        ping_start = 0
        ws.send(json.dumps({'op': 'ping'}))
    else:
        ping_start += 1

    print(message)


def on_close(ws):
    print(f'End: {datetime.now()}')

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()
