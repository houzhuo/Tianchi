import csv
import string
import re
from numpy import *

def loadData():
	train_x= []
	train_y =[]
	# reader = csv.reader(file('BuyCount.csv','rb'))
	# for line in reader:
	fr = open('1125.txt')
	for line in fr.readlines():
		lineArr = line.strip().split(',')
		train_x.append([1.0, float(lineArr[1]),float(lineArr[3])])
		train_y.append(float(lineArr[4]))
	return mat(train_x), mat(train_y).transpose()

print 'stcgradDesvent'
for i in range(numSamples):





if __name__ == '__main__':
	print '====================================='
	loadData( )

