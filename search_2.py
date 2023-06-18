import csv
import re

file=open('4.csv')
read=csv.reader(file)
content=list(read)
print("Note: 退出输入'q';通配符是'.'   \r")
input1=input("请输入件号或关键字描述(退出输入'q'):")
a=str(input1).upper()

list_temp=[]

#print(content[0][0]+"       "+content[0][6]+"   "+content[0][1]+"     "+content[0][2]+"    "+content[0][3]+"   "+content[0][5]+"  "+content[0][4])
#print("TS           "+"合同    "+"描述                                    "+"尺寸                          "+"图纸")
count=0
count_temp=0

while input1!="q":
	for i in range(89304):
		if re.search(a,str(content[i][0]).upper()) or re.search(a,str(content[i][1]).upper()) or re.search(a,str(content[i][2]).upper()) or re.search(a,str(content[i][3]).upper())!=None:
			list_temp.append(content[i][0]+"   "+content[i][6]+"   "+content[i][1]+"   "+content[i][2]+"   "+content[i][5]+"   "+content[i][3])#+"   "+content[i][4])
			#print(content[i][0]+"   "+content[i][6]+"   "+content[i][1]+"   "+content[i][2]+"   "+content[i][5]+"   "+content[i][3])#+"   "+content[i][4])
			count=count+1
	#-----------print the item quantity:
	if(count==0):
		print("none has been found")
	else:	
		#for i in range(0,count):
		#	print(list_temp[i])
		print("共发现  "+str(count)+"  条信息")
		print("TS           "+"合同    "+"描述                                    "+"尺寸                          "+"图纸")
		if count>10:
			print("前10条信息如下：")
			for k in range(10):
				print(list_temp[k])
			YorN=input("是否全部显示？Y or N?")
			if YorN=="Y":
				print("TS           "+"合同    "+"描述                                    "+"尺寸                          "+"图纸")
				for j in range(count):
					print(list_temp[j])
			FurInfo=input("是否继续输入额外的关键字查询？若是输入Y:   ")
			if FurInfo=="Y":
				Fuript=input("请输入新的关键字： ")
				Fuript_final=str(Fuript).upper()
				for c in range(count):
					if re.search(Fuript_final,str(list_temp[c]).upper())!=None:
						count_temp=count_temp+1
						print(str(list_temp[c]))


				if count_temp==0:
					print("根据新条件未能查询到")
				else:
					print("根据新条件共查询到  "+str(count_temp)+"  条记录")
				count_temp=0

		else:
			for m in range(count):
				print(list_temp[m])

	
	#---------将检查结果清零：
	count=0
	list_temp=[]
	re.purge()
	#再次输入，重新循环：
	input1=input("请输入件号或关键字描述(退出输入'q'):")
	a=str(input1).upper()
	#print(content[0][0]+"       "+content[0][6]+"   "+content[0][1]+"     "+content[0][2]+"    "+content[0][3]+"   "+content[0][5]+"  "+content[0][4])
	print("TS           "+"合同    "+"描述                                    "+"尺寸                          "+"图纸")
	

	
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