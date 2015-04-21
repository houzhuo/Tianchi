import csv
import string
import re

def cart():
	text =dict()
	list = []
	reader = csv.reader(file('tianchi_mobile_recommend_train_user.csv','rb'))
	writer = csv.writer(open('18cart.csv','wb'))
	writer.writerow(['user','item'])
	for line in reader:
		date  = re.sub(r'\D','',line[5])
		if line[2] == '3' and string.atoi(date) - 2014121800 > 0:
			text.setdefault(line[0],0)
			text[line[0]] = line[1]
			print line[5] 
	print 'start to write...'
	for i in text:
		list = [i,text[i]]
		writer.writerow(list)

if __name__ == '__main__':
	print '====================================='
	cart()

