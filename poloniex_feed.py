#!/usr/bin/python
# encoding: utf-8

# Cryptotrader poloniex feed 
# Author: Oscar Dionis

from Ohlc import Ohlc
import HistoricalDataCalculations as HDC
import urllib2
import json
from datetime import datetime
from decimal import Decimal



def get_historical_data(pair, timing):
	url = 'https://poloniex.com/public?command=returnChartData&currencyPair=' +  pair + '&start=1333734710&end=9999999999&period=' + timing
	json_response = urllib2.urlopen(url)
	data_json = json_response.readlines()
	return json.loads(data_json[0])

def get_bar_list(historical_data):
    bar_list = []
    for ohlc in historical_data:
        dictionary = {
            'volume': Decimal(ohlc['volume']),
            'quoteVolume': Decimal(ohlc['quoteVolume']),
            'high': Decimal(ohlc['high']),
            'low': Decimal(ohlc['low']),
            'date': str(datetime.fromtimestamp(ohlc['date']).strftime('%Y-%m-%d')),
            'time' : str(datetime.fromtimestamp(ohlc['date']).strftime('%H:%M:%S')),
            'close' : Decimal(ohlc['close']),
            'weightedAverage': Decimal(ohlc['weightedAverage']),
            'open' : Decimal(ohlc['open'])
        }
        bar_list.append (Ohlc(**dictionary))
    return bar_list

def main():
    historical_data = get_historical_data('BTC_ETH', '86400')
    bar_list = get_bar_list(historical_data)

    regr, x0, y0, x1, y1 = HDC.get_regression (1, bar_list, 10)
    print "Yearly regression for daily timing from %s (%f) to %s (%f) is: %s" % (bar_list[x0].date, y0, bar_list[x1].date, y1, regr)


if __name__ == '__main__':
    main()