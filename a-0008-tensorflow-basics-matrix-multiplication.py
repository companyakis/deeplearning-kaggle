m1 = tf.constant([[1, 2, 3], [4, 5, 6]],)

m2 = tf.constant([[7, 8], [10, 11], [12, 13]])

print(tf.matmul(m1, m2))

print("*******************")

print(m1 @ m2)

"""
tf.Tensor(
[[ 63  69]
 [150 165]], shape=(2, 2), dtype=int32)
*******************
tf.Tensor(
[[ 63  69]
 [150 165]], shape=(2, 2), dtype=int32)
"""
