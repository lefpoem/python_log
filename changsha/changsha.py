#%%
import pandas as pd
import numpy as np
source_data = pd.read_csv("mocel.csv", header=None)
raw_data=np.asarray(source_data)
s_data=raw_data.reshape(11,11)
print("数据形状：{}".format(s_data.shape))
c=np.zeros((11,11))
d=0
i=0
while i < 11:
    m=0
    s=0
    t=1000
    for  j in range(11):
        if  s_data[i][j] <= t and s_data[i][j]!=0:
            if c[i][j]!=1:
                t=s_data[i][j]
                m=i
                s=j

    d += t

    if c[m][s]==1:
        break
    else:
        c[m][s]=1
        c[s][m]=1
        i=s

print("The shortest length is {}".format(d))

# %%
