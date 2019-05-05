import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn import svm as svm1
import matplotlib.pyplot as plt
import ml_data.PCA as p
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

# 将分类器绘制到图中
def plot_classifier(classifier, X, y):
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
    # print(int(min(X[:, 1]))) # -23
    # print(int(max(X[:, 1]))) # 30
    plt.xticks((np.arange(int(min(X[:, 0])), int(max(X[:, 0])), 20.0)))
    plt.yticks((np.arange(int(min(X[:, 1])), int(max(X[:, 1])), 10.0)))
    plt.savefig("./images/img7.png")
    plt.show()

def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
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
    plt.savefig("./images/img8.png")
    plt.show()
    return ax

def svm(filepath):
    data = p.pca(filepath)
    x0 = []
    y0 = []
    x1 = []
    y1 = []
    x = []
    y = []
    for key in data.keys():
        tmp = data.get(key)
        if tmp[2] == "赤铁矿":
            x0.append(tmp[0])
            y0.append(tmp[1])
            x.append([tmp[0], tmp[1]])
            y.append(0)
        elif tmp[2] == "假象矿":
            x1.append(tmp[0])
            y1.append(tmp[1])
            x.append([tmp[0], tmp[1]])
            y.append(1)
        else:
            pass
    scatter0 = plt.scatter(x0, y0, c='b', marker='o')
    scatter1 = plt.scatter(x1, y1, c='r', marker='x')
    plt.legend(handles=[scatter0, scatter1], labels=["Hematite", "martite"], loc="best")
    plt.savefig("./images/img2.png")
    plt.show()

    # SVM
    train_X = np.array(x)
    train_y = np.array(y)
    # print(model.score(X, Y))

    import time
    time_start = time.time()
    # 第一种：使用多项式核函数：
    # classifier_poly = SVC(kernel='poly', degree=3, probability=True)  # 三次多项式方程
    classifier_poly = SVC(kernel='poly', degree=3)
    classifier_poly.fit(train_X, train_y)
    time_end = time.time()
    print('SVM: ', time_end - time_start, 's')

    # save svm model
    from sklearn.externals import joblib
    joblib.dump(classifier_poly, './model/svm.pkl')

    # restore
    classifier_poly = joblib.load('./model/svm.pkl')

    # 在训练集上的表现为：
    # t1 = time.time()
    plot_classifier(classifier_poly, train_X, train_y)
    # t2 = time.time()
    # print('t2-t1: ', t2-t1, 's')
    target_names = ['Hematite', 'martite']
    y_pred = classifier_poly.predict(train_X)
    # print(train_y)
    # print(y_pred)
    print(classification_report(train_y, y_pred, target_names=target_names))

    # # 第二种：使用径向基函数建立非线性分类器
    # classifier_rbf = SVC(kernel='rbf', probability=True)
    # classifier_rbf.fit(train_X, train_y)
    # # 在训练集上的表现为：
    # plot_classifier(classifier_rbf, train_X, train_y)
    # target_names = ['Hematite', 'martite']
    # y_pred = classifier_rbf.predict(train_X)
    # print(classification_report(train_y, y_pred, target_names=target_names))

    # # 使用训练好的SVM分类器classifier3对新样本进行预测，并给出置信度
    # for sample in new_samples:
    #     print('sample: {}, probs: {}'.format(sample, classifier3.predict_proba([sample])[0]))

def svm1(data_path):
    dataset = p.pca1(data_path)
    print(dataset)
    # prepare data for SVM
    train_X = dataset[:, 2:]
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
                mapx[namex].append(row[2])
                mapy[namey].append(row[3])
                break
    scatter = []
    markers = ['o', 'x', 'v', '.', '^', '<', '>', '1', '2', '3', '4', '8'
        , 's', 'p', '*', 'h', 'H', '+', ',', 'D', 'd', '|']
    colors=['b','r','g','k','m','w','c','y']
    for i in range(0, count):
        scatter.append(plt.scatter(mapx['x'+str(i)], mapy['y'+str(i)], c=colors[i], marker=markers[i]))
    plt.legend(handles=scatter, labels=target_names, loc="best")
    plt.savefig("./images/img6.png")
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
    # we don't need to training every time
    classifier_poly = SVC(kernel='rbf', gamma=0.2, decision_function_shape='ovo', C=1.5)
    clf = classifier_poly.fit(train_X, train_y)
    plot_classifier(clf, train_X, train_y)
    # save svm model
    from sklearn.externals import joblib
    joblib.dump(clf, '/Users/skye/PycharmProjects/20190302/model/svmtmp.pkl')

    # restore
    from sklearn.externals import joblib
    clf = joblib.load('/Users/skye/PycharmProjects/20190302/model/svmtmp.pkl')

    print('SVM在训练集上的准确率: ', clf.score(train_X, train_y))
    y_pred = clf.predict(train_X)
    print(train_y)
    print(y_pred)

    # plot confusion matrix
    # note: classes must be type of numpy.ndarray
    plot_confusion_matrix(train_y, y_pred, classes=np.array(target_names), title='Confusion matrix, without normalization')
    # plot_confusion_matrix(train_y, y_pred, classes=np.array(target_names), normalize=True, title='Normalized confusion matrix')

    # note: precision = '2' in y_pred/ '2' in train_y
    # but it have no influence on the total precision
    training_report = classification_report(train_y, y_pred, target_names=target_names)
    print(training_report)
    map = {}
    map['training_report'] = training_report
    map['accuracy'] = clf.score(train_X, train_y)
    return map

def prediction(data_path):
    dataset = p.pca1(data_path)
    print(dataset)
    samples = dataset[:, 0]
    train_X = dataset[:, 2:]
    # train_y = dataset[:, 1].astype('float').astype('int')
    from sklearn.externals import joblib
    clf = joblib.load('/Users/skye/PycharmProjects/20190302/model/svm4.pkl')
    y_pred = clf.predict(train_X)
    plot_classifier(clf, train_X, y_pred)
    print(y_pred)
    result = np.column_stack((samples, y_pred))
    # print(result)
    return result

# svm1('/Users/skye/PycharmProjects/20190302/data/光谱数据.xls')
# svm1('/Users/skye/PycharmProjects/20190302/data/光谱数据.csv')
prediction('/Users/skye/PycharmProjects/20190302/data/测试(预测)数据集.csv')