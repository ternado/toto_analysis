#! /usr/bin/python
# -*- coding: utf-8 -*-
# author: lyushuen@gmail.com

from csv_analysis import Csv

csvfile = 'data/toto.csv'
csvClass = Csv(csvfile=csvfile)

coldicts = csvClass.columndicts()
print coldicts