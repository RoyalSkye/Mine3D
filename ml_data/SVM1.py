import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

def visual_2D_dataset(dataset_X, dataset_y):
    '''将二维数据集dataset_X和对应的类别dataset_y显示在散点图中'''
    assert dataset_X.shape[1] == 2, 'only support dataset with 2 features'
    plt.figure()
    classes = list(set(dataset_y))
    markers = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8'
        , 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|']
    colors = ['b', 'c', 'g', 'k', 'm', 'w', 'r', 'y']
    for class_id in classes:
        one_class = np.array([feature for (feature, label) in
                              zip(dataset_X, dataset_y) if label == class_id])
        plt.scatter(one_class[:, 0], one_class[:, 1], marker=np.random.choice(markers, 1)[0],
                    c=np.random.choice(colors, 1)[0], label='class_' + str(class_id))
    plt.legend()
    plt.show()

# 将分类器绘制到图中
def plot_classifier(classifier, X, y):
    x_min, x_max = min(X[:, 0]) - 1.0, max(X[:, 0]) + 1.0  # 计算图中坐标的范围
    y_min, y_max = min(X[:, 1]) - 1.0, max(X[:, 1]) + 1.0
    step_size = 0.01 # 设置step size
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
    plt.xticks((np.arange(int(min(X[:, 0])), int(max(X[:, 0])), 1.0)))
    plt.yticks((np.arange(int(min(X[:, 1])), int(max(X[:, 1])), 1.0)))

    plt.show()

data_path='/Users/skye/Desktop/data.csv'
df=pd.read_csv(data_path,header=None)
# print(df.head())
# print(df.info())
dataset_X,dataset_y=df.iloc[:,:-1],df.iloc[:,-1]
dataset_X=dataset_X.values
dataset_y=dataset_y.values
visual_2D_dataset(dataset_X,dataset_y)
train_X, test_X, train_y, test_y=train_test_split(
    dataset_X,dataset_y,test_size=0.25,random_state=42)

# # 构建线性分类器
# classifier=SVC(kernel='linear')
# classifier.fit(train_X,train_y)
# # 模型在训练集上的性能报告：
# plot_classifier(classifier,train_X,train_y)  # 分类器在训练集上的分类效果
# target_names = ['Class-0', 'Class-1']
# y_pred=classifier.predict(train_X)
# print(classification_report(train_y, y_pred, target_names=target_names))
# # 分类器在测试集上的分类效果
# plot_classifier(classifier,test_X,test_y)
# target_names = ['Class-0', 'Class-1']
# y_pred=classifier.predict(test_X)
# print(classification_report(test_y, y_pred, target_names=target_names))

# 使用SVM建立非线性分类器主要是使用不同的核函数
# 第一种：使用多项式核函数：
classifier_poly=SVC(kernel='poly',degree=3) # 三次多项式方程
classifier_poly.fit(train_X,train_y)
# 在训练集上的表现为：
plot_classifier(classifier_poly,train_X,train_y)
target_names = ['Class-0', 'Class-1']
y_pred=classifier_poly.predict(train_X)
print(classification_report(train_y, y_pred, target_names=target_names))

# 第二种：使用径向基函数建立非线性分类器
classifier_rbf=SVC(kernel='rbf')
classifier_rbf.fit(train_X,train_y)
# 在训练集上的表现为：
plot_classifier(classifier_rbf,train_X,train_y)
target_names = ['Class-0', 'Class-1']
y_pred=classifier_rbf.predict(train_X)
print(classification_report(train_y, y_pred, target_names=target_names))

