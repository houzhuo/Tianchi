import csv
import string
import re

def NumberCount():
	list = []
	count = {}

	reader = csv.reader(file('tianchi_mobile_recommend_train_user.csv','rb'))
	writer = csv.writer(open('BuyCount.csv','wb'))
	writer.writerow(['userItem','click','col','cart','buy'])
	print 'first iterator...'
	for line in reader:
		userItem = '_'.join([line[0],line[1]])
		
		count.setdefault(userItem,[0,0,0,0])		
		if line[2] == '1':
			count[userItem][0] += 1
		elif line[2] == '2':
			count[userItem][1] = 1
		elif line[2] == '3':
			count[userItem][2] = 1
		elif line[2] == '4':
			count[userItem][3] = 1
		else:
			print 'false'
	print 'iterator over'
	print 'change click number...'
	for i in count:
		if count[i][0] > 0 and count[i][0] < 4:
			count[i][0] = 1.83845
		elif count[i][0] > 3 and count[i][0] < 7:
			count[i][0] = 4.53351
		elif count[i][0] > 6 and count[i][0] < 10:
			count[i][0] = 7.77549
		elif count[i][0] > 9 and count[i][0] < 13:
			count[i][0] = 10.82740
		elif count[i][0] > 12 and count[i][0] < 16:
			count[i][0] = 13.85166
		elif count[i][0] > 12:
			count[i][0] = 22.51637
		else:
			print count[i][0]
		list = [i,count[i][0],count[i][1],count[i][2],count[i][3]]
		writer.writerow(list)
	# click1 = 0
	# click2 = 0
	# click3 = 0
	# click4 = 0
	# click5 = 0
	# click6 = 0
	# k1 = 0
	# k2 = 0
	# k3 = 0
	# k4 = 0
	# k5 = 0
	# k6 = 0
	
	# for i in count:
	# 	if count[i][0] > 0 and count[i][0] < 4:
	# 		click1 += count[i][0]
	# 		k1 += 1
	# print float(click1) / float(k1)
	# for i in count:
	# 	if count[i][0] > 3 and count[i][0] < 7:
	# 		click2 += count[i][0]
	# 		k2 += 1
	# print float(click2) / float(k2)
	# for i in count:
	# 	if count[i][0] > 6 and count[i][0] < 10:
	# 		click3 += count[i][0]
	# 		k3 += 1
	# print float(click3) / float(k3)
	# for i in count:
	# 	if count[i][0] > 9 and count[i][0] < 13:
	# 		click4 += count[i][0]
	# 		k4 += 1
	# print float(click4) / float(k4)
	# for i in count:
	# 	if count[i][0] > 12 and count[i][0] < 16:
	# 		click5 += count[i][0]
	# 		k5 += 1
	# print float(click5) / float(k5)
	# for i in count:
	# 	if count[i][0] > 15:
	# 		click6 += count[i][0]
	# 		k6 += 1
	# print float(click6) / float(k6)

		# list = [i,count[i][0],count[i][1],count[i][2],count[i][3]]
		# writer.writerow(list)


if __name__ ==  '__main__':
	NumberCount()





