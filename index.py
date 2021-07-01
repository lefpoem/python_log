import numpy as np 
 # 索引坐标（0，0），（1,1),(2,0)
x = np.array([[1,  2],  [3,  4],  [5,  6]]) 
y = x[[0,1,2],  [0,1,0]]  # x[rows,cols]

m=np.arange(32).reshape((8,4))
print(m[[4,2,1,7]])# 4,2,1,7指行
print(m[[-4,-6,-7,-1]]) # 倒叙索引
print(y)
