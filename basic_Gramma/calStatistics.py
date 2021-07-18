'''
    本例子进行一些统计学计算
'''
from math import sqrt


def getNum():
    nums = []
    iNumstr = input("请输入数字（直接输入回车退出）：")
    while iNumstr != "":
        nums.append(eval(iNumstr))
        iNumstr = input("请输入数字（直接输入回车退出）：")
    return nums


def mean(numbers):
    s = 0.0
    for i in numbers:
        s += i
    return s/len(numbers)


def dev(numbers, mean):
    sdev = 0.0
    for i in numbers:
        sdev += (i-mean)**2
    return sqrt(sdev/(len(numbers)-1))


def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = ((numbers[size//2-1])+numbers[size//2]) / 2
    else:
        med = numbers[size//2]
    return med


n = getNum()
m = mean(n)
print("平均值：{},标准差{:.2f},中位数：{}".format(m,\
    dev(n,m),median(n)))
