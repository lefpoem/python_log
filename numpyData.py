import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)
a.shape = (3,2) # 调整数组
print(a)
f = a.reshape(2,3) # 调整数组,改变的是数组本身
print(f)
f[0,0]=100
print(a)
b = np.array([1],ndmin=2) #最小二维，会自动加[0]
print(b)
c = np.array([1,2,3],dtype = complex)
print(c)
dt = np.dtype(np.complex)
print(dt)
dt2 = np.dtype('i4')
print(dt2)
dt3 = np.dtype([('age',np.int8)])
e = np.array([(10,),(20,),(30,)],dtype=dt3)
print(e)
print(e.itemsize)
print(e['age']) # 存取age列
print(e.flags)