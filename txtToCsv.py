import csv
def txtToCsv():
	list = []
	fr = open('test','r')
	writer = csv.writer(open('last5days.csv','wb'))
	for line in fr.readlines():
		currline = line.strip().split(',')
		list = [currline[0],currline[1],currline[2]]
		writer.writerow(list)


if __name__ == '__main__':
	txtToCsv()