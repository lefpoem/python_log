a, b = 0, 1
while a < 1000: # 输出不大于1000的数列
    print(a, end=',') # F(0)=0,F(1)=1
    # 同步赋值语句，同时对多个变量进行赋值，避免多个无关变量同步赋值
    a, b = b, a+b # 右边计算完毕之后，同时对变量赋值
# 对于