import os
import sys
import os.path
def split(files):
	if not os.path.isfile(files):
		print file,"is not a file"
		exit(1)
	txtfile = open(files,"r")

	file_index = 0
	line_cnt = 0

	outfile = open("output_%d" %file_index+'.txt','w')
	for line in txtfile:
		if line_cnt<1000000:
			outfile.write(line)
			line_cnt += 1
		else:
			outfile.close()
			file_index +=1
			outfile=open("output_%d" %file_index+'.txt','w+')		
			line_cnt = 0

			outfile.close()
			txtfile.close()

	if __name__ == "__main__":
		split('tianchi_mobile_recommend_train_user.txt')#.txt