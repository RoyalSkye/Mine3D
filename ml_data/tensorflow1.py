from sklearn.model_selection import train_test_split
import pandas as pd
import ml_data.PCA as p
import numpy
import tensorflow as tf
import matplotlib
matplotlib.use('TkAgg')

data = p.pca("haha")
dataset_X = []
dataset_y = []
for key in data.keys():
    tmp = data.get(key)
    if tmp[2] == "赤铁矿":
        dataset_X.append([tmp[0], tmp[1]])
        dataset_y.append([1, 0])
    elif tmp[2] == "假象矿":
        dataset_X.append([tmp[0], tmp[1]])
        dataset_y.append([0, 1])
    else:
        pass
# X_train = numpy.array(dataset_X)
# y_train = numpy.array(dataset_y)
dataset_X = numpy.array(dataset_X)
dataset_y = numpy.array(dataset_y)
# numpy.savetxt("/Users/skye/Desktop/data1.txt", dataset_X)
X_train, X_test, y_train, y_test = train_test_split(
    dataset_X,dataset_y,test_size=0.4,random_state=42)

# data_path='/Users/skye/Desktop/data.csv'
# df=pd.read_csv(data_path,header=None)
# dataset_X,dataset_y=df.iloc[:,:-1],df.iloc[:,-1]
# dataset_X = dataset_X.values
# y = []
# for i in dataset_y.values:
#     if i == 0:
#         y.append([1, 0])
#     else:
#         y.append([0, 1])
# dataset_y = numpy.array(y)
# X_train, X_test, y_train, y_test = train_test_split(
#     dataset_X,dataset_y,test_size=0.25,random_state=42)

def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function == None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(v_ys,1))  # tf.argmax()最大值所在处的索引 0: 按列比 1：按行比 tf.equal()与矩阵维度一致
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result

xs = tf.placeholder(tf.float32, [None, 2])
ys = tf.placeholder(tf.float32, [None, 2])

l1 = add_layer(xs, 2, 4, activation_function=tf.nn.softmax)
prediction = add_layer(l1, 4, 2, activation_function=tf.nn.softmax)

# loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction), reduction_indices=[1]))
# cross_entropy = -tf.reduce_mean(ys * tf.log(tf.clip_by_value(prediction, 1e-10, 1.0)))
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(500):
    sess.run(train_step, feed_dict={xs: X_train, ys: y_train})
    if i % 50 == 0:
        print(compute_accuracy(X_test, y_test))
        # print(sess.run(cross_entropy, feed_dict={xs: X_test, ys: y_test}))
        # print("prediction ", sess.run(prediction, feed_dict={xs: X_test, ys: y_test}))
        # print("prediction"+sess.run(prediction, feed_dict={xs: X_train, ys: y_train}))
        # print(compute_accuracy(X_test, y_test)

pre = sess.run(prediction, feed_dict={xs: X_test})
for i in range(X_test.shape[0]):
    pre_label = numpy.argmax(pre[i])
    real_label = numpy.argmax(y_test[i])
    print("prediction is: %d, real is: %d"%(pre_label, real_label))
