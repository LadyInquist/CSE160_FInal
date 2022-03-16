"""
Ethan Hu, Raj Chaphekar, Angelina Lum
CSE 163

Main file for project. Imports and runs the nessasary
code to answer 3 research questions. Assumes that
requisite libaries are installed and that the valid
IMDB csv is present.
"""

import pandas as pd
from research_question_1 import rate_scatter
from research_question_1 import rate_bar
from research_question_2 import avg_profit
from research_question_2 import profits_by_year
from research_question_3 import average_score


def main():
    data = pd.read_csv("movies.csv")
    data_2021 = pd.read_csv("movies_2021.csv")
    data = data.dropna()

    # research question 1
    rate_scatter(data, "runtime", "country", crop="TOP")
    rate_bar(data, "genre")

    # research question 2
    avg_profit(data, "company")
    avg_profit(data, "director")
    avg_profit(data, "writer")
    profits_by_year(data)

    # research question 3
    print("ML using the critical columns as features")
    print(average_score(data, ["star", "director", "company", "score"]))

    print("ML using comparing pre 2021 and 2021")
    print("pre 2021")
    print(average_score(data, ["rating", "gross", "star", "director",
                               "company", "score", "rating", "genre"]))
    print("2021")
    print(average_score(data_2021, ["rating", "gross", "star", "director",
                        "company", "score", "rating", "genre"]))


if __name__ == '__main__':
    main()
