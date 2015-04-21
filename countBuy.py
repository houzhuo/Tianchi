import csv

def NumberCount():
	click=[]
	collection = []
	buy = []
	clickCount = {}
	collectionCount = {}
	count ={}
	list = []
	a=[[]]
	reader = csv.reader(file('last5days.csv','rb'))
	writer = csv.writer(open('clickCount.csv','wb'))
	writer.writerow(['userItem','Number','whether'])
	for line in reader:
		if line[2] == '1':
			clickUserItem = '_'.join([line[0],line[1]])
			click.append(clickUserItem)
		# if line[2] == '2':
		# 	colUserItem = '_'.join([line[0],line[1]])
		# 	collection.append(colUserItem)
		if line[2] == '4':
			UserItem = '_'.join([line[0],line[1]])
			buy.append(UserItem
	

	for i in click:
		clickCount.setdefault(i,0)
		clickCount[i] += 1

	for i in clickCount.keys():
		count.setdefault(i,{})
		count[i].setdefault(clickCount[i],0)
		for j in buy:
			if j == i:
				count[i][clickCount[i]] = 1
			# else:
			# 	count[i][clickCount[i]] = 0


		clickList = [i,clickCount[i],count[i][clickCount[i]]] 
		writer.writerow(clickList)


		


if __name__ ==  '__main__':
	NumberCount()






