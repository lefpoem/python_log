import json
fd = open("wine.json",'r')
ls = json.load(fd) # 生成一个数据类型对象,一般来说是一个列表
data = [list(ls[0].keys())]
for item in ls:
    data.append(list(item.values()))
fd.close()
ft = open('wine1.csv','w')
# 字符串分隔函数join，以及字符串加法操作
for item in data:
    ft.write(','.join(item)+'\n')
ft.close()
