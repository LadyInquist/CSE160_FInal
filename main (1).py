import pandas as pd
import seaborn as sns

def main():
    data = pd.read_csv("movies.csv")
    data = data.dropna()
    print("testing part 2")


if __name__ == '__main__':
    main()
