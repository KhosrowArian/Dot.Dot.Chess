import sqlite3
import random
from difflib import SequenceMatcher
import unicodedata
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from  sklearn import tree

conn = sqlite3.connect('../data-cleaning/data.db')
c = conn.cursor()

dfgames = pd.read_sql_query("select * from games_new;", conn)

np_array = np.array([dfgames['white_age'], dfgames['black_age'], dfgames['black_time_since_gm'], dfgames['white_time_since_gm'], dfgames['black_gm_age'], dfgames['white_gm_age']])

print(np.shape(np_array))

## DECISION TREE
X = np_array.T
# X = ([dfgames['white_age'], dfgames['black_age'], dfgames['black_time_since_gm'], dfgames['white_time_since_gm'], dfgames['black_gm_age'], dfgames['white_gm_age']]).T
y = dfgames['result']


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)

tree.plot_tree(clf)


## SVM

# def make_meshgrid(x, y, h=.02):
#     """Create a mesh of points to plot in

#     Parameters
#     ----------
#     x: data to base x-axis meshgrid on
#     y: data to base y-axis meshgrid on
#     h: stepsize for meshgrid, optional

#     Returns
#     -------
#     xx, yy : ndarray
#     """
#     x_min, x_max = x.min() - 1, x.max() + 1
#     y_min, y_max = y.min() - 1, y.max() + 1
#     xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
#                          np.arange(y_min, y_max, h))
#     return xx, yy


# def plot_contours(ax, clf, xx, yy, **params):
#     """Plot the decision boundaries for a classifier.

#     Parameters
#     ----------
#     ax: matplotlib axes object
#     clf: a classifier
#     xx: meshgrid ndarray
#     yy: meshgrid ndarray
#     params: dictionary of params to pass to contourf, optional
#     """
#     Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
#     Z = Z.reshape(xx.shape)
#     out = ax.contourf(xx, yy, Z, **params)
#     return out

# X = [dfgames['white_age'], dfgames['black_age'], dfgames['black_time_since_gm'], dfgames['white_time_since_gm'], dfgames['black_gm_age'], dfgames['white_gm_age']]
# # X = dfgames['white_age']
# y = dfgames['result']

# # X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# # we create an instance of SVM and fit out data. We do not scale our
# # data since we want to plot the support vectors
# C = 1.0  # SVM regularization parameter
# models = (svm.SVC(kernel='linear', C=C),
#           svm.LinearSVC(C=C, max_iter=10000),
#           svm.SVC(kernel='rbf', gamma=0.7, C=C),
#           svm.SVC(kernel='poly', degree=3, gamma='auto', C=C))
# models = (clf.fit(X, y) for clf in models)

# # title for the plots
# titles = ('SVC with linear kernel',
#           'LinearSVC (linear kernel)',
#           'SVC with RBF kernel',
#           'SVC with polynomial (degree 3) kernel')

# # Set-up 2x2 grid for plotting.
# fig, sub = plt.subplots(2, 2)
# plt.subplots_adjust(wspace=0.4, hspace=0.4)

# # X0, X1 = X[:, 0], X[:, 1]
# # xx, yy = make_meshgrid(X0, X1)

# # for clf, title, ax in zip(models, titles, sub.flatten()):
# #     plot_contours(ax, clf, xx, yy,
# #                   cmap=plt.cm.coolwarm, alpha=0.8)
# #     ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
# #     ax.set_xlim(xx.min(), xx.max())
# #     ax.set_ylim(yy.min(), yy.max())
# #     ax.set_xlabel('Sepal length')
# #     ax.set_ylabel('Sepal width')
# #     ax.set_xticks(())
# #     ax.set_yticks(())
# #     ax.set_title(title)

# plt.show()

