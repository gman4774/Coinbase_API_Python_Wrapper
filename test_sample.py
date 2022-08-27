import api
import websocket
from dateutil.parser import isoparse
import requests
import _thread
import json
import time

#pytest setup 

ws_url = 'wss://ws-feed.pro.coinbase.com'
channel = 'ticker'
product_id = 'BTC-USD'
trade_count = 3
sample_data = []

p = api.API() 

# WebSocket functions
def ws_message(ws, message):
	data = {}
	data = json.loads(message)
	if('side' and 'last_size') in json.loads(message).keys():
		sample_data.append(data)
		

def ws_open(ws):
	ws.send(json.dumps(
			{
				"type": "subscribe",
				"product_ids": [product_id],
				"channels": [channel],
			}

	))

	
def ws_thread(*args):
	global ws
	global ws_data
	ws = websocket.WebSocketApp(ws_url, on_open = ws_open, on_message = ws_message)
	ws.run_forever()

# Start a new thread for the WebSocket interface
_thread.start_new_thread(ws_thread, ())


# Continue other (non WebSocket) tasks in the main thread
while True:
	product_trades = p.trades(product_id, 1)
	time.sleep(1)
	ws.close()
	break
	
	
for d in sample_data:
	d['epoch'] = isoparse(d['time']).timestamp()
	
sample_data.sort(key=lambda x: x['epoch'], reverse=True)



def test_data():
	for d in sample_data:
		assert ('side' and 'last_size') in d
def test_date():
	current = 0
	previous = 99999999999999999999999999
	for d in sample_data:
		current = d['epoch']
		assert current <= previous
		previous = current


print('Product trades: ')
print(product_trades)
print(' ')
print('Websocket data epoch: ')
for d in sample_data:
	print(d['epoch'])


