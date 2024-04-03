length_flowers_dataset = len(flowers_dataset)

print(length_flowers_dataset) # 3670

train_size = int(length_flowers_dataset * 0.85)

train_flowers_dataset = flowers_dataset.take(train_size)

print(len(train_flowers_dataset))

test_flowers_dataset = flowers_dataset.skip(train_size)

print(len(test_flowers_dataset))

print(3119 + 551) # 3670
