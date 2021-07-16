"""
    通过计算BMI指数熟悉多分支结构的使用
"""

height, weight = eval(input("请输入身高(m)\
和体重(kg)[comma seperate]:"))
bmi = weight/height**2
print("BMI指数为:{:.2f}".format(bmi))
who, dom = "", ""  # 若输入错误，则打印空
if bmi < 18.5:
    who, dom = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, dom = "正常",  "正常" # 没有赋值方法为who = '',dom = ''
elif 24 <= bmi < 25:
    who, dom = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, dom = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, dom = "偏胖", "肥胖"
else:
    who, dom = "偏胖", "肥胖"
print("BMI指标为：国内'{1}'，国际'{0}'".format(who, dom))
