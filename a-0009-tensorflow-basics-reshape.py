tensor = tf.constant(np.arange(1, 21))

t1 = tf.reshape(tensor, shape = (5, 4))

print(t1)

"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]
 [17 18 19 20]], shape=(5, 4), dtype=int64)
"""
