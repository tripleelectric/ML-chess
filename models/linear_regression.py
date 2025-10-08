import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv('../data/games.csv')

class LinearRegression:
    def __init__(self, learning_rate=0.01, epochs=300, ):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0
        self.loss_history = []

    def fit(self, X, y):
        """
        train (adjust the weights) with gradient descent
        :param X: The input matrix
        :param y: the output vector
        :return:
        """
        n_samples, n_features = X.shape()

        self.weights = np.zeros(n_features) # for every feature 1 weight
        self.bias = 0



