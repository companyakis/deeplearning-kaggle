tensor = tf.constant([[1, 2, 3], [4, 5, 6]], dtype = tf.dtypes.float32)

print(tensor)

print("**********************")

print(tf.add(tensor, 2))

print("**********************")

print(tf.multiply(tensor, 2))

"""
tf.Tensor(
[[1. 2. 3.]
 [4. 5. 6.]], shape=(2, 3), dtype=float32)
**********************
tf.Tensor(
[[3. 4. 5.]
 [6. 7. 8.]], shape=(2, 3), dtype=float32)
**********************
tf.Tensor(
[[ 2.  4.  6.]
 [ 8. 10. 12.]], shape=(2, 3), dtype=float32)

"""
