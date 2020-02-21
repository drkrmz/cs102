from collections import Counter
from math import log
from numpy import argmax


class NaiveBayesClassifier:

    def __init__(self, alpha=0.05):
        self.alpha = alpha

    def fit(self, X, y):
        self.labels_list = []
        self.n_news = len(y)
        self.n_labels = len(dict(Counter(y)))
        self.y_counter = Counter(y)
        labeled_words = []
        for i in range(self.n_labels):
            self.labels_list.append(list(Counter(y))[i])
            labeled_words.append([])
        for i in range(len(X)):
            for word in X[i].split():
                j = 0
                while not y[i] in self.labels_list[j]:
                    j += 1
                labeled_words[j].append(word)
        labels_count = []
        n_words = []
        all_words = []
        self.P_words = []
        for i in range(self.n_labels):
            n_words.append(sum(Counter(labeled_words[i]).values()))
            labels_count.append(Counter(labeled_words[i]))
            all_words.extend(labeled_words[i])
            self.P_words.append(dict())
        all_words = Counter(all_words)
        for word in all_words:
            for i in range(self.n_labels):
                value = (labels_count[i][word] + self.alpha) / (n_words[i] + (self.alpha * len(all_words)))
                self.P_words[i].update({word: value})

    def predict(self, X):
        news_predict = []
        P_each = []
        ln = []
        for i in range(self.n_labels):
            ln.append(0)
            P_each.append(self.y_counter[self.labels_list[i]]/self.n_news)
        for i in range(len(X)):
            for j in range(self.n_labels):
                ln[j] = log(P_each[j])
            for word in X[i].split():
                for j in range(self.n_labels):
                    if word in self.P_words[j]:
                        ln[j] += log(self.P_words[j][word])
            news_predict.append(self.labels_list[argmax(ln)])
        return news_predict

    def score(self, X_test, y_test):
        y = self.predict(X_test)
        correct = 0
        for i in range(len(y)):
            if y[i] == y_test[i]:
                correct += 1
        return correct/len(y)
