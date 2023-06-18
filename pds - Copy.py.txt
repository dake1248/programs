import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arr0=pd.Series([1,2,3,4,5,6])
#print(arr0)

#传递一个list对象创建Series
s=pd.Series([1,2,3,4,np.nan,5,6])
print(s)

#传递一个numpy array创建一个DataFrame:

dates=pd.date_range('20110101',periods=10)
print("dates; ")
print(dates)


#DatetimeIndex(['2013-01-01','2013-01-02','2013-03-03','2013-01-04','2013-01-05','2013-01-06'],dtype='datetime64[ns]',freq='D')

df=pd.DataFrame(np.random.randn(10,6),index=dates,columns=list('ABCDEF'))
print(df)

#传递一个能被转换为类似序列结构的字典对象来创建一个DataFrame:

df2=pd.DataFrame({'A':1.1,
                  'B':pd.Timestamp('20130102'),
                  'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                  'D':np.array([3]*4,dtype='int32'),
                  'E':pd.Categorical(['test','train','test','train']),
                  'F':'foo'})

print(df2)

#------------------------------察看数据------------------

#查看不同列的数据类型：
print("df2 dtypes:  ")
print(df2.dtypes)
#查看DataFrame中头部和尾部的行： 
print("df.head():")
print(df.head(3))
print("df2.tail(3):")
print(df2.tail(3))

#显示索引、列和底层的numpy数据:
print("df.index:")
print(df.index)
print(df.columns)
print(df.values)

#对数据的快速汇总统计：
print(df.describe())

#对数据的转置
print(df)
print(df.T)

#按轴进行排序
print(df.sort_index(axis=1,ascending=False))

#按值进行排序
print(df)
print(df.sort_values(by='B'))



#------------------------------选择-------------------------

#选择一个单独的列
print("df[A]: ")
print(df['A'])
#行选择
print("df[0:3]:")
print(df[0:3])
print("df['20110102':'20110104']:")
print(df['20110102':'20110104'])

#使用标签获取交叉区域
print("df.loc[dates[0]]:显示索引dates的第0行数据 ")
print(df.loc[dates[0]])

#使用标签在多个轴上选择

print("df.loc[:,['A','B']]:")
print(df.loc[:,['A','B']])

#标签切片
print("df.loc[20110101':'20110104',['A','B','F']:  ")
print(df.loc['20110102':'20110104',['A','B','F']])


#对返回的对象进行维度缩减
print("df.loc['20130102',['A','B']:")
print(df.loc['20110102',['A','B']])

#获取一个标量
print("获取一个标量：索引dates的第0行和“A”列：")
print(df.loc[dates[0],'A'])

#快速访问一个标量
print("快速访问标量：索引dates的第0行和“A”列： df.at[dates[0],'A':")
print(df.at[dates[0],'A'])

#-----------------通过位置选择

#通过传递数值进行位置选择
print("#选择第3行:")
print(df.iloc[3])	#选择第3行

#通过数值进行切片
print("#通过数值进行切片:第2/3/4行，第1/2/3列")
print(df)
print(df.iloc[2:5,1:3])
#对行进行切片
print("#对行进行切片")
print(df.iloc[1:3,:])#选择1/2行
#对列进行切片
print("#对列进行切片")
#print(df.iloc[:,1:3])#choose column 1/2
#获取特定的值
print(df.iloc[1,1])

#访问标量
print(df.iat[1,1])


print("#对每一列的平均值")
#对每一列的平均值
print(df.mean())
#对每一行的平均值
print(df.mean(1))

