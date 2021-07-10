for i in range(1,10):
    for j in range(1,i+1):
        # {:1}1位长度，' '结尾加一个空格
        print("{}*{}={:1}".format(i,j,i*j),end=' ')
    # 每一内循环输出完，进行换行
    print('')