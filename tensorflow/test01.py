import tensorflow as tf 

a = tf.constant(10.1)
b = tf.constant(11.2)

sum01 = tf.add(a,b)

with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    print(sess.run(sum01))