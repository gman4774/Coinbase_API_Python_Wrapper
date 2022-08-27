import api
import websocket
from dateutil.parser import isoparse
import requests
import _thread
import json
import time

# code for getting product stats from API
product_id = 'BTC-USD'

p = api.API() 
stats = p.stats(product_id)
print('Product stats: ') 
for x in stats:
	print(x, stats[x])


