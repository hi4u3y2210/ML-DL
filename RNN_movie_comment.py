import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import imdb

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)
print('訓練總筆數:', len(x_train))
print('測試總筆數:', len(x_test))