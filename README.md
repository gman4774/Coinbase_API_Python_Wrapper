
# Small python wrapper for Coinbase API

This is a python wrapper for Coinbase API.

## Getting started

import API

- API has two methods(third in branch) 
- **pairs()** and **trades()**
- branch has **stats()**


## Features

- **pairs()** takes no arguments, it returns all trading pairs on Coinbase
- **trades()** takes 2 arguments, product_id(ex. 'BTC-USD') and trade_count(optional, default is 10)
- **stats()** takes 1 argument, product_id(ex. 'BTC-USD')
- Although this wrapper does not have websocket integration, sample code is included in the **examples.py** file

## Files

- **examples.py**  Example code to use the API. (all pairs, recent trades, websocket use)
- **test_sample.py** testfile to be used wiht pytest

