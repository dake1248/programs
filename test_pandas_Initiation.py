import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#传递一个list对象创建Series
s=pd.Series([1,2,3,4,np.nan,5,6])
s
print(s)


#传递一个numpy array创建一个DataFrame:

dates=pd.date_range('20110101',periods=6)

dates
print(dates)

#DatetimeIndes(['2013-01-01','2013-01-02','2013-03-03','2013-01-04','2013-01-05','2013-01-06'],dtype='datetime64[ns]',freq='D')

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
df


#传递一个能被转换为类似序列结构的字典对象来创建一个DataFrame:

#df2=pd.DataFrame({'A':1.,'B':pd.Timestamp('20130102'),'C':pd.Series(,indes=list(range(4)),dtype='float32'),'D':np.array([3]*4,dtype=]int32'),'E':pd.Categorical(["test","train","test","train"]),'F':'foo'})

#df2

#查看不同列的数据类型：
#df2.dtypes

#查看DataFrame中头部和尾部的行： 
df.head()
df.tail(3)

#显示索引、列和底层的numpy数据:
df.index
df.columns
df.values

#对数据的快速汇总统计：
df.describe()

#对数据的转置
df.T

#按轴进行排序
df.sort_index(axis=1,ascending=False)



#按值进行排序
df.sort_values(by='B')

#----------------------选择-------------------

#选择一个单独的列
df['A']

#行选择
df[0:3]

df['20130102':'20130104']

#使用标签获取交叉区域

df.loc[dates[0]]

#使用标签在多个轴上选择

df.loc[:,['A','B']]

#标签切片

df.loc['20130102':'20130104',['A','B']]

#对返回的对象进行维度缩减

df.loc['20130102',['A','B']]

#获取一个标量

df.loc[dates[0],'A']

快速访问一个标量

df.at[dates[0],'A']

#-----------------通过位置选择

#通过传递数值进行位置选择
df.iloc[3]	#选择第3行

#通过数值进行切片

df.iloc[3:5,0:2]

#通过制定一个位置的列表

df.iloc[[1,2,4],[0,2]]#选择1/2/4行的0/2列

#对行进行切片

df.iloc[1:3,:]#选择2/2行

#对列进行切片
df.iloc[:,1:3]

#获取特定的值
df.iloc[1,1]

#款苏访问标量
df.iat[1,1]


#------------------布尔索引

#使用一个单独列的数值选择数据
df[df.A>0]

#使用where操作选择数据
df[df>0]

#使用isin()方法过滤：
df2=df.copy()
df2['E']=['one','one','two','three','four','three']
df2
df2[df2['E'].isin(['two','four'])]


#--------设置

#设置一个新的列
s1=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130102',periods=6))
s1
df['F']=s1

#通过标签设置新的值
df.at[dates[0],'A']=0

#通过位置设置新的值
df.iat[0,1]=0
#通过一个numpy数组设置一组新值
df.loc[:,'D']=np.array([5]*len(df))

#通过where

df2=df.copy()
df2[df2>0]=-df2
df2

#--------------缺失值处理

#pandas中使用np.nan代替缺失值

#使用reindex()方法对指定轴上的索引进行改变/增加/删除

df1=df.reindex(index=dates[0:4],columns=list(df.columns)+['E'])
df2.loc[dates[0]:dates[1],'E']=1
df1

#去掉包含缺失值的行
df1.dropna(how='any')

#对缺失值进行填充
df1.fillna(value=5)

#对数据进行布尔填充

pd.isnull(df1)

#--------------------相关操作：统计

#描述性统计
df.mean()

#在其他轴上操作
df.mean(1)

#对有不同维度，需对其的对象进行操作

s=pd.Series([1,3,5,np.nan,6,8],index=dates).shift(2)
s

df.sub(s,axis='index')

#---------------APPLY

#对数据应用函数

df.apply(np.cumsum)

df.apply(lambda x:x.max()-x.min())
