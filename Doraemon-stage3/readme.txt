不调用库函数，使用adaboost方法预测购买房屋/车险等概率
输入：train.csv，test.csv文件
train.csv文件格式为：ID,特征（多列），标签
test.csv文件格式为:ID，特征
要求输出：test_prediction.csv
文件格式为：对应test.csv中的ID，预测的概率

简单修改一下路径即可

后续：没有对数据做异常处理，由于不清楚每列特征代表的含义，数据清洗后的结果未知
按理说应该提出训练数据中的异常值