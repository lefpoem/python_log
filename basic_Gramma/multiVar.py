'''
    本实例融合了
    1.可选参数
    2.可变数量参数
    3.全域变量与局部变量
'''
e = 1
# *b可变数量参数，c可选参数(有默认值)
def vfunc(a,*b,c=10):
    global e
    e = 4  # 此时也是对全局变量进行赋值
    for n in b:
        a += n
    a += c
    a += e
    return a,e
print(e) # 此时未调用vfunc，因此全局变量尚未更改
print(vfunc(1,2,3,4,5)) # 此时调用vfucn对全局变量赋值
print(e) # 此时e=4