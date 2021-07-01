import numpy as np
# arange [0,10) step=1,9 items
a = np.arange(10)
# slice  index[2,7),step=2,3 items endpoint=false
s = slice(2,8,2)
# the second slice
c = a[2:7:2] # a[start:stop:step] endpoint=false
# slice 2-D arrays
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
d = b[1:]
print(a[s]) 
print(c)
print(d)
# ,seperate dimensions
print(b[...,1])
print(b[1,...])
print(b[...,1:])