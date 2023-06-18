import numpy as np

#ufunc函数计算
#ufunc 是universal function 的缩写，它是一种能对数组中每个元素进行操作的函数。NumPy内置的许多ufunc 函数都是在C 语言级别实现的，因此它们的计算速度非常快。

x=np.linspace(0,2*np.pi,10)#linspace()产生一个从0 到2pi的等差数组
y=np.sin(x)


a = np.arange(0,4)
b = np.arange(1,5)

np.add(a,b)#add()返回一个数组，数组的每个元素都是两个参数数组中对应元素之和
np.add(a,b,a)#如果指定了第三个参数out，就不产生新的数组，而是直接将结果保存到指定的数组中


#常用运算符
x=np.array([1,2,3])
y=np.array([4,5,6])
z=np.array([1,2,0])

运 算 符 对应的ufunc 函数
y = x1 + x2 	add(x1, x2 [, y])
y = x1 - x2 	subtract(x1, x2 [, y])
y = x1 * x2 	multiply (x1, x2 [, y])
y = x1 / x2 	divide (x1, x2 [, y]), 如果两个数组的元素为整数，那么用整数除法
y = x1 / x2 	true_divide (x1, x2 [, y]), 总是返回精确的商
y = x1 // x2 	 (x1, x2 [, y]), 总是对返回值取整
y = -x 			negative(x [,y])
y = x1**x2 		power(x1, x2 [, y])
y = x1 % x2 r	emainder(x1, x2 [, y]),或mod(x1, x2, [, y])

#比较和布尔运算
x>y
x<y
x==y
x==z
#and、or 和not 等关键字,函数名都以“logical_”开头
np.logical_and(x>y,x<y)
np.logical_or(x>y,x<y)
np.logical_not(x==y,x==z)

np.any(x>y)
np.all(x==z)


