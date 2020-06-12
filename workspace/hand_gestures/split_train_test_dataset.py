import os
import numpy as np
import pandas as pd

script_path = os.path.dirname(os.path.realpath(__file__))
all_labels_path = os.path.join(script_path, "annotations/gesture_labels.csv")
train_labels_path = os.path.join(script_path, "annotations/train_labels.csv")
test_labels_path = os.path.join(script_path, "annotations/test_labels.csv")

np.random.seed(1)
full_labels = pd.read_csv(all_labels_path)
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

train.to_csv(train_labels_path, index=None)
test.to_csv(test_labels_path, index=None)