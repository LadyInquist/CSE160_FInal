import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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
    max_depth_mse = []
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)
    for i in range(1, 10):
        model = DecisionTreeRegressor(max_depth=i)
        model.fit(features_train, labels_train)

        train_predictions = model.predict(features_train)
        train_mse = mean_squared_error(labels_train, train_predictions)

        test_predictions = model.predict(features_test)
        test_mse =  mean_squared_error(labels_test, test_predictions)

        max_depth_mse.append({'Depth': i, "Train MSE": train_mse,
                             "Test Mse": test_mse})
    max_depth_mse = pd.DataFrame(max_depth_mse)
    return max_depth_mse

def plot_max(data):
    fig, [ax1, ax2] = plt.subplots(nrows=2)
    data.plot(x='Depth', y='Train MSE', ax=ax1)
    ax1.set_title('Train Accuracy')
    data.plot(x='Depth', y='Test Mse', ax=ax2)
    ax2.set_title('Test Accuracy')
    plt.title("Train"'Accuracy as Max Depth Changes')
    plt.xlabel('Max Depth')
    plt.savefig("ML Depth Testing")