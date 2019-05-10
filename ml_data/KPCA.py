from sklearn.decomposition import KernelPCA
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from sklearn import svm
from sklearn.model_selection import StratifiedKFold #交叉验证
from sklearn.model_selection import GridSearchCV #网格搜索

def kpca1(data_path):
    import pandas as pd
    df = pd.read_csv(data_path, header=None)
    # print(df)
    rowNum = df.shape[0]  # 不包括表头
    colNum = df.columns.size
    dataset = df.values
    y = dataset[1][1:].astype('int')  # category
    tmp = dataset[0:5][:,1:].transpose()
    samples = dataset[0]
    samples = samples[1:]
    samples = samples.tolist()
    waves = ['wavelength ' + str(i) for i in dataset[:,0][5:].tolist()]
    data = pd.DataFrame(columns=[*samples], index=waves)
    i = 5
    for wave in data.index:
        data.loc[wave, dataset[0][1]:dataset[0][-1]] = np.mat(dataset[i][1:])
        i = i + 1
    # tmp = data.values.astype('float')
    scaled_data = preprocessing.scale(data.T)
    kpca = KernelPCA(kernel="rbf", n_components=1000)
    x_kpca = kpca.fit_transform(scaled_data)
    print(x_kpca)

    # SVM:
    # y1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    # clf = svm.SVC(kernel='linear')
    # classifier_poly = svm.SVC(kernel='linear', gamma=0.1, decision_function_shape='ovo', C=0.1)
    # classifier_poly = svm.SVC(kernel='rbf', gamma=0.1, decision_function_shape='ovo', C=0.8)
    # from sklearn.multiclass import OneVsRestClassifier
    # clf = OneVsRestClassifier(svm.SVC(kernel='linear'))
    # clf = svm.SVC(kernel='poly', degree=3)
    # clf = svm.SVC(kernel='rbf', gamma=0.2, decision_function_shape='ovo', C=1.5) : adjust

    # gamma = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    # C = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    # param_grid = dict(gamma=gamma, C = C)  # 转化为字典格式，网络搜索要求
    # grid_search = GridSearchCV(clf, param_grid, scoring='neg_log_loss', n_jobs=-1, cv=3)
    # grid_result = grid_search.fit(x_kpca, y)  # 运行网格搜索
    # print(grid_result.best_score_)
    # print(grid_search.best_params_)

    clf = svm.SVC(kernel='linear', gamma=0.1, decision_function_shape='ovo', C=0.9)
    clf.fit(x_kpca, y)
    y_pred = clf.predict(x_kpca)
    print(y)
    print(y_pred)

kpca1('/Users/skye/PycharmProjects/20190302/data/ml_dataset/训练数据集.csv')
