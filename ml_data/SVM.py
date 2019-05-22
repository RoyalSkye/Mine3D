import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn import svm as svm1
import matplotlib.pyplot as plt
import ml_data.PCA as p
from sklearn.model_selection import train_test_split
from ml_data.LDA import lda1
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
from sklearn.model_selection import GridSearchCV

# 将分类器绘制到图中
def plot_classifier(classifier, X, y, path):
    x_min, x_max = min(X[:, 0]) - 1.0, max(X[:, 0]) + 1.0 # 计算图中坐标的范围
    y_min, y_max = min(X[:, 1]) - 1.0, max(X[:, 1]) + 1.0
    step_size = 0.1  # 0.01 too time-consuming !!
    x_values, y_values = np.meshgrid(np.arange(x_min, x_max, step_size),
                                     np.arange(y_min, y_max, step_size))
    # 构建网格数据
    mesh_output = classifier.predict(np.c_[x_values.ravel(), y_values.ravel()])
    mesh_output = mesh_output.reshape(x_values.shape)
    plt.figure()
    plt.pcolormesh(x_values, y_values, mesh_output, cmap=plt.cm.gray)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=80, edgecolors='black',
                linewidth=1, cmap=plt.cm.Paired)
    # specify the boundaries of the figure
    plt.xlim(x_values.min(), x_values.max())
    plt.ylim(y_values.min(), y_values.max())

    # specify the ticks on the X and Y axes

    range_x = int(max(X[:, 0])) - int(min(X[:, 0]))
    range_y = int(max(X[:, 1])) - int(min(X[:, 1]))
    intervel_x = range_x / 10.0
    intervel_y = range_y / 10.0
    plt.xticks((np.arange(int(min(X[:, 0])), int(max(X[:, 0])), intervel_x)))
    plt.yticks((np.arange(int(min(X[:, 1])), int(max(X[:, 1])), intervel_y)))
    plt.savefig(path)
    plt.show()

def plot_confusion_matrix(y_true, y_pred, classes, path,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues,):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    # print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    plt.savefig(path)
    plt.show()
    return ax

def svm1(data_path):
    dataset = p.pca1(data_path)
    # print(dataset)
    # prepare data for SVM
    samples = dataset[:,[0,2,3,4]]
    train_X = dataset[:, 5:]
    train_y = dataset[:, 1].astype('float').astype('int')
    target_names = ["Hematite", "magnetite", "martite"]
    count = 0
    category = []
    for i in train_y:
        if i not in category:
            count = count + 1
            category.append(i)
    if count != 3:
        target_names = []
        for i in category:
            target_names.append('type' + str(i))
    mapx = {}
    mapy = {}
    for i in range(0, count):
        namex = 'x'+str(i)
        namey = 'y' + str(i)
        mapx[namex] = []
        mapy[namey] = []
    for row in dataset:
        for i in range(0, count):
            if float(row[1]) == i:
                namex = 'x' + str(i)
                namey = 'y' + str(i)
                mapx[namex].append(row[5])
                mapy[namey].append(row[6])
                break
    scatter = []
    markers = ['o', 'x', 'v', '.', '^', '<', '>', '1', '2', '3', '4', '8'
        , 's', 'p', '*', 'h', 'H', '+', ',', 'D', 'd', '|']
    colors=['b','r','g','k','m','w','c','y']
    for i in range(0, count):
        scatter.append(plt.scatter(mapx['x'+str(i)], mapy['y'+str(i)], c=colors[i], marker=markers[i]))
    plt.legend(handles=scatter, labels=target_names, loc="best")
    plt.savefig("./images/PCA+SVM/img2.png")
    plt.show()

    # svm: classifier_poly = SVC(kernel='linear', gamma=0.1, decision_function_shape='ovo', C=0.1)
    # svm1: classifier_poly = SVC(kernel='rbf', gamma=0.1, decision_function_shape='ovo', C=0.8)
    # svm2: OneVsRestClassifier(SVC(kernel='linear'))
    # svm3: classifier_poly = SVC(kernel='poly', degree=3)
    # svm4: classifier_poly = SVC(kernel='rbf', gamma=0.2, decision_function_shape='ovo', C=1.5) : adjust C from 0.8-1.0-1.2-1.5
    # classifier_poly = SVC(kernel='linear', gamma=0.1, decision_function_shape='ovo', C=0.1)
    # classifier_poly = SVC(kernel='rbf', gamma=0.1, decision_function_shape='ovo', C=0.8)
    # from sklearn.multiclass import OneVsRestClassifier
    # classifier_poly = OneVsRestClassifier(SVC(kernel='linear'))
    # classifier_poly = SVC(kernel='poly', degree=3)

    # grid search
    param_grid = {"gamma": [0.01, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5],
                  "C": [0.5, 0.7, 1.0, 1.2, 1.5, 1.8]}
    print("Parameters:{}".format(param_grid))
    grid_search = GridSearchCV(SVC(), param_grid, cv=5)  # 实例化一个GridSearchCV类
    clf = grid_search.fit(train_X, train_y)  # 训练，找到最优的参数，同时使用最优的参数实例化一个新的SVC estimator。
    print(grid_search.best_params_)
    print(grid_search.best_score_)
    # classifier_poly = SVC(kernel='rbf', gamma=0.2, decision_function_shape='ovo', C=1.5)
    # clf = classifier_poly.fit(train_X, train_y)
    plot_classifier(clf, train_X, train_y, './images/PCA+SVM/img3.png')

    # save svm model
    from sklearn.externals import joblib
    joblib.dump(clf, './model/PCA+SVM/svm.pkl')

    # restore
    from sklearn.externals import joblib
    clf = joblib.load('./model/PCA+SVM/svm.pkl')

    print('SVM在训练集上的准确率: ', clf.score(train_X, train_y))
    y_pred = clf.predict(train_X)
    print(train_y)
    print(y_pred)

    # plot confusion matrix
    # note: classes must be type of numpy.ndarray
    plot_confusion_matrix(train_y, y_pred, classes=np.array(target_names), path='./images/PCA+SVM/img4.png', title='Confusion matrix, without normalization')
    # plot_confusion_matrix(train_y, y_pred, classes=np.array(target_names), normalize=True, title='Normalized confusion matrix')

    # note: precision = '2' in y_pred/ '2' in train_y
    # but it have no influence on the total precision
    training_report = classification_report(train_y, y_pred, target_names=target_names)
    print(training_report)
    map = {}
    map['training_report'] = training_report
    map['accuracy'] = clf.score(train_X, train_y)
    # result = np.column_stack((samples, y_pred))
    # map['result'] = result
    # print(map)
    return map

def prediction(data_path, modelpath, method):
    if method == 1:
        dataset = p.pca1(data_path, prediction=True)
        # print(dataset)
    elif method == 2:
        dataset = lda1(data_path, prediction=True)
        # print(dataset)
    else:
        pass
    # print(dataset)
    samples = dataset[:, [0,2,3,4]]
    train_X = dataset[:, 5:]
    y = dataset[:, 1].astype('int')
    # print(y)
    # print(train_X)
    # train_y = dataset[:, 1].astype('float').astype('int')
    from sklearn.externals import joblib
    clf = joblib.load(modelpath)
    y_pred = clf.predict(train_X)
    plot_classifier(clf, train_X, y_pred, './images/prediction/img2.png')
    # print(y_pred)
    result = np.column_stack((samples, y_pred))
    map = {}
    map["result"] = result
    map["accuracy"] = clf.score(train_X, y)
    # print(map)
    return map

# svm1('/Users/skye/PycharmProjects/20190302/data/光谱数据.xls')
# svm1('/Users/skye/PycharmProjects/20190302/data/训练数据集.csv')
# prediction('/Users/skye/PycharmProjects/20190302/data/测试(预测)数据集.csv')