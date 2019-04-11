import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression

file_path = "5-1_data.csv"
data = pd.read_csv(file_path, encoding = "utf8", delimiter = "\t")
                                       
# print(data[:216])