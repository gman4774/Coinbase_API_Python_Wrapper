from abc import ABC, abstractmethod

class Vehicle(ABC):
	
	@abstractmethod 
	def pairs(self):
		pass
	
	@abstractmethod
	def trades(self):
		pass
	@abstractmethod
	def stats(self):
		pass
