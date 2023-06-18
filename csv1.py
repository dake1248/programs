import csv

file=open('3.csv')
content=list(csv.reader(file))

#使用for循环获取单行内容，避免一次性读取大容量内容占用内存
import csv
file=open('3.csv')
read=csv.reader(file)
for row in read:
	print(str(row))
	print("line"+str(read.line_num)+":"+str(row))#read.line_num表示当前读取的行数


csv_w=open("3.csv",'w',newline='')
wc=csv.writer(csv_w)

wc.writerow(['date','follow','unfollow'])
list1=[content[0][0],content[0][1],content[0][2]]
for i in range(20):
	list=[content[i][0],content[i][1],content[i][2]]
	print(list)
	wc.writerow(list)


csv_w.close()