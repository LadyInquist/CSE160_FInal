import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

sns.set()


def avg_profit(data, production):
    data['profit'] = data['gross'] - data['budget']
    prod_data = data[[production, 'profit']]
    prod_data = prod_data.groupby([production]).mean()
    prod_data.reset_index(inplace = True)
    prod_data = prod_data.sort_values(by='profit', ascending=False)
    prod_data = prod_data.head(10)

    sns.catplot(x=production, y="profit", data=prod_data, kind="bar")

    production_label = production.capitalize()

    plt.title("Average Profit for Each " + production_label)
    plt.xlabel(production_label)
    plt.xticks(rotation = 90)
    plt.ylabel('Profit ($)')
    # plt.yticks(np.arange(2, 1000000))
    plt.ylim(bottom=100000)

    plt.savefig((production + '_avg_profit.png'), bbox_inches='tight')


def main():
    data = pd.read_csv("/home/movies.csv")
    avg_profit(data, "company")
    avg_profit(data, "director")
    avg_profit(data, "writer")


if __name__ == '__main__':
    main()
