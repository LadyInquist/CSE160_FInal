'''
Angelina Lum
CSE 163 AC

Creates cat plots and a line plot of the movie dataset with
the matplotlib and seaborn library. It is aimed at answering
research question 2, where we analyze the top companies,
directors, and writers' finances and see which ones have the
highest profits. Additionally analyzes how the trend of movie
profits have increased or decreased from 1980 - 2020.
'''

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


def avg_profit(data, production):
    '''
    Takes in the movie dataset and a production (company, director, or writer)
    and returns a cat plot of the top 10 productions' finances: budgets, gross,
    and profits. Graphs will be sorted by the ones that received the highest
    earning profits. It will plot the values of the finances in $100,000 on
    the y-axis and the production names on the x-axis.
    '''
    # Giving an acronym to the company,
    # "Beijing Dengfeng International Culture Communications Company"
    data['company'] = data['company']. \
        replace([
            'Beijing Dengfeng International Culture Communications Company'],
            'BDICCC')

    # Organizing data for the visualization
    data['profit'] = (data['gross'] - data['budget'])
    data['gross'] = (data['gross'])
    data['budget'] = (data['budget'])
    prod_data = data[[production, 'profit', 'gross', 'budget']]
    prod_data = prod_data.groupby([production]).mean()
    prod_data = prod_data.sort_values(by='profit', ascending=False)
    prod_data = prod_data.head(10)
    prod_data.reset_index(inplace=True)
    prod_data = prod_data.melt(id_vars=[production])
    prod_data.rename(columns={'variable': 'Type'}, inplace=True)
    prod_data['value'] = prod_data['value'] / 100000

    sns.catplot(x=production, y='value', data=prod_data,
                kind="bar", hue='Type', height=5, aspect=2)

    if production == 'company':
        production_label = 'Companies'
    else:
        production_label = (production.capitalize() + 's')

    plt.title("Average Finances for Top 10 " +
              production_label, weight='bold').set_fontsize('18')
    plt.xlabel(production_label, weight='bold')
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.ylabel('Value (in $100,000)', weight='bold')

    plt.savefig((production + '_avg_profit.png'), bbox_inches='tight')


def profits_by_year(data):
    '''
    Takes in the movie dataset and plots the average profit
    for each year on a lineplot. It will show the relationship
    of movies' profits over time from 1980 - 2020.
    '''
    data['profit'] = (data['gross'] - data['budget']) / 100000
    prod_data = data.groupby(['year']).mean()
    prod_data.reset_index(inplace=True)

    sns.relplot(x='year', y='profit', data=prod_data,
                kind="line", height=5, aspect=2)

    plt.title('Average Profits of Movies over Time',
              weight='bold').set_fontsize('18')
    plt.xlabel('Year', weight='bold')
    plt.ylabel('Profit (in $100,000)', weight='bold')

    plt.savefig(('movie_profits'), bbox_inches='tight')
