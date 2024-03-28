import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator

source = r"C:\Users\musta\OneDrive\Resimler\tf\formula1"

train_data_gen = ImageDataGenerator(rescale = 1.0/255, validation_split = 0.1)

test_data_gen = ImageDataGenerator(rescale = 1.0/255, validation_split = 0.1)

train_data_gen = train_data_gen.flow_from_directory(source, target_size = (500, 500), subset = "training", batch_size = 2)

test_data_gen = test_data_gen.flow_from_directory(source, target_size = (500, 500), subset = "validation", batch_size = 2)
