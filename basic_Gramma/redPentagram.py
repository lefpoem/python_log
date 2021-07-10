'''
    画一个填充红色的pentagram
'''
from turtle import *
fillcolor ('red')
begin_fill()
while True:
    forward(200)  # 控制前进距离
    right(144)  # 控制转向角度
    # pos 返回当前游标coordinate
    if abs(pos()) < 1:
        break
end_fill()
done()