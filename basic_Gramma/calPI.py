'''
    通过蒙特卡罗方法对PI进行估计计算。
    首先PI的计算可以转换为，计算圆的面积。
    通过随机抛点，对在圆范围内的点数进行统计。
    圆内点数/正方形内点数的比可近似为PI/4.
'''

# Mento Carol
from random import random
from math import sqrt
from time import process_time

DARTS = 10000
hits = 0
process_time()
for i in range(DARTS + 1):
    x,y = random(),random()
    dist = x**2 + y**2
    if dist <= 1:
        hits += 1
pi = 4*hits/DARTS
print("PI的值为：{}".format(pi))
print("运行时间为{:5.5}s".format(process_time()))