'''
   本次使用一个UCI数据集wine进行训练，本数据集具有14个属性，
属性指明酒中的化学成分。目的是检验数据标记
   使用pandas读入数据的意义是方便处理。利用iloc转换为数组
'''
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, OneClassSVM
source_data = pd.read_csv("wine.data", header=None)
print("数据量数：{}".format(len(source_data)))
# 利用x.columns.size返回列数
print("数据列数：{}".format(source_data.columns.size))
# 样本随机化,防止选不到第三种红酒
source_data = shuffle(source_data)

# 产生训练数据,125个样本
x_train = source_data.iloc[:125, 1:14]
# 训练集的标记，125个
y_train = source_data.iloc[:125, 0]
# 53 obserbations
x_test = source_data.iloc[125:, 1:14]
# 53 notes
y_test = source_data.iloc[125:, 0]

# 防止尺度敏感，进行标准化。
scaler = StandardScaler()  # (x-u)/s
scaler.fit(x_train)
x_train_standard = scaler.transform(x_train)
scaler.fit(x_test)
x_test_standard = scaler.transform(x_test)

# 转换y_test为列表s
y_train_list = y_train.tolist()
y_test_list = y_test.tolist()
print("测试集的目标类别：{}".format(y_test_list))

# 使用rbf核SVC算法训练模型
plf = SVC(kernel="rbf", C=600,gamma=0.1)
plf.fit(x_train_standard, y_train)


# 使用模型
y_pred_train = plf.predict(x_train_standard)
y_pred_test = plf.predict(x_test_standard)

# 转为列表
y_pred_train_list = list(y_pred_train)
y_pred_test_list = list(y_pred_test)

# 真实标记与预测标记进行比对并计数
n_correct_test = sum([1 for n in range(len(y_test_list))
                      if y_pred_test_list[n] == y_test_list[n]])
n_correct_train = sum([1 for n in range(len(y_train_list))
                      if y_pred_train_list[n] == y_train_list[n]])
# 输出正确率
print("测试集正确率：{}".format(n_correct_test/len(y_test_list)))
print("训练集正确率：{}".format(n_correct_train/len(y_train_list)))
