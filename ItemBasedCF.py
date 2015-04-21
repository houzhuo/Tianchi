import math 
import random
class ItemBasedCF:
	def __init__(self, datafile= None):
		self.datafile = datafile
		self.readData()
		self.splitData(3,47)


	def readData(self,datafile=None):
		self.datafile = datafile or self.datafile
		self.data = []
		file = open(self.datafile,'r')
		for line in file.readlines():
			# usrid, itemid, record,_ = line.strip().split(',')
			lineArr = line.strip().split(',')
			usrid.append(lineArr[0])
			itemid.append(lineArr[1])
			record.append(lineArr[2])
			self.data.append((usrid,itemid,int(record)))
	def splitData(self,k,seed,data=None,M=8):
		self.testdata = {}
		self.traindata = {}
		data = data or self.data
		random.seed(seed)
		for user, item, record in self.data:
			if random.randint(0,7) == k:
				self.testdata.setdefault(item,{})
				self.testdata[user][item] = record
			else:
				self.traindata.setdefault(item,{})
				self.traindata[user][item] = record
				print traindata

def ItemSimilarity(self, train = None):
	train = train or self.traindata		
	self.itemSim = dict()
	item_user_count=dict()#item_user_count{item: likeCount} 
	count = dict() #count{i:{j:value}} the number of users who both like item i and j		
	for user, item in train.items(): #initialize the user_items{user: items}
		for i in item.keys():
			item_user_count.setdefault(i,0)
			item_user_count[i] += 1 #increase the value of i 
			for j in item.keys():
				if i ==j :
					continue
		count.setdefault(i,{})
		count[i].setdefault(j,0)
		count[i][j] += 1
	for i, related_item in count.items():
		self.itemSim.setdefault(i,dict())
		for j, cuv in related_item.items():
			self.itemSim[i].setdefault(j,0)
			self.itemSim[i][j] = cuv/math.sqrt(item_user_count[i]*item_user_count[j]*1.0)


def recommend(self,user,train = None,k=8, nitem=40):
	train = train or self.train
	rank = dict()
	ru = train.get(user,{})#return the value of key or return none{}
	for i, pi in ru.items():
		for j,wj in sorted(self.itemSim[i].items(),key = lambda x:x[1],reverse =True)[0:k]:
			if j in ru:
				continue
			rank,setdefault(j,0)
			rank[j] += wj
	return dict(sorted(rank.items(),key = lambda x:x[1],reverse=True)[0:nitem])
	
	def recallAndprecision(self,train = None, test = None, k = 8, nitem = 10):
		train = train or self.traindata
		test = test or self.testdata
		hit = 0
		recall = 0
		precision = 0
		for user in train.keys():
			tu = test.get(user, {})
		rank = self.recommend(user, train= train, k = k,nitem = nitem)
		for item,_ in rank.items():
			if item in tu:
				hit += 1
				recall += len(tu)
				precision += nitem
		return  (hit / (recall *1.0), hit / (precision * 1.0))
	def coverage(self,train = None,test = None, k =8, item = 10):
		train = train or self.traindata
		test = test or self.testdata
		recommend_items =set()
		all_items = set()
		for user in train.keys():
			for item in train[user].keys():
				all_items.add(item)
		rank = self.recommend(user, train, k = k, nitem = nitem)
		for item,_ in rank.items():
			recommend_items.add(item)
		return len(recommend_items) / (len(all_items) * 1.0)
	def popularity(self, train = None, test = None, k = 8, nitem = 10):
		train = train or self.traindata
		item = test or self.testdata
		item_popularity = dict()
		for user , items in train.items():
			for item in items.keys():
				item_popularity.setdefault(item, 0)
				item_popularity[item] += 1
		ret = 0
		n = 0
		for user in train.keys():
			rank = self.recommend(user, train, k = k, nitem = nitem)
		for item,_ in rank.items():
			ret += math.log(1 + item_popularity[item])
		n += 1
		return ret / (n * 1.0)
	def testRecommend():
		ubcf = ItemBasedCF("train.txt")
		ubcf.readData()
		ubcf.splitData(4,100)
		ubcf.ItemSimilarity()
		user = '345'
		rank = ubcf.recommend(user, k = 3)
		for i, rvi in rank.items():
			items = ubcf.testdata.get(user,{})
			record = items.get(i, 0)
			print "%5s: %.4f--%.4f" %(i.rvi.record)
	def testItemBasedCF():
		cf =ItemBasedCF('test.txt')
		print "%3s%20s%20s%20s%20s" %('k', 'recall', 'precision','coverage','popularity')
		for k in [5,10,20,40,80,160]:
			recall,precision = cf.recallAndprecision(k = k)
		coverage = cf.coverage(k = k)
		popularity = cf.popularity(k = k)
		print "%3d%19.3f%%%19.3f%%%19.3f%%%20.3f" % (k,recall * 100,precision * 100,coverage * 100,popularity)

if __name__ == "__main__":
	recommend.testItemBasedCF()
