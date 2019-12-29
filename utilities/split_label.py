import numpy as np
import pandas as pd

np.random.seed(1)
full_labels = pd.read_csv('hand_labels.csv')
full_labels.head()
grouped = full_labels.groupby('filename')
grouped.apply(lambda x: len(x)).value_counts()

gb = full_labels.groupby('filename')
grouped_list = [gb.get_group(x) for x in gb.groups]

train_index = np.random.choice(len(grouped_list), size=6, replace=False)
test_index = np.setdiff1d(list(range(10)), train_index)
# take first 200 files
train = pd.concat([grouped_list[i] for i in train_index])
test = pd.concat([grouped_list[i] for i in test_index])

train.to_csv('train_labels.csv', index=None)
test.to_csv('test_labels.csv', index=None)