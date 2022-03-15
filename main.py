import pandas as pd
import seaborn as sns
from rating_model import ml_regressor
from research_question_2 import *


def main():
    data = pd.read_csv("movies.csv")
    data = data.dropna()
    ml_regressor(data, ["budget", "score", "company", "director"])
    print()
    ml_regressor(data , ["budget", "score", "company", "director", "genre",
                 "runtime"])
    print()
    ml_regressor(data , ["budget", "score", "company", "director", "genre",
                "year", "runtime", "rating", "gross", "year"])
    """
    # calling visualizations for research question 2
    avg_profit(data, "company")
    avg_profit(data, "director")
    avg_profit(data, "writer")
    profits_by_year(data)
    
    print("testing part 2")
    """

if __name__ == '__main__':
    main()
