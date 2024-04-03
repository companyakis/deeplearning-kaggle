##b'/root/.keras/datasets/flower_photos/dandelion/5600240736_4a90c10579_n.jpg'

def process_flower_image(file_path):
  flower_label = get_flower_label(file_path)
  image = tf.io.read_file(file_path)
  image = tf.image.decode_jpeg(image)
  image = tf.image.resize(image, [64, 64]) #64*64 is my selection now!
  image = image / 255 #between 0 and 1
  return image, flower_label

sample_path = b'/root/.keras/datasets/flower_photos/dandelion/5600240736_4a90c10579_n.jpg'

img, label = process_flower_image(sample_path)

print(img.shape) # (64, 64, 3)

print(label.numpy()) # b'dandelion'
