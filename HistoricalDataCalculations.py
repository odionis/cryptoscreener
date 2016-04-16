#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Cryptoscreener Historical Data Calculation Library
# Author: Oscar Dionis

import math
from decimal import *

class Element():
	def __init__( self, value = -1, position = -1 ):
		self.value = Decimal(value)
		self.position = position

	def __repr__(self):
		output = """ -> Value: %f ; Position: %d""" % (self.value,self.position)
		return output


def get_entry_point (SE, SD, pos):

	if SE.position - SD.position == 0:
		SE.position = 1
		SD.position = 0
	if SE.value > 0 and SD.value > 0:
		if(SE.position == SD.position):
			return Element(0,0)
		b = (math.log(SE.value, 2) - math.log(SD.value, 2)) / (SE.position - SD.position)
		dividend = (2**(b*SE.position))
		if dividend == 0:
			dividend = 1
		a = Decimal(str(SE.value)) / Decimal(str(dividend))
		oper = b*pos
		y = a * Decimal(str(2**(b*pos)))
		return Element(y,pos)
	else:
		return Element(0,0)


def get_regression ( timing, Bar_list, num_total ):

	stop_point = len(Bar_list)-1
	if num_total < stop_point:
		start_point = stop_point - num_total
	else:
		start_point = 0
	m = 0
	x = 0
	xy = 0
	xx = 0
	y = 0
	for pos in range ( start_point, stop_point+1, 1):
		m = (Bar_list[pos].high + Bar_list[pos].low)/2
		x = x + pos
		xy = xy + (pos*m)
		xx = xx + (pos*pos)
		y = y + m
	n = stop_point - start_point + 1
	if n*xx - x*x == 0:
		m = 0
	else:
		m = (n * xy - x*y) / (n*xx - x*x)
	b = (y - m*x)/n
	x0 = start_point
	y0 = m*start_point + b
	x1 = stop_point
	y1 = m*stop_point + b
	next_point = get_entry_point(Element(y0, x0), Element(y1,x1), x1+3)
	regr_13 = get_profit(Element(y0,x0),next_point, timing)
	return regr_13, x0, y0, x1, y1


def get_profit ( Primer, Ultim, timing):

	diff_between_values = Decimal(Ultim.value - Primer.value)
	distance_between_points= Decimal(Ultim.position - Primer.position)
	if ( (Primer.value == 0 ) or (distance_between_points== 0 )):
		return 0, 0
	else:
		percen = diff_between_values / Primer.value
		rent = ((1+percen)**(1/distance_between_points))-1
		profit = (((1+rent)**(get_yearly_timing_unit(timing)))-1)*100
	return Decimal(profit)

def get_yearly_timing_unit ( timing ):

	if timing == 23:
		return int(12)
	elif timing == 5:
		return int(52)
	elif timing == 1:
		return int(365)

