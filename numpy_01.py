import numpy as np

a=np.array([1,2,3,4])

b=np.array([5,6,7,8])

c=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

a.shape#数组的形状:描述数组各个轴长度的元组(tuple):(4,)
tuple_a=a.shape
c.shape
tuple_c=c.shape#各轴长度：(3, 4)，即0轴长度为3，1轴长度为4
c.shape=4,3#在保持数组元素个数不变的情况下，改变数组每个轴的长度;并不是对数组进行转置,只是改变每个轴的
大小，数组元素在内存中的位置并没有改变
print(c)#

d=a.reshape((2,2))#reshape()方法，可以创建指定形状的新数组，而原数组的形状保持不变
#----数组a 和d 其实共享数据存储空间，因此修改其中任意一个数组的元素都会同时修改另外一个数组的内容：
a[0]=100
print(a)
print(d)

a.dtype#过dtype 参数在创建数组时指定元素类型
e=np.array([1,2,3,4],dtype=float)

#arange()类似于内置函数range()，通过指定开始值、终值和步长创建表示等差数列的一维数组，注意得到的结果数组不包含终值。
f=np.arange(0,1,0.1)
print(f)

#linspace()通过指定开始值、终值和元素个数创建表示等差数列的一维数组，可以通过endpoint 参数指定是否包含终值，默认值为True，即包含终值。
g_0=np.linspace(0,1,10)
print(g_0)#array([0.        , 0.11111111, 0.22222222, 0.33333333, 0.44444444,0.55555556, 0.66666667, 0.77777778, 0.88888889, 1.        ])

g_1=np.linspace(0,1,10,endpoint=False)
print(g_1)#:array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

#logspace()创建等比数列
h_0=np.logspace(0,1,10)
h_1=np.logspace(0,1,10,endpoint=False)
h_2=np.logspace(0,1,10,base=2,endpoint=False)#基数可以通过base 参数指定，默认值为10。

#numpy中的常量
numpy.pi#pi
numpy.e#e

#字符串

s = "abcdefgh"
list_int=np.fromstring(s,dtype=np.int8)#如果从字符串s 创建一个8 bit 的整数数组，所得到的数组正好就是字符串中每个字符的ASCII 编码
list_float=np.fromstring(s,dtype=np.float)#把整个字符串转换为一个64 bit 的双精度浮点数数组
'''如果我们用C 语言的二进制方式写了一组double 类型的数值到某个文件中，那么就可以从此文件中读取相应的数据，并通过fromstring()将其转换为
float64 类型的数组。或者直接使用fromfile()从二进制文件中读取数据。
'''
#将二进制array写入一个二进制文件中
str='abcdefghijklmnopqrstuvwxyz'
list_1=np.fromstring(str,dtype=np.int8)
list_1.tofile("list_1.bin")




