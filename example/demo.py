# coding=utf-8
"""
@author: 章云
"""
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train = pd.read_csv('../data/train.csv')

sns.distplot(train['Age'].dropna())
plt.show()
