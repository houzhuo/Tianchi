from numpy import *
import matplotlib.pyplot as plt
import time
from logRegression import *
import csv
import string

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

## step 1: load data  
print "step 1: load data..."
train_x, train_y = loadData()
test_x = train_x; test_y = train_y
  
## step 2: training...  
print "step 2: training..."
opts = {'alpha': 0.01, 'maxIter': 20, 'optimizeType': 'smoothStocGradDescent'}
optimalWeights = trainLogRegres(train_x, train_y, opts)
print optimalWeights
  
## step 3: testing  
print "step 3: testing..."  
accuracy = testLogRegres(optimalWeights, test_x, test_y)
  
## step 4: show the result  
print "step 4: show the result..."  
print 'The classify accuracy is: %.3f%%' % (accuracy * 100)
showLogRegres(optimalWeights, train_x, train_y)
