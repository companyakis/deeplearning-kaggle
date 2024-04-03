import pathlib

flowers_root = tf.keras.utils.get_file(     
    'flower_photos',     
    'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz', 
    untar=True)

flowers_root = pathlib.Path(flowers_root)

#to_list

flowers_dataset = tf.data.Dataset.list_files(str(flowers_root/"*/*"))

print(len(flowers_dataset)) # 3670

#let's look at first four items

for file in flowers_dataset.take(4):
  print(file.numpy())

"""
b'/root/.keras/datasets/flower_photos/daisy/14907815010_bff495449f.jpg'
b'/root/.keras/datasets/flower_photos/dandelion/18204150090_fb418bbddb.jpg'
b'/root/.keras/datasets/flower_photos/roses/14982802401_a3dfb22afb.jpg'
b'/root/.keras/datasets/flower_photos/dandelion/5600240736_4a90c10579_n.jpg'

"""
