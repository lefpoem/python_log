'''
    组合数据变量（列表）额尔
    无局部列表变量时，
    对全局列表变量进行修改
'''
ls = [] #  全局列表变量


def func(a, b):
    ls = [] # 局部列表变量 
    ls.append(b)
    return a*b


s = func("knock~", 2)
print(s, ls)
