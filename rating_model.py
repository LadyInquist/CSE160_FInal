import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


def score_predictor(data, x):
    data = data[x]
    features = data.loc[:, data.columns != "score"]
    features = pd.get_dummies(features)
    labels = data["score"]
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.3)
    model = DecisionTreeRegressor(max_depth=17)
    model.fit(features_train, labels_train)
    # Compute training accuracy
    train_predictions = model.predict(features_train)
    print('Train MSE:',
          mean_squared_error(labels_train, train_predictions))
    print('Train R2:',
          r2_score(labels_train, train_predictions))
    # Compute test accuracy
    test_predictions = model.predict(features_test)
    print('Test  MSE:',
            mean_squared_error(labels_test, test_predictions))
    print('Test  R2:',
            r2_score(labels_test, test_predictions))
            
    return (mean_squared_error(labels_test, test_predictions),
            r2_score(labels_test, test_predictions))

def find_max_depth(data):
    features = data.loc[:, data.columns != "score"]
    features = pd.get_dummies(features)
    labels = data["score"]
    mse_scores = {}
    for i in range(10, 20, 1):
        features_train, features_test, labels_train, labels_test = \
            train_test_split(features, labels, test_size=0.2)
        model = DecisionTreeRegressor(max_depth=i)
        model.fit(features_train, labels_train)
        test_predictions = model.predict(features_test)
        mse_scores[i] = mean_squared_error(labels_test, test_predictions)
    print(mse_scores)

def genre_predictor(data, x):
    data = data[x]
    features = data.loc[:, data.columns != "genre"]
    features = pd.get_dummies(features)
    labels = data["genre"]
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
    model = DecisionTreeClassifier(max_depth=20)
    model.fit(features_train, labels_train)

    # Compute training accuracy
    train_predictions = model.predict(features_train)
    print('Train accuracy:', accuracy_score(labels_train,
                                            train_predictions))
    # Compute test accuracy
    test_predictions = model.predict(features_test)
    print('Test  accuracy:',
            accuracy_score(labels_test, test_predictions))
    return accuracy_score(labels_test, test_predictions)