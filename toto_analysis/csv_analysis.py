#! /usr/bin/python
# -*- coding: utf-8 -*-
# author : lyushuen@gmail.com

import csv


class Csv(object):

	""" 用来处理csv 文件，三个函数的作用：
		rowdicts： csv文件的第一行中的每一个单元格作为key，对每一行都会产生多个 key: value对的
					dictionary
		columdicts：以csv文件的第一行中的每一个单元格作为key， 每一列会产生一个字典
		keydicts： 根据用户输入的key的关键字， 此函数会产生基于此关键字的针对每一行的字典
	"""

	def __init__(self, csvfile=None):
		self.dicts = {}
		self.csvfile = csvfile


	def rowdicts(self):
		"""read csv file and output in the format of dictionary, each row is a dictionary
			with the first row as keys"""
		d_ = []
		with open(self.csvfile, 'rt') as f:
			reader = csv.DictReader(f)
			for row in reader:
				d_.append(row)

		return d_

	def columndicts(self):
		"""column based dictionary genaration"""

		columnD_ = self.dicts
		with open(self.csvfile) as csvf:
			reader = csv.DictReader(csvf)
			for row in reader:
				for column, value in row.iteritems():
					columnD_.setdefault(column, []).append(value)

		return columnD_

	def keydicts(self, key="Draw"):

		"""this function is key based, which can be used for generating the dictionary 
			with key defined, for example if key="Draw", the "Draw" key based dict will 
			be generated.However, the key here should be Unique, such as "Draw"(which is 
			the index of each draw) and data, but cannot be "win1" or other keys because 
			it will fresh the dict with the same key
		"""
		self.key = key
		keyD_ = self.dicts
		with open(self.csvfile) as csvf:
			reader = csv.DictReader(csvf)
			for row in reader:
				key = row.pop(self.key)
				if key in drawD_:
					pass
				keyD_[key]= row
		return keyD_
