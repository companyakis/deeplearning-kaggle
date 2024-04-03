raw = [2 * i - 7 for i in range(10)]

#print(raw) # [-7, -5, -3, -1, 1, 3, 5, 7, 9, 11]

tf_dataset = tf.data.Dataset.from_tensor_slices(raw)

new_dataset = tf_dataset.filter(lambda i: i > 1).map(lambda i: i * 3).shuffle(4).batch(3)

for number in new_dataset:
  print(number.numpy())

"""
[15 33 21]
[ 9 27]

"""
