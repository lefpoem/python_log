'''
    本代码实现csv文件转Json文件
'''
import json
fd = open('wine.csv', 'r')
ls = []
for line in fd:
    line = line.replace('\n', '')
    # 以,划分为字符之后，加其按每行为一个元素加入到列表中
    ls.append(line.split(','))
fd.close()
# print(len(ls)) 为178
fw = open('wine.json', 'w')
for i in range(1, len(ls)):
    # zip函数组成一个关系对插入到字典中
    ls[i] = dict(zip(ls[0], ls[i]))
json.dump(ls[1:], fw, sort_keys=False, indent=4)
fw.close()
