"""
Raj Chaphekar (AB), Ethan Hu (AB), Angelina Lum (AC)
CSE 163

Description
"""
import pandas as pd

import datetime as dt
from rating_model import RatingModel


# I don't think we actually need to use this
def to_month(release_date):
    release_date = str(release_date).split('(')[0]
    if len(release_date.strip().split(' ')) >= 3:
        month = dt.datetime.strptime(release_date.strip(),
                                     "%B %d, %Y").strftime("%B")
        return str(month)
    else:
        return " "
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
    data['released_weekday'] = data["released"].apply(to_month)
    data = data[["rating", "score", "genre", "budget", "company", "runtime",
                 "released_weekday"]]

    sns.countplot(x='released_weekday', hue='rating', data=data)
    plt.savefig('/home/weekday2.png')


def main():
    
    data = pd.read_csv("/home/movies.csv")
    print(data["released"].apply(to_weekday))
    '''
    print(data.head())
    score_model(data)
    
    ml_data = data[["rating", "score", "genre", "budget", "company", "runtime"]]
    r = RatingModel('score', ml_data, True)
    print(r)
    #print(r.ml_classifier())
    print(r.ml_regressor())
    '''


if __name__ == '__main__':
    main()
