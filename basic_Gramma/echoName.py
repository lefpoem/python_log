name = input("输入姓名:")
# 输出格式为槽位置+format方法:.2f表示输出数值取两位小数
print("{}同学，欢迎来到Python！".format(name))
print("{}大侠,欢迎来到Python!".format(name[0]))
print("{}哥哥,欢迎来到Python!".format(name[1:]))
print("%s同学，欢迎来到Python!"%name)
print("%s大侠，欢迎来到Python!"%name[0])
print("%s同学,欢迎来到Python!"%name[1:])

