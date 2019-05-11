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
    target_names = ["Hematite", "magnetite", "martite"]
    category = []
    count = 0
    for i in y_tmp:
        if i not in category:
            count = count + 1
            category.append(i)
    if count != 3:
        target_names = []
        for i in category:
            target_names.append('type' + str(i))
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
        with tf.name_scope("layer"):
            with tf.name_scope("weights"):
                Weights = tf.Variable(tf.random_normal([in_size, out_size]), dtype=tf.float32, name="w")
                tf.summary.histogram('layer/weights', Weights)
            with tf.name_scope("biases"):
                biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, dtype=tf.float32, name="b")
                tf.summary.histogram('layer/biases', biases)
            with tf.name_scope("Wx_plus_b"):
                Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
            if activation_function == None:
                outputs = Wx_plus_b
            else:
                outputs = activation_function(Wx_plus_b, name="predict")
            tf.summary.histogram('layer/outputs', outputs)
            return outputs

    with tf.name_scope("inputs"):
        xs = tf.placeholder(tf.float32, [None, 2], name="xs")
        ys = tf.placeholder(tf.float32, [None, count], name='ys')

    prediction = add_layer(xs, 2, count, activation_function=tf.nn.softmax)

    # loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction), reduction_indices=[1]))
    # cross_entropy = -tf.reduce_mean(ys * tf.log(tf.clip_by_value(prediction, 1e-10, 1.0)))
    with tf.name_scope("loss"):
        cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction), reduction_indices=[1]))
        tf.summary.scalar('loss', cross_entropy)
    with tf.name_scope("train"):
        train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

    saver = tf.train.Saver()
    sess = tf.Session()
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("./model/LDA+ANN/logs", sess.graph)
    sess.run(tf.global_variables_initializer())

    report = ''
    for i in range(501):
        sess.run(train_step, feed_dict={xs: dataset_X, ys: dataset_y})
        if i % 50 == 0:
            result = sess.run(merged,
                              feed_dict={xs: dataset_X, ys: dataset_y})
            writer.add_summary(result, i)
            v_xs = dataset_X
            v_ys = dataset_y
            y_pre = sess.run(prediction, feed_dict={xs: v_xs})
            correct_prediction = tf.equal(tf.argmax(y_pre, 1),
                                          tf.argmax(v_ys, 1))  # tf.argmax()最大值所在处的索引 0: 按列比 1：按行比 tf.equal()与矩阵维度一致
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
            result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
            print(result)
            report = report + "training_step: " + str(i)+", accuracy: " + str(result) + '\n'

    saver.save(sess, './model/LDA+ANN/tensorflow_ann.ckpt')

    # final accuracy
    v_xs = dataset_X
    v_ys = dataset_y
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1),
                                  tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    from ml_data.SVM import plot_confusion_matrix
    pre_label = []
    for i in range(dataset_X.shape[0]):
        pre_label.append(numpy.argmax(y_pre[i]))
    pre_label = numpy.array(pre_label)
    plot_confusion_matrix(y_tmp, pre_label, classes=np.array(target_names), path='./images/LDA+ANN/img4.png',
                          title='Confusion matrix, without normalization')
    map = {}
    map['accuracy'] = result
    map['training_report'] = report
    # print(map)
    return map

def tensorflow_predict(data_path):
    dataset = lda2(data_path, True)
    # print(dataset
    dataset_X = dataset[:, [5, 6]]
    samples = dataset[:, [0, 2, 3, 4]]
    # print(samples)
    y_tmp = dataset[:, 1].astype("int")
    target_names = ["Hematite", "magnetite", "martite"]
    category = []
    count = 0
    for i in y_tmp:
        if i not in category:
            count = count + 1
            category.append(i)
    dataset_y = []
    if count != 3:
        target_names = []
        for i in category:
            target_names.append('type' + str(i))
    for i in y_tmp:
        tmp = []
        for j in range(0, count):
            tmp.append(0)
        tmp[i] = 1
        dataset_y.append(tmp)
    helper.tensor = count

    # restore tensorflow model
    sess = tf.Session()
    saver = tf.train.import_meta_graph('./model/LDA+ANN/tensorflow_ann.ckpt.meta')
    saver.restore(sess, tf.train.latest_checkpoint('./model/LDA+ANN/'))
    graph = tf.get_default_graph()
    # for op in graph.get_operations():
    #     print(op.name)
    predict = graph.get_tensor_by_name("layer/predict:0")
    xs = graph.get_tensor_by_name("inputs/xs:0")
    ys = graph.get_tensor_by_name("inputs/ys:0")
    dataset_X = dataset_X.astype(np.float32)
    pre = sess.run(predict, feed_dict={xs: dataset_X})
    y_pred = []
    for i in range(dataset_X.shape[0]):
        pre_label = numpy.argmax(pre[i])
        real_label = numpy.argmax(dataset_y[i])
        y_pred.append(pre_label)
        print("prediction is: %d, real is: %d" % (pre_label, real_label))
    y_pred = np.array(y_pred)
    result = np.column_stack((samples, y_pred))
    v_xs = dataset_X
    v_ys = dataset_y
    correct_prediction = tf.equal(tf.argmax(pre, 1),
                                  tf.argmax(v_ys, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result1 = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    from ml_data.SVM import plot_confusion_matrix
    plot_confusion_matrix(y_tmp, y_pred, classes=np.array(target_names), path='./images/prediction/img2.png',
                          title='Confusion matrix, without normalization')
    map = {}
    map["result"] = result
    map["accuracy"] = result1
    # print(map)
    return map

# tensorflow_ann("/Users/skye/PycharmProjects/20190302/data/ml_dataset/训练数据集.csv")
# tensorflow_predict("/Users/skye/PycharmProjects/20190302/data/ml_dataset/测试数据集.csv")