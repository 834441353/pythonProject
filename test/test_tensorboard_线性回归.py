import tensorflow as tf
import os


def myregression():
    """
    模拟线性回归
    :return:
    """
    # 自实现线性回归预测
    with tf.variable_scope("data"):
        # 1.准备数据，  X  特征值跑[100,1]   Y  目标值[100]
        x = tf.random_normal([100, 1], mean=1.75, stddev=0.5, name="x_data")

        # 矩阵相乘必须是二维的
        y_true = tf.matmul(x, [[0.7]]) + 0.8
    with tf.variable_scope("model"):
        # 2.建立线性回归模型 1个特征，1个权重，1个偏置 y=xw+b
        weight = tf.Variable(
            tf.random_normal([1, 1], mean=0.0, stddev=1.0), name="w")
        bias = tf.Variable(0.0, name="b")

        y_predict = tf.matmul(x, weight) + bias

    with tf.variable_scope("loss"):
        # 3.建立损失函数，均方误差
        loss = tf.reduce_mean(tf.square(y_true - y_predict))

    with tf.variable_scope("optimizer"):
        # 4.梯度下降优化损失  learning_rate:0~1,2,3,5,7,10
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

        # 1.收集tensor
        tf.summary.scalar("losses", loss)
        tf.summary.histogram("weights", weight)
        # 2.合并变量
        merged = tf.summary.merge_all()

        # 定义一个初始化变量的op
        init_op = tf.global_variables_initializer()

        # 定义一个保存模型的实例
        saver = tf.train.Saver()
    # 通过绘画运行程序
    with tf.Session() as sess:
        sess.run(init_op)
        print("随机初始化的权重为： %f，偏置为： %f" % (weight.eval(), bias.eval()))
        filewrite = tf.summary.FileWriter("./tmp/summary/test/", graph=sess.graph)

        # 加载模型，覆盖模型中随机定义的参数,从上次训练的参数结果开始
        if os.path.exists("./tmp/ckpt/checkpoint"):
            saver.restore(sess, "./tmp/ckpt/model")

        for i in range(400):
            sess.run(train_op)
            summary = sess.run(merged)
            filewrite.add_summary(summary, i)
            print("第%d次参数权重为： %f，偏置为： %f" % (i, weight.eval(), bias.eval()))
        saver.save(sess, "./tmp/ckpt/model")
    return None


if __name__ == "__main__":
    myregression()
