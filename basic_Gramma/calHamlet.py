'''
    通过计算hamlet文本使用map
    并进行模块化设计,但并未使用类进行封装
'''


def getText(str):  # 获取待处理文本
    txt = open(str, 'r').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        txt = txt.replace(ch, ' ')
    return txt


def processText(words,counts,excludes):  # 处理文本，创建字典，将文本存入字典
    for word in words:  # 插入文本到字典
        counts[word] = counts.get(word, 0)+1
    for word in excludes:
        del(counts[word])
    items = list(counts.items())  # 转换为列表
    items.sort(key=lambda x: x[1], reverse=True)  # 以第二列ok进行排序
    return items  # 返回key-value对


def main(s):
    hamlet = getText(s)
    words = hamlet.split()  # 字符串划分函数
    counts = {} # 创建字典
    # 创建排除集
    excludes = {"the","and","of","you","a","my","i","in"}
    items = processText(words,counts,excludes)
    for i in range(10):  # 输出前10个key-value对
        word, count = items[i]
        print("{0:<10}{1:>5}".format(word, count))


main("Halmet.txt")
