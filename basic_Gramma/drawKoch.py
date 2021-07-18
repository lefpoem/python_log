'''
    通过绘制koch曲线，理解递归函数的使用，
    koch中n指示阶数，size指示线的长度.
'''
import turtle


def koch(size, n):
    if n == 0:
        turtle.pencolor("purple")
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)


def main():
    turtle.setup(800, 800)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300, 175)
    turtle.pendown()
    turtle.pensize(2)
    turtle.fillcolor("gold")
    turtle.begin_fill()
    koch(600, 3)
    turtle.right(120)
    koch(600, 3)
    turtle.right(120)
    koch(600, 3)
    turtle.end_fill()
    turtle, turtle.hideturtle
    
    turtle.done()


main()
