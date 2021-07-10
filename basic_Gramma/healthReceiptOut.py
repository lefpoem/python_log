'''
    选定两种不同的食材组成菜式
'''
diet = ['西红柿','花椰菜','黄瓜','牛排','虾仁']
for i in range(0,5):
    for j in range(0,5):
        if not(i==j):
            # 两个以上输出字符串使用format()
            print("{}{}".format(diet[i],diet[j]))