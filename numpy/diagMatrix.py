import numpy as np
a = np.eye(3,dtype=int)
# k indictes the diagonal
b = np.eye(3,k=-2,dtype=int)# 只有已选择的对角线数字为1
c = np.diag(b,k=-2)
print(a)
print(b,c)
