import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


class RatingModel:
    def ml_regressor(data):
        data = data[["budget", "score", "company"]]
        features = data.loc[:, data.columns != "score"]
        features = pd.get_dummies(features)
        labels = data["score"]
        features_train, features_test, labels_train, labels_test = \
            train_test_split(features, labels, test_size=0.2)
        model = DecisionTreeRegressor()
        model.fit(features_train, labels_train)
        # Compute training accuracy
        train_predictions = model.predict(features_train)
        print('Train MSE:',
              mean_squared_error(labels_train, train_predictions))
        # Compute test accuracy
        test_predictions = model.predict(features_test)
        print('Test  MSE:',
              mean_squared_error(labels_test, test_predictions))

    def ml_classifier(self):
        data = data[["budget", "score", "rating", "company"]]
        features = data.loc[:, data.columns != "rating"]
        features = pd.get_dummies(features)
        labels = data["rating"]
        features_train, features_test, labels_train, labels_test = \
            train_test_split(features, labels, test_size=0.2)
        model = DecisionTreeClassifier()
        model.fit(features_train, labels_train)

        # Compute training accuracy
        train_predictions = model.predict(features_train)
        print(train_predictions)
        print(labels_train)
        print('Train accuracy:', accuracy_score(labels_train,
                                                train_predictions))

        # Compute test accuracy
        test_predictions = model.predict(features_test)
        print('Test  accuracy:',
                accuracy_score(labels_test, test_predictions))

