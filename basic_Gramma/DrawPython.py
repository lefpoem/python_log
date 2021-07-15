'''
    Python对大小写敏感,
    正向递增序列，反向递减序列
    函数可以理解为对特定功能表达式的封装，
    接收变量并输出结果，缩进代码表示一种所属关系
'''
import turtle

# 定义函数
def drawSnake(radius,angle,length):
    turtle.seth(-40)
    for i in range(length):
        turtle.circle(radius,angle)
        turtle.circle(-radius,angle)
    turtle.circle(radius,angle/2)
    turtle.fd(40)
    turtle.circle(16,180)
    turtle.fd(40*2/3)

# 主内容
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
drawSnake(40,80,4)
turtle.done()
