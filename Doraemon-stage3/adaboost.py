import numpy as np
import pandas as pd


# 在这个案例中正确分类，要求标签是-1和+1，sign函数方便
def sigmoid(inX):  #sigmoid函数
    return 1.0 / (1 + np.exp(-inX))


def stump_classify(data_matrix, dimen, thresh_val, thresh_ineq):  # just classify the data

    # 通过阈值比较，一边分成-1，一边为1，可以通过数组对比
    ret_array = np.ones((np.shape(data_matrix)[0], 1))
    # 看看是哪一边取-1
    if thresh_ineq == 'lt':
        ret_array[data_matrix[:, dimen] <= thresh_val] = -1.0
    else:
        ret_array[data_matrix[:, dimen] > thresh_val] = -1.0
    return ret_array


# 这是一个弱决策器
def build_stump(data_arr, class_labels, d):
    # 遍历所有可能的值到stump_classify种，找到最佳的单层决策树
    # 这里的最佳是通过权重向量d来定义
    data_matrix = np.mat(data_arr)
    label_mat = np.mat(class_labels).T  # 让它站起来
    m, n = np.shape(data_matrix)
    num_steps = 10.0  # 在特征所有可能值上遍历，超出也无所谓
    best_stump = {}  # 这个字典存储给定权重d时所得到的最佳决策树相关信息
    best_clas_est = np.mat(np.zeros((m, 1)))
    min_error = np.inf  # init error sum, to +infinity，一开始被初始为无穷大
    for i in range(n):  # loop over all dimensions一层在所有特征上遍历
        range_min = data_matrix[:, i].min()  # 固定列的最小值
        range_max = data_matrix[:, i].max()
        step_size = (range_max - range_min) / num_steps  # 设定步长
        # 二层遍历所有当前特征
        for j in range(-1, int(num_steps) + 1):  # loop over all range in current dimension
            # 在大于小于特征间切换不等式
            for inequal in ['lt', 'gt']:  # go over less than and greater than
                thresh_val = (range_min + float(j) * step_size)  # 阈值慢慢挪动
                # 调用前面定义的分类函数
                predicted_vals = stump_classify(data_matrix, i, thresh_val,
                                                inequal)  # call stump classify with i, j, lessThan
                err_arr = np.mat(np.ones((m, 1)))
                err_arr[predicted_vals == label_mat] = 0  # 分错了就是0
                weighted_error = d.T * err_arr  # calc total error multiplied by D

                # print("split: dim %d, thresh %.2f, thresh ineqal: %s, the weighted error is %.3f" % (
                #     i, thresh_val, inequal, weighted_error))
                if weighted_error < min_error:
                    # 如果找到了一个最好的版本，就全部换成这个
                    min_error = weighted_error
                    best_clas_est = predicted_vals.copy()
                    best_stump['dim'] = i
                    best_stump['thresh'] = thresh_val
                    best_stump['ineq'] = inequal
    return best_stump, min_error, best_clas_est


def adaboost_trainDS(data_arr, class_labels, num_iter=40):
    # 输入，数据集，类别标签，迭代次数num_iter
    # DS,单层决策树，decision stump，最流行的弱分类器。但事实上，任何分类器都可以充当弱分类器
    weak_class_arr = []  # 一个单层决策树的数组
    m = np.shape(data_arr)[0]
    d = np.mat(np.ones((m, 1)) / m)  # init D to all equal  # 包含数据点的权值
    agg_class_est = np.mat(np.zeros((m, 1)))  # 每个数据点类别估计累计值
    for i in range(num_iter):
        # 第一件事就是建树，返回的是利用d而得到的具有最小错误率的单层决策树
        # 同时还返回最小错误率及估计的类别向量
        best_stump, error, class_est = build_stump(data_arr, class_labels, d)  # build Stump
        # print("d:", d.T)
        # 重头戏，估计alpha值，告诉总分类器本次单层决策树输出结果的权重
        # 1e-16是避免除零溢出
        alpha = float(0.5 * np.log(
            (1.0 - error) / max(error, 1e-16)))  # calc alpha, throw in max(error,eps) to account for error=0
        # 接下来把分类器和权重都放进去
        best_stump['alpha'] = alpha
        weak_class_arr.append(best_stump)  # store Stump Params in Array
        # print("classEst: ", class_est.T)
        expon = np.multiply(-1 * alpha * np.mat(class_labels).T, class_est)  # exponent for D calc, getting messy
        d = np.multiply(d, np.exp(expon))  # Calc New D for next iteration
        d = d / d.sum()
        # calc training error of all classifiers, if this is 0 quit for loop early (use break)
        agg_class_est += alpha * class_est
        # print("aggClassEst: ", agg_class_est.T)
        # sign是保证结果是二值的
        agg_errors = np.multiply(np.sign(agg_class_est) != np.mat(class_labels).T, np.ones((m, 1)))
        error_rate = agg_errors.sum() / m
        # print("total error: ", error_rate)
        if error_rate == 0.0: break  # 运行直到误分类为0
    return weak_class_arr, agg_class_est


def ada_classify(dat2class, classifier_arr):
    # 输入是待分样例和弱分类器集合
    # 仅仅是利用了前面训练好的分类器
    data_matrix = np.mat(dat2class)  # do stuff similar to last aggClassEst in adaBoostTrainDS
    m = np.shape(data_matrix)[0]
    agg_class_est = np.mat(np.zeros((m, 1)))  # 全0列向量
    for i in range(len(classifier_arr)):  # 遍历所有的弱分类器
        # 用单层决策树获得每个分类器自己的决策值
        class_est = stump_classify(data_matrix, classifier_arr[i]['dim'], classifier_arr[i]['thresh'],
                                   classifier_arr[i]['ineq'])  # call stump classify
        # 输出结果是累加
        agg_class_est += classifier_arr[i]['alpha'] * class_est
    # print(agg_class_est)  # 这个例子中，值越来越小
    # 要满足不超界，大于0为+1，小于0为-1
    return np.sign(agg_class_est),sigmoid(agg_class_est)
    # return sigmoid(agg_class_est)

def house_prediction(train_path,test_path):
    df_train = pd.read_csv(train_path)
    df_test = pd.read_csv(test_path)

    train = df_train.iloc[:, 1:-1].values
    # print(train)
    train_label = df_train.iloc[:,-1].values
    for i in range(len(train_label)):
        if(train_label[i] == 0):
            train_label[i] = -1
    # print(train_label)
    classifier_array, agg_class_est = adaboost_trainDS(train, train_label, 40)

    test = df_test.iloc[:, 1:].values
    prediction = ada_classify(test, classifier_array)[1]
    # print(prediction)
    return  prediction
def getPrediction():
    train_path = "src/step1/input/train.csv"
    test_path = "src/step1/input/test.csv"
    # train_path = "E:\\Workspace\\PycharmProjects\\eduencoder\\final\\input\\train.csv"
    # test_path = "E:\\Workspace\\PycharmProjects\\eduencoder\\final\\input\\test.csv"
    # tf_train_list, tf_test_list = dataload(train_path,test_path)
    prediction = house_prediction(train_path, test_path)

    address = pd.read_csv(test_path, usecols=[0])
    new_address = address.values.tolist()
    new_address = [str(n) for a in new_address for n in a]
    prediction = prediction.tolist()
    predict = []
    for i in range(len(prediction)):
        predict.append(prediction[i][0])
    # print(predict)
    df = pd.DataFrame({'ID': new_address, 'TARGET': predict})
    df.to_csv("src/output/test_prediction.csv", index=False)
    # df.to_csv("E:\\Workspace\\PycharmProjects\\eduencoder\\final\\input\\test_prediction.csv", index=False)


getPrediction()
