import pandas as pd
import seaborn as sns
from rating_model import ml_regressor

def main():
    data = pd.read_csv("movies.csv")
    data = data.dropna()
    ml_regressor(data)
    print("testing part 2")


if __name__ == '__main__':
    main()
