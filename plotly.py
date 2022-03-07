"""
Ethan Hu
CSE 163

Demonstrates the utility of the plotly libary by processing
an IMDB dataset. Aimed at answering questions pretaining to
a movies score (user based rating) by creating visualizations.
Assumes that the pandas and plotly libaries are properly
installed, and that the imdb dataset is in the same location
as this file.
"""

import pandas as pd
import plotly.express as px
import plotly.offline as off

CROP_AMOUNT = 100

def main():
    """
    Primary method, change the second parameter of
    rating_scatter and rating_bar to column names
    to generate plots related to them.
    """
    data = pd.read_csv("movies.csv")
    data = data.dropna()
    rating_scatter(data, "country", "TOP")
    rating_bar(data, "genre")


def rating_bar(data, second_factor):
    """
    Creates an .html page containing an interactive bar plot. This graph is
    based on an imdb dataframe, data, alongside a column within that dataframe,
    second_factor. Assumes that the given dataset is the correct IMDB dataset,
    and that second_factor is a valid column name. Outputs it as an image,
    with the name dependent on the column.
    """
    data = data.groupby(second_factor).mean()
    data.reset_index(inplace=True)
    data = data.sort_values("score")
    fig = px.bar(data,
                 x=second_factor,
                 y="score",
                 title=(second_factor + " as a factor of score "))
    file_name = second_factor + '_bar.html'
    off.plot(fig, filename=file_name)


def rating_scatter(data, third_factor, crop=""):
    """
    Creates an .html page containing an interactive scatterplot. This graph is
    based on an imdb dataframe, data, alongside a column within that dataframe,
    third_factor. Assumes that the given dataset is the correct IMDB dataset,
    and that third_factor is a valid column name. Outputs it as an image,
    with the name dependent on the column.
    """
    data = data.sort_values("score", ascending=False)
    crop = crop.capitalize()
    if crop == "Top":
        data = data.head(CROP_AMOUNT)
    elif crop == "Bottom":
        data = data.tail(CROP_AMOUNT)
    title_concat = "Budget and " + third_factor + " as factors in " + crop + " scored movies"
    fig = px.scatter(data,
                     x="budget",
                     y="score",
                     color=third_factor,
                     title=(title_concat),
                     hover_name="name",
                     trendline="ols")
    fig.update_layout(
        hoverlabel=dict(
            font_size=16,
            font_family="Arial"
        )
    )
    fig.update_yaxes(
        range=[0,10],  # sets the range of xaxis
    )
    file_name = crop + "_" + third_factor + "_and_budget.html"
    print(file_name)
    off.plot(fig, filename=file_name)


if __name__ == '__main__':
    main()