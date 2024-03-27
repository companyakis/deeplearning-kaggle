#model-training1.py

#training and fit method

#30 epochs

model_training = model.fit(X_train, y_train, epochs = 30, validation_data = (X_validation, y_validation))
