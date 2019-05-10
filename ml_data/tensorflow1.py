from sklearn.model_selection import train_test_split
import numpy as np
import helper
from ml_data.LDA import lda2
import numpy
import tensorflow as tf
import matplotlib.pyplot as plt

def tensorflow_ann(data_path):
    dataset = lda2(data_path)
    # print(dataset)
    dataset_X = dataset[:,[5,6]]
    y_tmp = dataset[:, 1].astype("int")
    category = []
    count = 0
    for i in y_tmp:
        if i not in category:
            count = count + 1
            category.append(i)
    dataset_y = []
    for i in y_tmp:
        tmp = []
        for j in range(0, count):
            tmp.append(0)
        tmp[i] = 1
        dataset_y.append(tmp)
    helper.tensor = count
    # print(dataset_X)
    # print(dataset_y)

    def add_layer(inputs, in_size, out_size, activation_function=None):
        Weights = tf.Variable(tf.random_normal([in_size, out_size]), dtype=tf.float32, name="weights")
        biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, dtype=tf.float32, name="biases")
        Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function == None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b, name="predict")
        return outputs

    xs = tf.placeholder(tf.float32, [None, 2], name="xs")
    ys = tf.placeholder(tf.float32, [None, count], name='ys')

    prediction = add_layer(xs, 2, count, activation_function=tf.nn.softmax)

    # loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction), reduction_indices=[1]))
    # cross_entropy = -tf.reduce_mean(ys * tf.log(tf.clip_by_value(prediction, 1e-10, 1.0)))
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

    saver = tf.train.Saver()
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    report = []
    for i in range(500):
        sess.run(train_step, feed_dict={xs: dataset_X, ys: dataset_y})
        if i % 50 == 0:
            v_xs = dataset_X
            v_ys = dataset_y
            y_pre = sess.run(prediction, feed_dict={xs: v_xs})
            correct_prediction = tf.equal(tf.argmax(y_pre, 1),
                                          tf.argmax(v_ys, 1))  # tf.argmax()最大值所在处的索引 0: 按列比 1：按行比 tf.equal()与矩阵维度一致
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
            result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
            print(result)
            report.append(result)

    saver.save(sess, './model/LDA+ANN/tensorflow_ann.ckpt')
    return report
    # pre = sess.run(prediction, feed_dict={xs: dataset_X})
    # for i in range(dataset_X.shape[0]):
    #     pre_label = numpy.argmax(pre[i])
    #     real_label = numpy.argmax(dataset_y[i])
    #     print("prediction is: %d, real is: %d"%(pre_label, real_label))


def tensorflow_predict(data_path):
    dataset = lda2(data_path)
    # print(dataset)
    dataset_X = dataset[:, [5, 6]]
    y_tmp = dataset[:, 1].astype("int")
    category = []
    count = 0
    for i in y_tmp:
        if i not in category:
            count = count + 1
            category.append(i)
    dataset_y = []
    for i in y_tmp:
        tmp = []
        for j in range(0, count):
            tmp.append(0)
        tmp[i] = 1
        dataset_y.append(tmp)
    helper.tensor = count

    # restore tensorflow model
    sess = tf.Session()
    saver = tf.train.import_meta_graph('../model/LDA+ANN/tensorflow_ann.ckpt.meta')
    saver.restore(sess, tf.train.latest_checkpoint('../model/LDA+ANN/'))
    graph = tf.get_default_graph()
    # w1 = graph.get_tensor_by_name("weights:0")
    # w2 = graph.get_tensor_by_name("biases:0")
    predict = graph.get_tensor_by_name("predict:0")
    xs = graph.get_tensor_by_name("xs:0")
    dataset_X = dataset_X.astype(np.float32)
    pre = sess.run(predict, feed_dict={xs: dataset_X})
    for i in range(dataset_X.shape[0]):
        pre_label = numpy.argmax(pre[i])
        real_label = numpy.argmax(dataset_y[i])
        print("prediction is: %d, real is: %d" % (pre_label, real_label))

# tensorflow_ann("/Users/skye/PycharmProjects/20190302/data/ml_dataset/训练数据集.csv")
tensorflow_predict("/Users/skye/PycharmProjects/20190302/data/ml_dataset/测试数据集.csv")