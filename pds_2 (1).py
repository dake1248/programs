import pandas as pd
import numpy as np
import matplotlib
import random

import plotly.express as px
import plotly.io as pio

#读入CSV文件"1.csv"
#a=pd.read_csv("1.csv")
#print(a)
#b=pd.read_csv("filename.csv")
#b=pd.read_excel("filename.xls")
#-----写入文件
#pd.to_csv("filename.csv",sep=',',index=False)#写入csv：逗号分隔，不带索引
#pd.to_excel("filename.xls",sheet_name="sheet1",index=False)#写入excel：指定Sheet名，不带索引

#b=pd.read_csv("Metro_Interstate_Traffic_Volume.csv")#直接读取，index默认
b=pd.read_csv("Metro_Interstate_Traffic_Volume.csv",index_col="date_time")#index默认为date_time
b.values#返回除index之外的所有行（每行是一个list)
b.head(10)
b.describe()#统计所有是数字的列（不统计文本的列）
b['holiday']
b['temp'].describe()
b.index
b.set_index('temp')#设置temp列为index
b.reset_index(drop=True)## 不保留原索引到DataFrame中
b.columns
b.dtypes#获取列的数据类型

#-----------逐列打印df内容
for row in df:
	df[row]

#-----读取dataframe的若干行并将其转化为一个列表list
df1=df[1:10]
df_2_list=list(df1)#仅转化第一行

#。。。？？？？？？？如何操作？

df[df.holiday!='None']
df[(df.holiday=='None')&(df.weather_main!='Thunderstorm')]#--------与-------------
df[(df.holiday=='None')|(df.weather_main=='Thunderstorm')]#---------或-------------
df[-(df.holiday=='None')&(df.weather_main!='Thunderstorm')]#---------非-------------

df[df.holiday.isin(['Labor Day','State Fair'])]#-----验证在某个列表范围内
df[-df.holiday.isin(['Labor Day','State Fair'])]#-----验证不在某个列表范围内
df[df.holiday.str.contains('Fair')]#-----包含某个字符（区分大小写）
df[df.holiday.str.contains('Wash')]



b.rename(columns={'temp':'TEMP'})#更改列名
#b['col_name'].astype(np.float32)#修改列的数据类型
k=['holiday', 'temp', 'snow_1h', 'rain_1h', 'clouds_all', 'weather_main','weather_description','traffic_volume']
b[k]#更改列的顺序

b[b.weather_main=='Clouds']#筛选某列的单一数值

df[df.rain_1h!=0][['temp','holiday','traffic_volume']]#某选择条件下，选择某几列内容
df[(df.rain_1h!=0)&(df.holiday!='None')]

df[(df.holiday!='None')]


#------------pandas /sqlite3结合
import slqlite3
import pandas

#从CSV文件读取并写入sqlite3
b=pd.read_csv("Metro_Interstate_Traffic_Volume.csv",index_col="date_time")#index默认为date_time
con=sqlite3.connect("metro.db")#链接数据库metro.db
cur=con.cursor()
cur.execute("drop table if exists Metro")#检查表确保没有存在的表"Metro"
b.to_sql("Metro",con)#写入数据库
re=cur.execute("select * from Metro")

#-------------打印全部数据库内容（分别打印每行的列表）
for row in re:
	print(row[0]+"   "+row[1]+"   "+str(row[2])+"   "+str(row[3])+"   "+str(row[4])+"   "+str(row[5]))
for i in range(10):
	re.fetchone()#检查读入的前10条记录

#从sqlite3数据库读入pandas
df=pandas.read_sql("select * from Metro",con,index_col='date_time')#将date_time作为index读入
df
for i in range(20):
	df[i:i+1]#逐行打印df内的内容


df.to_excel("metro.xls",sheet_name="metro",index=True)
cur.close()
con.close()






#-----------------------ORDER BY — 排序------------------------------#
#默认情况下，Pandas 会使用升序排序。如果要使用降序，请设置 asending=False。

b.sort_index(axis=1,ascending=False)
b.sort_index()
b.sort_values(by='temp')
b.sort_values(by='date_time')
b['weather_description'].describe()
b['weather_main'].value_counts()
b['weather_main'].unique()#检查某一列的唯一值
b['weather_main'].nunique()#查看某一列唯一值数量
b['col_name'].idxmax()#求某一列最大值所在的位置;以修改axis参数，当axis=0时表示对行进行操作，当axis=1时表示对列进行操作。
df.corr()#求各列之间的相关性

df[df.holiday!='None'].sort_values('traffic_volume')
df[df.holiday!='None'].sort_values('traffic_volume',ascending=False)

df.groupby(['holiday','temp']).size()#将holiday和temp分组排列：相同holiday的列出temp
df.groupby(['holiday','temp','traffic_volume']).size()#相同holiday的列出temp和traffic_volume

#----------------删除-------------------
a=df.drop(df[df.holiday=='Christmas Day'].index)#删除df.holiday中是"Christmas Day"的行
a['holiday'].value_counts()#检查确认已删除Christmas Day


#---------------替换-------------------
#指定条件替换
df.loc[df.holiday=='Christmas Day','holiday']='CHRISTMAS DAY'
#全局替换
df.replace(to_replace='CHRISTMAS DAY',value='CHS DAY',inplace=True)
#局部替换
df.replace({'holiday':{'CHS DAY':'Christmas Day','Veterans Day':'Vet Day'}},inplace=True)
'''
#数据处理方式操作函数：

1 df.columns = ['a','b','c'] # 重命名列名
2 pd.isnull() # 检查DataFrame对象中的空值，并返回一个Boolean数组
3 pd.notnull() # 检查DataFrame对象中的非空值，并返回一个Boolean数组
4 df.dropna() # 删除所有包含空值的行
5 df.dropna(axis=1) # 删除所有包含空值的列
6 df.dropna(axis=1,thresh=n) # 删除所有小于n个非空值的行
7 df.fillna(x) # 用x替换DataFrame对象中所有的空值
8 s.astype(float) # 将Series中的数据类型更改为float类型
9 s.replace(1,'one') # 用‘one’代替所有等于1的值
10 s.replace([1,3],['one','three']) # 用'one'代替1，用'three'代替3
11 df.rename(columns=lambda x: x + 1) # 批量更改列名
12 df.rename(columns={'old_name': 'new_ name'}) # 选择性更改列名
13 df.set_index('column_one') # 更改索引列
14 df.rename(index=lambda x: x + 1) # 批量重命名索引
'''
#判断是否是空值
for row in df:
	df[row].isnull()#逐列判断是否是空值


c=b['weather_main'].value_counts()#返回统计后的一个字典
c['Clouds']
c['Smoke']
c[0]
c[:5]#前5个统计

#df[df.
#c.plot(kind='bar')#绘制条形图


import numpy as np
pd.Series([1,2,3])
pd.Series([1,2,3]).values
np.array([1,2,3])

k=np.array([1,2,3])
k!=2
k1=k[k!=2]#传递不等于2的列表k的剩余元素

#--------pandas处理字符串
clouds=b['weather_main'].str.contains('Clouds')#查询weather_main列中包含"Clouds"的列
clouds
#clouds.plot()#绘制图表
