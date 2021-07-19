'''
    首先以写模式打开文件，之后将文本写入json
'''
import json
# 首先打开一个json文件
sp = open('mt.json', 'w')
# 建立一个列表
mt = [{'a': 6, 'b': 5, 'c': 4}, {'e': 'blue', 'f': 'red'}]
# 对列表对象进行编码生成json文件
json.dump(mt, sp, indent=4, sort_keys=True)
# 打开一个json文件，并进行读文件操作，生成一个字符串对象
js = open('js.json', 'r').read()
# 转换一个字符串对象为列表对象
print(json.loads(js))
# 打开一个json文件，生成一个文件对象
jt = open('js.json', 'r')
# 转换一个json文件为列表对象
print(json.load(jt))
