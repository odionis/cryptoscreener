#!/usr/bin/python
# encoding: utf-8

# Cryptoscreener OHLC class
# Author: Oscar Dionis

class Ohlc():
	def __init__(self, **atr ):
		if ( atr != {}):
			self.set_values(**atr)

	def get_dict(self):
		dictionary = {
			"volume": self.volume,
			"quoteVolume": self.quoteVolume,
			"high": self.high,
			"low": self.low,
			"date": self.date,
			"time": self.time,
			"close": self.close,
			"weightedAverage": self.weightedAverage,
			"open": self.open
		}
		return dictionary

	def set_values(self, **atr):
		self.volume = atr['volume']
		self.quoteVolume = atr['quoteVolume']
		self.high = atr['high']
		self.low = atr['low']
		self.date = atr['date']
		self.time = atr['time']
		self.close = atr['close']
		self.weightedAverage = atr['weightedAverage']
		self.open = atr['open']


	def __repr__(self):
		output = """ Bar info
			Date : %s, %s
			Open : %f
			High : %f
			Low : %f
			Close : %f
			Volume: %f
		""" % (self.date, self.time, self.high, self.low, self.open,self.volume,self.volume)
		return output

