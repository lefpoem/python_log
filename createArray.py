import numpy  as np
# empty return raw darray,"order" indicates the order of elments in memory
x = np.empty([3,2],dtype=int,order='C')
print(x)
# create arrays and fill '0'
y = np.zeros([3,2],dtype=int,order='C')
print(y)
z = np.ones([3,2],dtype=int,order='C')
e = y.itemsize
print(z)