"""
Raj Chaphekar
CSE 163 AB

This file has various functions to create and evaluate a machine learning
algorithm for the score column of the data.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split


def score_predictor(data, attributes):
    """
    Takes in a dataset and the columns for the features and creates a machine
    learning model, returning the test data MSE.
    """
    data = data[attributes]
    features = data.loc[:, data.columns != "score"]
    features = pd.get_dummies(features)
    labels = data["score"]
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
    model = DecisionTreeRegressor(max_depth=30)
    model.fit(features_train, labels_train)
    test_predictions = model.predict(features_test)

    mse_score = mean_squared_error(labels_test, test_predictions)
    return (mse_score)


def find_max_depth(data, attributes):
    """
    Takes in a dataset and the columns for the features and runs multiple
    regressor models at different max_depth hyperparameters and creates a
    data frame to store the different values.
    """
    data = data[attributes]
    features = data.loc[:, data.columns != "score"]
    features = pd.get_dummies(features)
    labels = data["score"]
    max_depth_mse = []
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
    for i in range(1, 50, 2):
        model = DecisionTreeRegressor(max_depth=i)
        model.fit(features_train, labels_train)

        train_predictions = model.predict(features_train)
        train_mse = mean_squared_error(labels_train, train_predictions)

        test_predictions = model.predict(features_test)
        test_mse = mean_squared_error(labels_test, test_predictions)

        max_depth_mse.append({'Depth': i, "Train MSE": train_mse,
                             "Test Mse": test_mse})
    max_depth_mse = pd.DataFrame(max_depth_mse)
    return max_depth_mse


def plot_max(data):
    """
    Takes a dataset of the depth, train mse, and test mse to plot them on two
    different axes and compare the MSE at different max_depth
    """
    fig, [ax1, ax2] = plt.subplots(nrows=2)
    data.plot(x='Depth', y='Train MSE', c='#a98d19', ax=ax1)
    data.plot(x='Depth', y='Test Mse', c='#a98d19', ax=ax2)
    plt.xlabel('Max Depth')
    plt.savefig("ML Depth Testing.png")


def average_score(data, attributes):
    """
    Takes in a dataset and column names and uses the score_predictor function
    to return the average MSE from multiple models.
    """
    sum = 0
    for i in range(3):
        s = score_predictor(data, attributes)
        sum += s
    return sum / 3.0
