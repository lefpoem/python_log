'''
    通过此代码了解函数的封装
    以及turtle,datetime
'''

from turtle import *
import datetime


def drawGap():  # 画数码馆间隔
    penup()
    fd(5)


def drawLine(draw):  # 设置可开关的单段数码管绘制函数
    drawGap()
    pendown() if draw else penup()
    fd(40)
    drawGap()
    right(90)


def drawDigit(d):  # 画单个数字
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
    left(90)
    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    penup()
    left(180)
    fd(20)


def drawDate(date):  # 画日期
    for i in date:
        if i == '-':
            write('年', font=("Arial", 18, "normal"))
            pencolor("green")
            fd(40)
        elif i == '=':
            write('月', font=("Arial", 18, "normal"))
            pencolor("blue")
            fd(40)
        elif i == '+':
            write('日', font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))


def main():  # 主函数，执行背景
    setup(800, 350, 200, 200)
    penup()
    pensize(5)
    fd(-300)
    drawDate(datetime.datetime.now().strftime('%Y-%m=%d+'))
    hideturtle()
    done()


main()
