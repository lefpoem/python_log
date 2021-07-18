'''
    jieba库使用在自然语言处理领域
'''
import jieba
# 搜索引擎模式，适用于搜索引擎分词
print(jieba.lcut_for_search("中华人民共和国一个强大的国家！"))
# 精确模式，适用于文本分析，完整且不多余的产生原生文本
print(jieba.lcut("中华人民共和国是一个强大的国家！"))
# 全模式，输出文本中所有可能的单词，产生所有可能产生的所有问题，冗余性最大
print(jieba.lcut("中华人民共和国是一个强大的国家！"))
# 添加一个新词
jieba.add_word("强大的")
print(jieba.lcut("中华人民共和国是一个强大的国家！"))
c = jieba.cut("中国是一个强大的国家！")
print(list(c))
