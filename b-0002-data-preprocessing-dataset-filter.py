raw = [2 * i - 7 for i in range(10)]

print(raw) # [-7, -5, -3, -1, 1, 3, 5, 7, 9, 11]

tf_dataset = tf.data.Dataset.from_tensor_slices(raw)

for item in tf_dataset.filter(lambda n: n > 1):
  print("item: ", item.numpy())

"""
item:  3
item:  5
item:  7
item:  9
item:  11
"""
