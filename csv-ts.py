import csv

file=open("ts.csv")
content=list(csv.reader(file))

csv_w=open("3.csv",'w',newline='')
wc=csv.writer(csv_w)

#wc.writerow(['date','follow','unfollow'])
list1=[content[0][0],content[0][1],content[0][2]]
for i in range(89304):
	list=[content[i][1],content[i][2],content[i][3],content[i][5],content[i][7],content[i][4],content[i][0],content[i][33],content[i][39]]
	print(list)
	wc.writerow(list)


csv_w.close()