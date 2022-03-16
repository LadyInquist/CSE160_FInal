import pandas as pd
from research_question_3 import find_max_depth
from research_question_3 import score_predictor
from research_question_3 import plot_max


def potential_range(mse_scores):
    if mse_scores < 1.75:
        print("Valid!")
    else:
        print("Make model more optimal")


def compare_scores():
    for i in range(10):
        print("hi")


def finding_depth(data):
    """
    Calls the functions in rating
    """
    ml_data = find_max_depth(data, ["star", "director", "company", "score",
                             "rating", "genre", "runtime", "gross"])
    plot_max(ml_data)
    print(ml_data)


def main():
    data = pd.read_csv("movies.csv")
    data_2021 = pd.read_csv("movies_2021.csv")
    data = data.dropna()
    # testing MSE to be at least under 1 and that train has less error than
    # test
    main_MSE = score_predictor(data, ["star", "director", "company",
                               "score", "rating", "genre", "runtime", "gross"])
    potential_range(main_MSE)
    mse_2021 = score_predictor(data_2021, ["star", "director", "company",
                               "score", "rating", "genre", "runtime", "gross"])
    potential_range(mse_2021)
    # finding the best depth
    finding_depth(data)


if __name__ == '__main__':
    main()
