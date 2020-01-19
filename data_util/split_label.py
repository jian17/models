import numpy as np
import pandas as pd

np.random.seed(1)
full_labels = pd.read_csv('gesture_labels.csv')
full_labels.head()
grouped = full_labels.groupby('filename')
grouped.apply(lambda x: len(x)).value_counts()

gb = full_labels.groupby('filename')
grouped_list = [gb.get_group(x) for x in gb.groups]

total_size = len(grouped_list)
train_size = int(total_size * 0.9)
test_size = int(total_size * 0.1)
print(train_size, test_size)

train_index = np.random.choice(len(grouped_list), size=train_size, replace=False)
test_index = np.setdiff1d(list(range(total_size)), train_index)
print('Train index: {}\nTest index: {}'.format(train_index, test_index))

train = pd.concat([grouped_list[i] for i in train_index])
test = pd.concat([grouped_list[i] for i in test_index])

train.to_csv('train_labels.csv', index=None)
test.to_csv('test_labels.csv', index=None)