from sklearn.model_selection import StratifiedKFold
import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
y = np.array([0, 0, 0, 1, 1, 1])

print(x)
print(y)
skf = StratifiedKFold(n_splits=3, shuffle=True)
for train_index, test_index in skf.split(x, y):
    print('Train:', train_index, 'Test:', test_index)
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_teat = y[train_index], y[test_index]
    # print(x_train)