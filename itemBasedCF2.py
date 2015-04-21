import math 
import random
import csv


def readData():
	
	data = []
	file = open("train",'r')
	for line in file.readlines():
		usrid, itemid, record,a,b,c = line.strip().split(',')
		# lineArr = line.strip().split(',')
		# usrid.append(lineArr[0])
		# itemid.append(lineArr[1])
		# record.append(lineArr[2])
		data.append((usrid,itemid,record))
	return data
def splitData():
	testdata = {}
	traindata = {}
	data = readData()
	random.seed(100)
	for user, item, record in data:
		if random.randint(0,10) == 3:
			testdata.setdefault(user,{})
			testdata[user][item] = record
			
		else:
			traindata.setdefault(user,{})
			traindata[user][item] = record
	return  testdata,traindata,testdata.keys(),testdata.keys()

def ItemSimilarity():
	test, train ,testKeys,trainKeys = splitData()	
	itemSim = dict()
	recommend ={}
	item_user_count=dict()#item_user_count{item: likeCount} 
	count = dict() #count{i:{j:value}} the number of users who both like item i and j		
	for user, item in train.items(): #initialize the user_items{user: items}
		for i in item.keys():
			item_user_count.setdefault(i,0)
			item_user_count[i] += 1 #increase the value of i 
			for j in item.keys():
				if i == j :
					continue
			count.setdefault(i,{})
			count[i].setdefault(j,0)
			count[i][j] += 1
	for i, related_item in count.items():
		itemSim.setdefault(i,dict())
		for j, cuv in related_item.items():
			itemSim[i].setdefault(j,0)
			itemSim[i][j] = cuv/math.sqrt(item_user_count[i]*item_user_count[j]*1.0)

 	rank = dict()
 	recommend = dict()
 	recommendList=[]
 	writer = csv.writer(open('tianchi_mobile_recommendation_predict.csv','wb'))
	writer.writerow(['user_id','item_id'])
 	for user_id in trainKeys:
	 	ru = train.get(user_id,{})#return the value of key or return none{}
	 	for i, pi in ru.items():
			for j,wj in sorted(itemSim[i].items(),key = lambda x:x[1],reverse =True)[0:10]:
				if j in ru:
					continue
				rank.setdefault(j,0)
				rank[j] = wj*float(pi)
		
		
		recommend =  sorted(rank.items(),key = lambda x:x[1],reverse=True)

		recommendList= [user_id, recommend[0][0]]
		#print recommendList
	
		writer.writerow(recommendList)






# def recallAndprecision():
# 	test, train =splitData()
# 	hit = 0
# 	recall = 0
# 	precision = 0
# 	for user in train.keys():
# 		tu = test.get(user, {}).keys()
# 		rank = ItemSimilarity(user)
# 		for item in rank.keys():
# 			# print item
# 			if item in tu:
# 				hit += 1
# 				recall += len(tu)
# 				precision += 10
# 				print hit,recall,precision
# 		print  hit / (recall *1.0), hit / (precision * 1.0)

	
if __name__ == "__main__":
	#recommend('111935471')
	ItemSimilarity()
	#recallAndprecision()
	#splitData()
	# readData()

