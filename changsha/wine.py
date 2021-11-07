'''
    本次设计为了解决寻找最短路径问题。
'''
import pandas as pd
import prim 
import numpy as np
source_data = pd.read_csv("mocel.csv", header=None)
raw_data=np.asarray(source_data)
s_data=raw_data.reshape(11,11)
print("数据列数：{}".format(s_data.shape))
c=np.zeros((11,11))
d=prim.Prim(0,0,0,11,s_data,c);
print("The shortest length is {}".format(d))
