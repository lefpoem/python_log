'''
    华氏温度和摄氏度转换，华氏温度=摄氏温度*1.8+32，
    IPO模式（input,process,output),
    if-elif-else 条件结构使用。
    eval函数，解析"Hello"为hello变量，由于未进行赋值，
    则解释器会报错。解析"'hello'"为'hello'即为一个字符。
'''

def TempConvert(ValueStr):
    # 方括号和逗号组成的类型叫列表，格式为[元素1,元素2,...,元素n]
    while TempStr[-1] not in ['N', 'n']:
        if TempStr[-1] in ['F', 'f']:
            # eval(<字符串>)解析并执行字符串
            C = (eval(TempStr[0:-1]) - 32)/1.8
            print("转换后的温度值为:%.2fC" % C)
            break
        elif TempStr[-1] in ['C', 'c']:
            F = eval(TempStr[0:-1])*1.8+32
            print("转换后的温度值为:{:.2f}F".format(F))
            break
        else:
            print("输入格式错误。")


TempStr = input("请输入带有符号的温度值: ")
TempConvert(TempStr)
