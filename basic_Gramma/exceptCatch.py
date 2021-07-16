'''
    else是对无异常时的追加，
    finally无论 是否出现异常都要执行。
'''
try:
    num = eval(input("请输入一个整数:"))
    print(num**2)
except NameError:
    print("Invalid Value")
except :
    print("其他错误")
else: # 无异常时执行
    print("无异常时执行")
finally:
    print("有无异常")