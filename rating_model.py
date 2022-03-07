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
    def to_month(release_date):
        release_date = str(release_date).split('(')[0]
        if len(release_date.strip().split(' ')) >= 3:
            month = dt.datetime.strptime(release_date.strip(),
                                        "%B %d, %Y")
            return month.month
        else:
            return 0
# Might not need this function at all actually


    def movies_by_weekday(data):
        """
        Assuming that the data parameter is the IMDB dataframe,
        plots lines of best fit for both budget and profit
        as a factor of IMDB score.
        """
        r = data['rating'] == "R"
        pg = data['rating'] == "PG"
        pg13 = data['rating'] == "PG-13"
        data = data[r | pg | pg13]
        data['month'] = data["released"].apply(to_month)
        data = data.sort_values('month')
        print(data)
        data = data[["rating", "score", "genre", "budget", "company", "runtime",
                    "month"]]

        sns.catplot(x='month', col='rating', kind='count', data=data)
        plt.savefig('/home/weekday2.png')
