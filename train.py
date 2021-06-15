from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
import json
import os
import numpy as np
import csv
import dvc.api
import pandas as pd

with dvc.api.open(
    'data_folder/iris.csv',
    repo='https://github.com/healiosuk/ML-project-template.git',
    rev='master'
) as fd:
    data = pd.read_csv(fd)
    # fd is a file descriptor which can be processed normally

print(len(data))

# Read in data
# test
X_train = np.genfromtxt("data/train_features.csv")
y_train = np.genfromtxt("data/train_labels.csv")
X_test = np.genfromtxt("data/test_features.csv")
y_test = np.genfromtxt("data/test_labels.csv")


# Fit a model
depth = 5
clf = RandomForestClassifier(max_depth=depth)
clf.fit(X_train,y_train)

acc = clf.score(X_test, y_test)
print(acc)
with open("metrics.txt", 'w') as outfile:
        outfile.write("Accuracy: " + str(acc) + "\n")


# Plot it
disp = plot_confusion_matrix(clf, X_test, y_test, normalize='true',cmap=plt.cm.Blues)
plt.savefig('confusion_matrix.png')

