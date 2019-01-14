import tensorflow as tf
import os


def csvread(filelist):
    """
    读取CSV文件
    :param filelist:文件路径+名字列表
    :return:读取的内容
    """
    # 1.构造文件队列
    file_queue = tf.train.string_input_producer(filelist)

    # 2.构造CSV阅读器读取队列数据（按一行）
    reader = tf.TextLineReader()
    key, value = reader.read(file_queue)

    # 3.对每行内容进行解码
    # record_defaults：制定每一个样本的每一列的类型，指定默认值
    records = [['None'], ['None']]
    example, label = tf.decode_csv(value, record_defaults=records)

    # 4. 想要读取多个数据就行进行批处理
    example_batch, label_batch = tf.train.batch([example, label], batch_size=5, num_threads=1, capacity=9)
    return example_batch, label_batch


if __name__ == "__main__":
    # 找到文件，放入列表   路径
    file_name = os.listdir("./csvdata/")
    filelist = [os.path.join('./csvdata/', file) for file in file_name]
    example, label = csvread(filelist)
    # 开启会话
    with tf.Session() as sess:
        # 定义一个线程的协调器
        coord = tf.train.Coordinator()

        # 开启读取文件的线程
        thread = tf.train.start_queue_runners(sess, coord=coord)

        print(sess.run([example, label]))

        # 回收子线程
        coord.request_stop()
        coord.join(thread)
