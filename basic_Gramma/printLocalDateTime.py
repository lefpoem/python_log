from datetime import datetime
now = datetime.now() # 输出现在的时间
print(now)
now.strftime("%x") # 输出时间的日期部分
now.strftime("%X") # 输出时间的时间部分