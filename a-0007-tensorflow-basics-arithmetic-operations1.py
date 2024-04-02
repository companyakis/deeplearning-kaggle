tensor = tf.constant([[1, 2, 3], [4, 5, 6]], dtype = tf.dtypes.float32)

print(tensor)

print("**********************")

print(tensor + 3)

print("**********************")

print(tensor - 2)

print("**********************")

print(tensor * 2.5)

print("**********************")

print(tensor / 2)

"""
tf.Tensor(
[[1. 2. 3.]
 [4. 5. 6.]], shape=(2, 3), dtype=float32)
**********************
tf.Tensor(
[[4. 5. 6.]
 [7. 8. 9.]], shape=(2, 3), dtype=float32)
**********************
tf.Tensor(
[[-1.  0.  1.]
 [ 2.  3.  4.]], shape=(2, 3), dtype=float32)
**********************
tf.Tensor(
[[ 2.5  5.   7.5]
 [10.  12.5 15. ]], shape=(2, 3), dtype=float32)
**********************
tf.Tensor(
[[0.5 1.  1.5]
 [2.  2.5 3. ]], shape=(2, 3), dtype=float32)

"""
