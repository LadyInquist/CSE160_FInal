import pandas as pd
import seaborn as sns
from rating_model import *
from research_question_2 import *


def main():
    data = pd.read_csv("movies.csv")
    data = data.dropna()
    #find_max_depth(data)
    
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

if __name__ == '__main__':
    main()