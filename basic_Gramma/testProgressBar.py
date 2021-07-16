'''
    带刷新的文本进度条
'''

import time
print("执行开始".center(16,'-'))
scale = 10
# version3.9 don't support time.clock().
t = time.process_time() # 使用一个计时器
for i in range(scale+1):
    a,b = "**"*i,"--"*(scale-i)
    c = (i/scale)*100
    t -= time.process_time()
    # \r光标回到本行首行
    print("\r{:>3.0f}% [{}->{}]".format(c,a,b),end='')
    time.sleep(0.1) # 增加程序暂时挂机，增加停留时间
print("\n{0:-^16}".format("执行结束"))
