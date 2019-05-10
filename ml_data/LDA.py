import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.metrics import classification_report

# LDA+SVM
def lda1(data_path):
    import pandas as pd
    df = pd.read_csv(data_path, header=None)
    # print(df)
    rowNum = df.shape[0]  # 不包括表头
    colNum = df.columns.size
    dataset = df.values
    y = dataset[1][1:].astype('int')  # category
    tmp = dataset[0:5][:, 1:].transpose()
    samples = dataset[0]
    samples = samples[1:]
    samples = samples.tolist()
    waves = ['wavelength ' + str(i) for i in dataset[:, 0][5:].tolist()]
    data = pd.DataFrame(columns=[*samples], index=waves)
    i = 5
    for wave in data.index:
        data.loc[wave, dataset[0][1]:dataset[0][-1]] = np.mat(dataset[i][1:])
        i = i + 1
    X = data.values.astype('float').transpose()
    y = dataset[1][1:].astype('int')
    # print(X)
    # print(y)
    target_names = ["Hematite", "magnetite", "martite"]
    category = []
    count = 0
    for i in y:
        if i not in category:
            count = count + 1
            category.append(i)
    print(category)
    if count != 3:
        target_names = []
        for i in category:
            target_names.append('type' + str(i))
    colors = ['r', 'g', 'b', 'k', 'm', 'w', 'c', 'y']
    markers = ['x', '*', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8'
        , 's', 'p', ',', 'h', 'H', '+', '.', 'D', 'd', '|']
    lda = LDA(n_components=2)
    X_r =lda.fit(X,y).transform(X)
    ax = plt.figure()
    for c, i, m, target_name in zip(colors[:count], category, markers, target_names):
        plt.scatter(X_r[y == i, 0], X_r[y == i, 1], c=c, marker=m, label=target_name)
    plt.xlabel('Dimension1')
    plt.ylabel('Dimension2')
    plt.title("LDA")
    plt.legend()
    plt.savefig("./images/LDA+SVM/img1.png")
    plt.show()

    classifier_poly = svm.SVC(kernel='rbf', gamma=0.2, decision_function_shape='ovo', C=1.5)
    clf = classifier_poly.fit(X_r, y)
    from ml_data.SVM import plot_classifier
    plot_classifier(clf, X_r, y, './images/LDA+SVM/img2.png')
    # save svm model
    from sklearn.externals import joblib
    joblib.dump(clf, './model/LDA+SVM/svm.pkl')
    # restore
    from sklearn.externals import joblib
    clf = joblib.load('./model/LDA+SVM/svm.pkl')

    print('SVM在训练集上的准确率: ', clf.score(X_r, y))
    y_pred = clf.predict(X_r)
    print(y)
    print(y_pred)

    from ml_data.SVM import plot_confusion_matrix
    plot_confusion_matrix(y, y_pred, classes=np.array(target_names), path='./images/LDA+SVM/img3.png',
                          title='Confusion matrix, without normalization')
    plot_confusion_matrix(y, y_pred, classes=np.array(target_names), normalize=True, path='./images/LDA+SVM/img4.png',
                          title='Normalized confusion matrix')
    training_report = classification_report(y, y_pred, target_names=target_names)
    print(training_report)
    dataset = np.column_stack((tmp, X_r[:, [0, 1]]))
    map = {}
    map['training_report'] = training_report
    map['accuracy'] = clf.score(X_r, y)
    map['result'] = dataset
    return map

# LDA+ANN
def lda2(data_path):
    import pandas as pd
    df = pd.read_csv(data_path, header=None)
    # print(df)
    rowNum = df.shape[0]  # 不包括表头
    colNum = df.columns.size
    dataset = df.values
    y = dataset[1][1:].astype('int')  # category
    tmp = dataset[0:5][:, 1:].transpose()
    samples = dataset[0]
    samples = samples[1:]
    samples = samples.tolist()
    waves = ['wavelength ' + str(i) for i in dataset[:, 0][5:].tolist()]
    data = pd.DataFrame(columns=[*samples], index=waves)
    i = 5
    for wave in data.index:
        data.loc[wave, dataset[0][1]:dataset[0][-1]] = np.mat(dataset[i][1:])
        i = i + 1
    X = data.values.astype('float').transpose()
    y = dataset[1][1:].astype('int')
    # print(X)
    # print(y)
    target_names = ["Hematite", "magnetite", "martite"]
    category = []
    count = 0
    for i in y:
        if i not in category:
            count = count + 1
            category.append(i)
    print(category)
    if count != 3:
        target_names = []
        for i in category:
            target_names.append('type' + str(i))
    colors = ['r', 'g', 'b', 'k', 'm', 'w', 'c', 'y']
    markers = ['x', '*', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8'
        , 's', 'p', ',', 'h', 'H', '+', '.', 'D', 'd', '|']
    lda = LDA(n_components=2)
    X_r = lda.fit(X, y).transform(X)
    ax = plt.figure()
    for c, i, m, target_name in zip(colors[:count], category, markers, target_names):
        plt.scatter(X_r[y == i, 0], X_r[y == i, 1], c=c, marker=m, label=target_name)
    plt.xlabel('Dimension1')
    plt.ylabel('Dimension2')
    plt.title("LDA")
    plt.legend()
    # plt.savefig("./images/LDA+ANN/img1.png")
    plt.show()
    dataset = np.column_stack((tmp, X_r[:, [0, 1]]))
    return dataset