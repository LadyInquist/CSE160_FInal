from numpy import average
import pandas as pd
import seaborn as sns
from research_question_3 import score_predictor
from research_question_3 import average_score
from research_question_2 import *
from research_question_1 import *


def main():
    data = pd.read_csv("movies.csv")
    data_2021 = pd.read_csv("movies_2021.csv")
    data = data.dropna()
    #########
    print("ML using the critical columns as features")
    print(average_score(data, ["star", "director", "company", "score"]))

    print("ML using comparing pre 2021 and 2021")
    print("pre 2021")
    print(average_score(data, ["rating", "gross", "star", "director",
                               "company", "score", "rating", "genre"]))
    print("2021")
    print(average_score(data_2021, ["rating", "gross", "star", "director",
                        "company", "score", "rating", "genre"]))

    rate_scatter(data, "runtime", "country", crop="TOP")
    rate_bar(data, "genre")
    score_predictor(data, ["budget", "score", "company", "director"])
    print()
    score_predictor(data, ["budget", "score", "company", "director", "genre",
                "year", "runtime"])
    print()
    score_predictor(data, ["budget", "score", "company", "director", "genre",
                "year", "runtime", "gross", "year", "star"])
    """
    # calling visualizations for research question 2
    avg_profit(data, "company")
    avg_profit(data, "director")
    avg_profit(data, "writer")
    profits_by_year(data)
    print("testing part 2")
    """
    print("testing part 2")


if __name__ == '__main__':
    main()
