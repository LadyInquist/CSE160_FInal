import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# sns.set()


def avg_profit(data, production):
    # Giving an acronym to the company, "Beijing Dengfeng International Culture Communications Company"
    data['company'] = data['company'].replace(['Beijing Dengfeng International Culture Communications Company'], 'BDICCC')

    data['profit'] = (data['gross'] - data['budget']) / 100000
    prod_data = data[[production, 'profit']]
    prod_data = prod_data.groupby([production]).mean()
    prod_data.reset_index(inplace = True)
    prod_data = prod_data.sort_values(by='profit', ascending=False)
    prod_data = prod_data.head(10)

    sns.catplot(x=production, y="profit", data=prod_data, kind="bar", height=5, aspect=2)

    production_label = production.capitalize()

    plt.title("Average Profit for Each " + production_label, weight='bold').set_fontsize('18')
    plt.xlabel(production_label, weight='bold')
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.ylabel('Profit (in $100,000)', weight='bold')
    plt.ticklabel_format(style='plain', axis='y')

    plt.savefig((production + '_avg_profit.png'), bbox_inches='tight')


def main():
    data = pd.read_csv("/home/movies.csv")
    avg_profit(data, "company")
    avg_profit(data, "director")
    avg_profit(data, "writer")


if __name__ == '__main__':
    main()
