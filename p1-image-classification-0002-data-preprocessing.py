# split data (train and test data)

(X_train_all, y_train_all), (X_test, y_test) = fashion_mnist_data

# print(X_train_all.shape) #(60000, 28, 28)
# print(y_train_all.shape) #(60000,)
# print(X_test.shape) #(10000, 28, 28)
# print(y_test.shape) #(10000,)

# Train, validation and test data

# 55000 train and 5000 validation data

X_train = X_train_all[:55000]
y_train = y_train_all[:55000]
X_validation = X_train_all[-5000:]
y_validation = y_train_all[-5000:]

#look data
# print(X_train[0])
# print(X_train.dtype) #uint8

#scale data
X_train, X_validation, X_test = X_train/255.0, X_validation/255.0, X_test/255.0

#look at data again
#print(X_train[0])
#print(X_train.dtype) #float64

#what about y?
#print(y_train[0]) #9

#how many classes?
print(np.unique(y_train)) #[0 1 2 3 4 5 6 7 8 9]

#we should give class names
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal",  "Shirt", "Sneaker", "Bag", "Ankle boot"]

#remember y_train[0] is equal to 9

print(class_names[y_train[0]]) #now not 9, Ankle boot
