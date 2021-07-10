'''
    画一个太阳花
'''
from turtle import *
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(170) # 指定角度
    if abs(pos()) < 1:
        break
end_fill()
done()