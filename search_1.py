import csv
import re

file=open('4.csv')
read=csv.reader(file)
content=list(read)
a=input("input the partical number('q' to quit)：   ")
print("\r")
print(content[0][0]+"       "+content[0][1]+"           "+content[0][2]+"          "+content[0][3]+"        "+content[0][4])
count=0

while a!="q":
	for i in range(89304):
		if re.search(a,str(content[i][0])) or re.search(a,str(content[i][1])) or re.search(a,str(content[i][2])) or re.search(a,str(content[i][3]))!=None:
			print(content[i][0]+"   "+content[i][1]+"   "+content[i][2]+"   "+content[i][3]+"   "+content[i][4])
			count=count+1
	if(count==0):
		print("none has been searched")
	else:
		print(str(count)+"   items  searched")
	count=0
	a=input("input the partical number('q' to quit)：  ")
	print(content[0][0]+"       "+content[0][1]+"           "+content[0][2]+"          "+content[0][3]+"        "+content[0][4])
	re.purge()

'''
#-----------------根据件号搜索信息-----------------
	for i in range(89304):
		if re.search(a,str(content[i][0]))!=None:
			print(content[i][0]+"                "+content[i][1]+"           "+content[i][2]+"          "+content[i][3]+"        "+content[i][4])
			count=count+1

	if(count==0):
		print("none has been searched")
	else:
		print(str(count)+"   items totally has been searched")
	count=0
	a=input("input the partical number:")
#-----------------根据件号搜索信息-----------------
'''	

'''
csv_w=open("3.csv",'w',newline='')
wc=csv.writer(csv_w)

wc.writerow(['date','follow','unfollow'])
list1=[content[0][0],content[0][1],content[0][2]]
for i in range(20):
	list=[content[i][0],content[i][1],content[i][2]]
	print(list)
	wc.writerow(list)
'''