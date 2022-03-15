import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

sns.set()


def avg_profit(data, production):
    # Giving an acronym to the company, "Beijing Dengfeng International Culture Communications Company"
    data['company'] = data['company'].replace(['Beijing Dengfeng International Culture Communications Company'], 'BDICCC')

    # Organizing data for the visualization
    data['profit'] = (data['gross'] - data['budget'])
    data['gross'] = (data['gross'])
    data['budget'] = (data['budget'])
    prod_data = data[[production, 'profit', 'gross', 'budget']]
    prod_data = prod_data.groupby([production]).mean()
    prod_data = prod_data.sort_values(by='profit', ascending=False)
    prod_data = prod_data.head(10)
    prod_data.reset_index(inplace = True)
    prod_data = prod_data.melt(id_vars=[production])
    prod_data.rename(columns = {'variable':'Type'}, inplace = True)
    prod_data['value'] = prod_data['value'] / 100000

    sns.catplot(x=production, y='value', data=prod_data, kind="bar", hue='Type', height=5, aspect=2)

    if production == 'company':
        production_label = 'Companies'
    else:
        production_label = (production.capitalize() + 's')

    plt.title("Average Finances for Top 10 " + production_label, weight='bold').set_fontsize('18')
    plt.xlabel(production_label, weight='bold')
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.ylabel('Value (in $100,000)', weight='bold')

    plt.savefig((production + '_avg_profit.png'), bbox_inches='tight')


def profits_by_year(data):
    data['profit'] = (data['gross'] - data['budget']) / 100000
    prod_data = data.groupby(['year']).mean()
    prod_data.reset_index(inplace = True)

    sns.relplot(x='year', y='profit', data=prod_data, kind="line", height=5, aspect=2)

    plt.title('Average Profits of Movies over Time', weight='bold').set_fontsize('18')
    plt.xlabel('Year', weight='bold')
    plt.ylabel('Profit (in $100,000)', weight='bold')

    plt.savefig(('movie_profits'), bbox_inches='tight')
