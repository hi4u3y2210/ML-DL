import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
(x_train, y_train),( x_test, y_test) = mnist.load_data()
plt.imshow(x_train[0],cmap='Greys')