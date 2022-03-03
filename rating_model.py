import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


class RatingModel:
    def __init__(self, label, data, regressor):
        self._data = data
        features = data.loc[:, data.columns != label]
        features = pd.get_dummies(features)
        labels = data[label]
        self._regressor = regressor
        self._features_train, self._features_test, self._labels_train, self._labels_test = \
            train_test_split(features, labels, test_size=0.2)
        print(self._features_train, self._features_test, self._labels_train, self._labels_test)

    def ml_regressor(self):
        model = DecisionTreeRegressor()
        model.fit(self._features_train, self._labels_train)
        # Compute training accuracy
        train_predictions = model.predict(self._features_train)
        print('Train MSE:',
              mean_squared_error(self._labels_train, train_predictions))
        # Compute test accuracy
        test_predictions = model.predict(self._features_test)
        print('Test  MSE:',
              mean_squared_error(self._labels_test, test_predictions))
        # return mean_squared_error(self._labels_test, self._test_predictions)

    def ml_classifier(self):
        if not self._regressor:
            model = DecisionTreeClassifier()
            model.fit(self._features_train, self._labels_train)

            # Compute training accuracy
            train_predictions = model.predict(self._features_train)
            print(train_predictions)
            print(self._labels_train)
            print('Train accuracy:', accuracy_score(self._labels_train,
                                                    self._train_predictions))

            # Compute test accuracy
            test_predictions = model.predict(self._features_test)
            print('Test  accuracy:',
                  accuracy_score(self._labels_test, test_predictions))
        else:
            return "Please use regression"

