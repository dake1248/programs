import pandas
import numpy as np
import matplotlib.pyplot as plt

n=np.array(range(0,401))
fx=n**3
x=np.sin(np.pi/17*n)


list_value=list(x)

#判断是否可被3整除,若不能被3整除，使用最近的平均值完成插值
if len(list_value)%3==1:
	t0=(list[len(list_value)-2]+list[len(list_value)-3])/2
	t1=(list[len(list_value)-1]+list[len(list_value)-2])/2
	list_value.append(t0)
	list_value.append(t1)
if len(list_value)%3==2:
	t1=(list_value[len(list_value)-1]+list_value[len(list_value)-2])/2
	list_value.append(t1)

SUM=0

for i in range(1,int(len(list_value)/3)+1):
	SUM=SUM+(list_value[i*3-3]+4*list_value[i*3-2]+list_value[i*3-1])/6


df=pandas.DataFrame(x)
#df.to_csv("numpy_signal_02.csv")

print(SUM)
#plt.scatter(n,x)
#plt.bar(n,x)
plt.plot(n,x)




plt.show()