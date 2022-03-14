import pandas as pd
import seaborn as sns
from rating_model import ml_regressor
from research_question_2

def main():
    data = pd.read_csv("movies.csv")
    data = data.dropna()
    ml_regressor(data)

    # calling visualizations for research question 2
    avg_profit(data, "company")
    avg_profit(data, "director")
    avg_profit(data, "writer")
    profits_by_year(data, "company")
    profits_by_year(data, "director")
    profits_by_year(data, "writer")
    
    print("testing part 2")


if __name__ == '__main__':
    main()
