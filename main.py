import pandas as pd
import seaborn as sns
from rating_model import ml_regressor
from average_profit import avg_profit

def main():
    data = pd.read_csv("movies.csv")
    data = data.dropna()
    ml_regressor(data)
    # testing visualizations (problem 2)
    avg_profit(data, "company")
    avg_profit(data, "director")
    avg_profit(data, "writer")
    
    print("testing part 2")


if __name__ == '__main__':
    main()
