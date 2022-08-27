import api
import websocket
from dateutil.parser import isoparse
import requests
import _thread
import json
import time

#example code for getting data from the API and coinbase websocket
ws_url = 'wss://ws-feed.pro.coinbase.com'
channel = 'ticker'
product_id = 'BTC-USD'
trade_count = 3
count = 100

p = api.API() 
all_pairs = p.pairs()
product_trades = p.trades(product_id, trade_count)

pairs_loc = {}
pos = 0

print('All trading pairs: ')

for x in all_pairs:
	for y in x:
		if y == 'symbol':
			pairs_loc[x[y]] = pos
			print(x[y])
	pos += 1
print(' ')
print('All recent product trades: ')
for trade in product_trades:
	print(trade)

def listinlist(lst):
	return [[el] for el in lst]

new_pairs = listinlist(all_pairs)

# WebSocket functions
def ws_message(ws, message):
	data = json.loads(message)
	if('side' and 'last_size') in data.keys():
		new_pairs[pairs_loc[product_id]].append(data)

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
	ws = websocket.WebSocketApp(ws_url, on_open = ws_open, on_message = ws_message)
	ws.run_forever()

# Start a new thread for the WebSocket interface
_thread.start_new_thread(ws_thread, ())

# Continue other (non WebSocket) tasks in the main thread
while True:
	time.sleep(3)
	ws.close()
	break
print(' ')
print('Trading pair data with websocket data: ') 
for x in new_pairs[pairs_loc[product_id]]:
	print(x)


