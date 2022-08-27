import abc_api
import requests
import websocket
import json
import time

class API(abc_api.Vehicle):
	# get all known trading pairs
	def pairs(self):
		url = "https://api.exchange.coinbase.com/products"
		headers = {"Accept": "application/json"}
		response = requests.get(url, headers=headers)
		json_response = response.json()
		asset_struct = ['base_asset', 'quote_asset', 'symbol', 'base_min_size', 'base_increment', 'quote_increment']
		# base_max_size couldnt be found due to coinbase removing that part of the response
		pair2 = dict()
		r2 = list()
		for pair in list(json_response):
			pair['base_asset'] = pair.pop('base_currency')
			pair['quote_asset'] = pair.pop('quote_currency')
			pair['symbol'] = pair['id']
			pair['base_min_size'] = pair.pop('min_market_funds')
			for struct in asset_struct:
				if struct in pair.keys():
					pair2[struct] = pair[struct]
			r2.append(pair2)
			pair2 = dict()
		json_response = r2
		return json_response

	# get all current trades for product
	def trades(self, product_id, rec=10):
		url = "https://api.exchange.coinbase.com/products/" + product_id + "/trades"
		headers = {"Accept": "application/json"}
		response = requests.get(url, headers=headers)
		json_response = response.json()
		lim = 0
		recent_list = []
		for t in json_response:
			recent_list.append(t)
			lim += 1
			if lim == rec:
				break
		return recent_list
		
	def stats(self, product_id):
		url = 'https://api.exchange.coinbase.com/products/' + product_id + '/stats'
		headers = {"Accept": "application/json"}
		response = requests.get(url, headers=headers)
		json_response = response.json()
		return json_response
