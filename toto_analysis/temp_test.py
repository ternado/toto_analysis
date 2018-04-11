#! /usr/bin/python
#--*-- code: utf-8 --*--
# author: lyushuen@gmail.com

from csv_analysis import Csv 




if __name__ == '__main__':

	WIN1 = []
	WIN2 = []
	WIN3 = []
	WIN4 = []
	WIN5 = []
	WIN6 = []
	ADDNO = []
	DRAW = []

	csvfile = 'data/toto.csv'
	csv_analysis = Csv(csvfile=csvfile)
	dicts = csv_analysis.keydicts()
	for draw_id in dicts:
		print(":{}, length:{}".format(draw_id,len(dicts)))
		print("dictionary:{} for draw:{}".format(dicts[draw_id], draw_id))
		
		WIN1.append(dicts[draw_id]['win1'])
		WIN2.append(dicts[draw_id]['win2'])
		WIN3.append(dicts[draw_id]['win3'])
		WIN4.append(dicts[draw_id]['win4'])
		WIN5.append(dicts[draw_id]['win5'])
		WIN6.append(dicts[draw_id]['win6'])
		ADDNO.append(dicts[draw_id]['addno'])
		print("win1 :{}".format(WIN1))
		print("win2 :{}".format(WIN2))
		print("win3 :{}".format(WIN3))
		print("win4 :{}".format(WIN4))
		print("win5 :{}".format(WIN5))
		print("win6 :{}".format(WIN6))
		print("addno :{}".format(ADDNO))
		print("\n\n")
		#for item in dicts[draw_id]:
		#	print("key of item :{} and value of item:{} in draw:{}".format(item, \
		#		dicts[draw_id][item],draw_id))

			
		#break
