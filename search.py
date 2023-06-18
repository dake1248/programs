import csv
import re

file=open("4.csv")
read=csv.reader(file)
content=list(read)
#print("	提示：(1)退出输入'q'    (2)通配符是'.'	“）
input1=input("请输入件号或关键字描述(退出输入'q'):")
a=str(input1).upper()

print("\r")
print(content[0][0]+"       "+content[0][6]+"   "+content[0][1]+"     "+content[0][2]+"    "+content[0][3]+"   "+content[0][5]+"  "+content[0][4])
count=0

while input1!="q":
	for i in range(89304):
		if re.search(a,str(content[i][0]).upper()) or re.search(a,str(content[i][1]).upper()) or re.search(a,str(content[i][2]).upper()) or re.search(a,str(content[i][3]).upper())!=None:
			print(content[i][0]+"   "+content[i][6]+"   "+content[i][1]+"   "+content[i][2]+"   "+content[i][3]+"   "+content[i][5]+"   "+content[i][4])
			count=count+1
	#-----------print the item quantity:
	if(count==0):
		print("none has been searched")
	else:
		print(str(count)+"   items  searched")
	
	#---------repeat the loop:
	count=0
	input1=input("请输入件号或关键字描述(退出输入'q'):")
	a=str(input1).upper()
	print(content[0][0]+"       "+content[0][6]+"   "+content[0][1]+"     "+content[0][2]+"    "+content[0][3]+"   "+content[0][5]+"  "+content[0][4])
	re.purge()
print("thanks,88")

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