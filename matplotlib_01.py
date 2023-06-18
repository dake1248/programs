import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


squares=[1,4,9,16,25,36]
x=[1,2,3,4,5,6]

plt.title("Square Numbers")
plt.xlabel("Value")
plt.ylabel("Square of value")
plt.tick_params(axis='both')
#plt.figure(figsize=(10,6))#指定图表的宽度、高度、分辨率和背景色
#plt.axes().get_xaxis().set_visible(False)#隐藏x轴
#plt.axes().get_yaxis().set_visible(False)#隐藏y轴

#---------使用plot()绘制折线图
#plt.plot(squares)
#plt.plot(squares,linewidth=5)
#plt.plot(x,squares,linewidth=1)

#----使用scatter() 绘制散点图并设置其样式

#plt.scatter(2,4)#传递一对 x 和 y 坐标，它将在指定位置绘制一个点：
#plt.scatter(x,squares,s=10)#设定x/y座标位置，参数s设定显示点的大小

x=list(range(1,101))
y=[x**2 for x in x]#遍历 x 值（for x in x_values ），计算其平方值（x**2 ）
#plt.scatter(x,y,s=10,edgecolor='green')
#plt.scatter(x,y,s=10,c='red',edgecolor='green')

#plt.scatter(x,y,s=10,c=(0.5,0.5,0.8),edgecolor='None')
plt.scatter(x,y,c=y,cmap=plt.cm.Blues,edgecolor='None',s=20)#根据每个点的 y 值来设置其颜色

plt.axis([0, 110, 0, 11000])#axis() 要求提供四个值：x 和 y 坐标轴的最小值和最大值
'''
颜色：
1.使用颜色参数c:
	并将其设置为一个元组，其中包含三个0~1之间的小数值，它们分别表示红色、绿色和蓝色分量
2.使用颜色映射:
plt.scatter(x,y,c=y,cmap=plt.cm.Blues,edgecolor='None',s=40)#根据每个点的 y 值来设置其颜色

#--snip--# 设置图表标题并给坐标轴加上标签

'''
plt.show()

plt.savefig('squares_plot.png')#剪掉空白区域后保存为.png

