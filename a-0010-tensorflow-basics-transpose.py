tensor = tf.constant(np.arange(1, 21))

t = tf.reshape(tensor, shape = (5, 4))

transposed = tf.transpose(t)

print(transposed)

"""
tf.Tensor(
[[ 1  5  9 13 17]
 [ 2  6 10 14 18]
 [ 3  7 11 15 19]
 [ 4  8 12 16 20]], shape=(4, 5), dtype=int64)

"""
