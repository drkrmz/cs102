{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import confusion_matrix, accuracy_score, roc_curve, precision_score, recall_score, f1_score, auc\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from math import sqrt\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class LogisticRegression:\n",
    "    \n",
    "    def __init__(self, alpha=0.01, precision=0.001):\n",
    "        self.alpha = alpha\n",
    "        self.precision = precision\n",
    "        \n",
    "    def fit(self, X, y):\n",
    "        self.beta = []\n",
    "        X = X.values\n",
    "        y = y.values\n",
    "        self.cost = 0\n",
    "        old_cost = 1\n",
    "        n_values = len(X[0])\n",
    "        for i in range(n_values + 1):\n",
    "            self.beta.append(0)\n",
    "        while (old_cost - self.cost) > self.precision: \n",
    "            error = 0\n",
    "            old_cost = self.cost\n",
    "            for i in range(len(X)):\n",
    "                e = self.beta[0]\n",
    "                d_cost = 0\n",
    "                for j in range(n_values):\n",
    "                    e += self.beta[j + 1] * X[i][j]\n",
    "                y_pred = 1.0 / (1.0 + np.exp(-e))\n",
    "                error += y_pred - y[i]\n",
    "                self.cost += -y[i] * np.log(y_pred) - (1 - y[i]) * np.log(1 - y_pred)\n",
    "                self.beta[0] -= self.alpha * error\n",
    "                for j in range(n_values):\n",
    "                    self.beta[j + 1] -= self.alpha * error * X[i][j]\n",
    "        return self.beta\n",
    "    \n",
    "    def predict(self, X):\n",
    "        X = X.values\n",
    "        self.y_predict = []\n",
    "        self.prob = []\n",
    "        for i in range(len(X)):\n",
    "            e = self.beta[0]\n",
    "            for j in range(len(X[i])):\n",
    "                e += self.beta[j + 1] * X[i][j]\n",
    "            self.prob.append(1 / (1 + np.exp(-e)))\n",
    "            if self.prob[i] >= 0.35:\n",
    "                self.y_predict.append(1)\n",
    "            else:\n",
    "                self.y_predict.append(0)\n",
    "        return self.y_predict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>sepal length</th>\n",
       "      <th>sepal width</th>\n",
       "      <th>petal length</th>\n",
       "      <th>petal width</th>\n",
       "      <th>species</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>5.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>4.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>4.7</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>4.6</td>\n",
       "      <td>3.1</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.6</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0  sepal length  sepal width  petal length  petal width  species\n",
       "0           0           5.1          3.5           1.4          0.2        0\n",
       "1           1           4.9          3.0           1.4          0.2        0\n",
       "2           2           4.7          3.2           1.3          0.2        0\n",
       "3           3           4.6          3.1           1.5          0.2        0\n",
       "4           4           5.0          3.6           1.4          0.2        0"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "iris = pd.read_csv('~/Downloads/iris.csv')\n",
    "iris.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = iris[iris['species'] < 2][['sepal length', 'sepal width']]\n",
    "y = iris[iris['species'] < 2]['species']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=32)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[-0.043268080317835404, 0.05475142245316805, -0.2676251523877654]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_pred = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[16,  4],\n",
       "       [ 1, 12]], dtype=int64)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "confusion_matrix(y_test, y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9230769230769231"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "recall_score(y_test, y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.75"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "precision_score(y_test, y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8275862068965517"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f1_score(y_test, y_pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Ro3OmaZKlSocP36co0ePsn79eoYNG5bucl944QWKFCnCunXrADh06FC682zdupWFCxcSEhJCUlISM2fOpF+/fixdupSKFStSpkwZbr31Vh5++GGuvPJKdu3aRZcuXdi0adM5y1m+fDl169ZNHq5ZsyaLFy8mNDSUhQsXMnLkSL744gsAlixZwtq1aylevDgjR46kffv2vP/++xw+fJimTZvSsWNHSpcuzYIFCyhQoADbtm2jT58+LF++/Lz4W7duzbFj57dg/dprr9GxY8dzPvvnn3+47LLLACfZFilShJiYGEqWLJk8TdWqVdm8eTM7d+4kIiKCWbNmcfr0aQBGjRpF586defvttzlx4gQLFy5Mnq9x48Y89dRT6e7vzJDrE8XQod/y5ptLqVq1ON99dzudOlUJdkgmJ7qAX/6ZKTY2lgYNGrBz504aNWpEp06dAM77VevpQurhFi5cyPTp05OHixVLv1WCm2++mZAQ547B3r178/zzz9OvXz+mT59O7969k5e7cePG5HmOHj3KsWPHCA8PT/5s7969yb/CwfnFfdddd7Ft2zZEhPj4+ORxnTp1onhx50aU7777jjlz5vDaa68Bzm3Mu3btoly5cgwePJjVq1cTEhLC1q1bU43/559/Tncbz9BUunFIuX+LFSvGhAkT6N27N3ny5KFly5bs2LEDgGnTptG3b1+GDRvGkiVLuOOOO1i/fj158uShdOnS7Nmzx+dYLkauTBRJSU65W0hIHpo2Lc8zz7RhxIjWFCiQK3eHycHCwsJYvXo1R44c4dprr2XcuHE8+OCD1KlTh8WLF58z7Y4dOyhUqBDh4eHUqVOHFStWJBfrpCWthOP5Wcp7+gsWLJj8vkWLFmzfvp3o6GhmzZqV/As5KSmJJUuWEBYW5nXbPJf99NNP065dO2bOnMnOnTtp27ZtqutUVb744gtq1KhxzvJGjRpFmTJlWLNmDUlJSRQoUCDV9V7IFUVERAS7d+8mIiKChIQEjhw5kpywPF133XVcd911AEyaNCk5kb733nt8++23yfsqLi6OAwcOULp0aeLi4rzun8yU6+56WrPmX1q2fI9x45YBcOut9XjuuXaWJEyOVqRIEd566y1ee+014uPjue222/jll1+SizJiY2N58MEHk++4GT58OC+++GLyr+qkpCTGjBlz3nI7d+7M2LFjk4fPFD2V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\n",
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
    "fpr, tpr, thresholds = roc_curve(y_test, model.prob)\n",
    "roc_auc= auc(fpr, tpr)\n",
    "plt.figure()\n",
    "plt.plot(fpr, tpr, color='darkorange', label='ROC curve (area = %0.2f)' % roc_auc)\n",
    "plt.plot([0, 1], [0, 1], color='navy', linestyle='--')\n",
    "plt.xlim([0.0, 1.0])\n",
    "plt.ylim([0.0, 1.05])\n",
    "plt.xlabel('False Positive Rate')\n",
    "plt.ylabel('True Positive Rate')\n",
    "plt.title('Receiver operating characteristic example')\n",
    "plt.legend(loc=\"lower right\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8484848484848485"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(y_test, y_pred)"
   ]
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
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
