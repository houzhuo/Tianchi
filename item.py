def loadCsvData():
	import csv
	text ={}
	list =[]
	reader= csv.reader(file('tianchi_mobile_recommend_train_user.csv','rb'))
	for line in reader:
		if  line[2]>'1':
		#lineArr = line.split(",")
			text.setdefault(line[0],[])
			text[line[0]].append(line[1])
		
	writer = csv.writer(file('datafile.csv','wb'))
	writer.writerow(['user_id', 'item_id'])	
	for i in text:
		print i," ",text[i],'\n'

		list=[i,text[i]]
		writer.writerow(list)	

	return text,text[i]
def splitData(data,M,K,seed):
	test = []
	train = []
	random.seed(seed)
	for user, item in data:
		if random.randint(0,M) == k:
			test.append([user,item])
		else:
			train.append([user,item])
	return train, test

def loadTxtData():
	import csv
	
	data={}
	
	list=[]

	fr=open('ceshiji','r')
	
	for line in fr.readerdlines():
		currLine = line.strip().split(",")
		if currLine[1]>'2':
		
			data.setdefault(currLine[0],[])
			data[currLine[0]].append(currLine[1])

	writer  = csv.writer(file('useritem.csv','w+'))
	writer.writerow(['user_id','item_id'])
	for i in data:
		list=[i,data[i]]
		writer.writerow(list)
	return data,data[i]



