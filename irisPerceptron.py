{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import datasets\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "iris=datasets.load_iris()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "X=iris.data[:,[2,3]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "y=iris.target"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\VarunTarun\\Downloads\\anaconda678679\\lib\\site-packages\\sklearn\\cross_validation.py:41: DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved. Also note that the interface of the new CV iterators are different from that of this module. This module will be removed in 0.20.\n",
      "  \"This module will be removed in 0.20.\", DeprecationWarning)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.cross_validation import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "sc=StandardScaler()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "StandardScaler(copy=True, with_mean=True, with_std=True)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sc.fit(X_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train_std=sc.transform(X_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_test_std=sc.transform(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import Perceptron"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "ppn=Perceptron(n_iter=40,eta0=0.1,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\VarunTarun\\Downloads\\anaconda678679\\lib\\site-packages\\sklearn\\linear_model\\stochastic_gradient.py:117: DeprecationWarning: n_iter parameter is deprecated in 0.19 and will be removed in 0.21. Use max_iter and tol instead.\n",
      "  DeprecationWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "Perceptron(alpha=0.0001, class_weight=None, eta0=0.1, fit_intercept=True,\n",
       "      max_iter=None, n_iter=40, n_jobs=1, penalty=None, random_state=0,\n",
       "      shuffle=True, tol=None, verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ppn.fit(X_train_std,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred=ppn.predict(X_test_std)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "print((y_test !=y_pred).sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib.colors import ListedColormap"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9111111111111111\n"
     ]
    }
   ],
   "source": [
    "print(accuracy_score(y_test,y_pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot_decision_regions(X, y, classifier,test_idx=None, resolution=0.02):\n",
    "      markers = ('s', 'x', 'o', '^', 'v')  \n",
    "      colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')    \n",
    "      cmap = ListedColormap(colors[:len(np.unique(y))])    # plot the decision surface \n",
    "      x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1    \n",
    "      x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1    \n",
    "      xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))   \n",
    "      Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)    \n",
    "      Z = Z.reshape(xx1.shape)   \n",
    "      plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)   \n",
    "      plt.xlim(xx1.min(), xx1.max())   \n",
    "      plt.ylim(xx2.min(), xx2.max())   # plot all samples  \n",
    "      X_test, y_test = X[test_idx, :], y[test_idx]                                  \n",
    "      for idx, cl in enumerate(np.unique(y)):     \n",
    "            plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, c=cmap(idx),marker=markers[idx], label=cl)        \n",
    "            # highlight test samples   \n",
    "            if test_idx:       \n",
    "                X_test, y_test = X[test_idx, :], y[test_idx]          \n",
    "                plt.scatter(X_test[:, 0], X_test[:, 1], c='', alpha=1.0, linewidth=1, marker='o', s=55, label='test set')\n",
    "             \n",
    "             "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "X_combined_std = np.vstack((X_train_std, X_test_std)) \n",
    "y_combined = np.hstack((y_train, y_test)) \n",
    "plot_decision_regions(X=X_combined_std, y=y_combined,classifier=ppn, test_idx=range(105,150))\n",
    "plt.xlabel('petal length [standardized]') \n",
    "plt.ylabel('petal width [standardized]') \n",
    "plt.legend(loc='upper left') \n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
