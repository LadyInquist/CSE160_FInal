"""
Ethan Hu
CSE 163

Demonstrates the utility of the plotly libary by processing
an IMDB dataset. Aimed at answering questions pretaining to
a movies score (user based rating) by creating visualizations.
Assumes that the pandas and plotly libaries are properly
installed, and that the imdb dataset is in the same location
as this file. CROP_AMOUNT dictates the amount of top or bottom
movies that the rating_scatter pulls from.
"""

import plotly.express as px
import plotly.offline as off


# amount of rows that a crop takes
CROP_AMOUNT = 500


def rate_bar(data, second_factor):
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
                 title=(second_factor + " as a factor of score ").capitalize())
    file_name = second_factor + '_bar.html'
    off.plot(fig, filename=file_name)


def rate_scatter(data, second_factor="budget", third_factor="genre", crop=""):
    """
    Creates an .html page containing an interactive scatterplot. This graph is
    based on an imdb dataframe, data,
    alongside 2 columns within that dataframe, third_factor.
    Crop can indicate top or bottom to only show the top or bottom values.
    Assumes that the given dataset is the correct IMDB dataset,
    second_factor is a column with non-categorical values,
    and that second and third_factor are valid column names. Outputs it as an
    image, with the name dependent on the column.
    """
    data = data.sort_values("score", ascending=False)
    crop = crop.lower()
    if crop == "top":
        data = data.head(CROP_AMOUNT)
    elif crop == "bottom":
        data = data.tail(CROP_AMOUNT)
    else:
        crop = "All"
    title_concat = second_factor + " and " + third_factor +\
        " as factors in " + crop + " scored movies"
    title_concat = title_concat.capitalize()
    fig = px.scatter(data,
                     x=second_factor,
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
        range=[0, 10]
    )
    file_name = crop + "_" + third_factor + "_and_" + second_factor + ".html"
    print(file_name)
    off.plot(fig, filename=file_name)
