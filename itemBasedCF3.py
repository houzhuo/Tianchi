import csv	
import re
import string
def loadData():
	text=dict()
	reader = csv.reader(file('tianchi_mobile_recommend_train_user.csv','rb'))
	writer= csv.writer(open('tianchi_mobile_recommendation_predict.csv','wb'))
	writer.writerow(['user_id','item_id'])
	for line in reader: 
		if line[2]=='3':
			date  = re.sub(r'\D','',line[5])
			if string.atoi(date)-2014121800 > 0:
				writer.writerow([line[0],line[1]])
			 	



if __name__ == '__main__':
	loadData()



