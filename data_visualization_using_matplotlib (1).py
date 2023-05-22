import pandas as pd
import numpy as np
import matplotlib
import streamlit as st 

# 1. Convert text file to csv

read_file = pd.read_csv(r'/content/dataset.txt', delimiter=' ')
read_file.to_csv(r'/content/dataset.csv', index=None)

dataset = pd.read_csv(r'/content/dataset.csv')

row_num = dataset.shape[0]
col_num = dataset.shape[1]

print('row_num = ', row_num)
print('col_num = ', col_num)

dataset.head(10)

for i in range(dataset.shape[1]):
    n_miss = dataset.iloc[:, i].isnull().sum()
    perc = n_miss / dataset.shape[0] * 100
    print('> %s, Missing: %d (%.3f%%)' % (dataset.columns[i], n_miss, perc))

dataset.dtypes

dataset['Date'].fillna(method='ffill', inplace=True)

dataset

dataset['Confirmed'].fillna(0, inplace=True)
dataset['Deaths'].fillna(0, inplace=True)

dataset

plt.bar(dataset['Deaths'],dataset['Confirmed'])
plt.show()