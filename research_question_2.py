import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

sns.set()


def avg_profit(data, production):
    # Giving an acronym to the company, "Beijing Dengfeng International Culture Communications Company"
    data['company'] = data['company'].replace(['Beijing Dengfeng International Culture Communications Company'], 'BDICCC')

    data['profit'] = (data['gross'] - data['budget']) / 100000
    prod_data = data[[production, 'profit']]
    prod_data = prod_data.groupby([production]).mean()
    prod_data.reset_index(inplace = True)
    prod_data = prod_data.sort_values(by='profit', ascending=False)
    prod_data = prod_data.head(20)

    sns.catplot(x=production, y="profit", data=prod_data, kind="bar", height=5, aspect=2)

    if production == 'company':
        production_label = 'Companies'
    else:
        production_label = (production.capitalize() + 's')

    plt.title("Average Profit for Top 20 " + production_label, weight='bold').set_fontsize('18')
    plt.xlabel(production_label, weight='bold')
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.ylabel('Profit (in $100,000)', weight='bold')
    # plt.ticklabel_format(style='plain', axis='y')

    plt.savefig((production + '_avg_profit.png'), bbox_inches='tight')


def profits_by_year(data, production):
    data['profit'] = (data['gross'] - data['budget']) / 100000
    prod_data = data.groupby(['year']).mean()
    prod_data.reset_index(inplace = True)

    sns.relplot(x='year', y='profit', data=prod_data, kind="line", height=5, aspect=2)

    plt.title('Average Profits of Movies over Time', weight='bold').set_fontsize('18')
    plt.xlabel('Year', weight='bold')
    plt.ylabel('Profit (in $100,000)', weight='bold')
    plt.ticklabel_format(style='plain', axis='y')

    plt.savefig(('movie_profits'), bbox_inches='tight')
