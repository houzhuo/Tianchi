import csv
import string
import re

def NumberCount():
	list = []
	count = {}
	i = 0

	reader = csv.reader(file('tianchi_mobile_recommend_train_user.csv','rb'))
	writer = csv.writer(open('1125.csv','wb'))
	writer.writerow(['userItem','click','col','cart','buy'])
	print 'first iterator...'
	for line in reader:
		date = re.sub(r'\D','',line[5]) 
		userItem = '_'.join([line[0],line[1]])
		if line[2] == '1' and string.atoi(date[:8]) == 20141217:
			count.setdefault(userItem,[0,0,0,0])
			count[userItem][0] += 1
		elif line[2] == '2'and string.atoi(date[:8]) == 20141217:
			count.setdefault(userItem,[0,1,0,0])
			count[userItem][1] = 1
		elif line[2] == '3'and string.atoi(date[:8]) == 20141217:
			count.setdefault(userItem,[0,0,1,0])
			count[userItem][2] = 1
		elif line[2] == '4' and string.atoi(date[:8]) == 20141218:
			count.setdefault(userItem,[0,0,0,1])
			count[userItem][3] = 1
			
	print '>>>>>>>>>>>>>>>>>>>>>.writing...'
	for i in count:
		list = [i,count[i][0],count[i][1],count[i][2],count[i][3]] 
		writer.writerow(list)
if __name__ == '__main__':
	NumberCount()