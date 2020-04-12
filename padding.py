import keras
import numpy as np

X = np.load("dataX.npy",allow_pickle=True)
print(len(X))
X = X[:-1]
print(len(X))
print(type(X))
print("Srishti Loves Maggie")
X2 = keras.preprocessing.sequence.pad_sequences(X, maxlen=100, dtype='float32', padding='post', truncating='post')
print("saving")
np.save("dataY.npy",Y)
