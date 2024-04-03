import os

#b'/root/.keras/datasets/flower_photos/dandelion/5600240736_4a90c10579_n.jpg'

#dandelion

def get_flower_label(file_path):
  parts = tf.strings.split(file_path, os.sep)
  return parts[-2]

sample_path = b'/root/.keras/datasets/flower_photos/dandelion/5600240736_4a90c10579_n.jpg'

print(get_flower_label(sample_path).numpy()) # b'dandelion'
