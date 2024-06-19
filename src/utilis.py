import pandas as pd
import numpy as np
from IPython.display import Image
import seaborn as sns
import matplotlib.pyplot as plt

def plot_hist(df:pd.DataFrame, column:str, color:str)->None:
    # plt.figure(figsize=(15, 10))
    # fig, ax = plt.subplots(1, figsize=(12, 7))
    sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    plt.show()



# def plot_scatter(df, time_duration_col, trip_id_col):
#     """
#     Plots a scatterplot of trip duration vs. trip_id for a Pandas DataFrame.
    
#     Parameters:
#     df (pandas.DataFrame): The DataFrame containing the data to be plotted.
#     time_duration_col (str): The name of the column containing the time duration values.
#     trip_id_col (str): The name of the column containing the trip ID values.
#     """
#     fig, ax = plt.subplots(figsize=(10, 6))
#     ax.scatter(df[trip_id_col], df[time_duration_col])
#     ax.set_title(f'{time_duration_col} vs. Trip ID')
#     ax.set_xlabel(trip_id_col)
#     ax.set_ylabel(time_duration_col)
#     plt.show()

def plot_scatter(df, col_1, col_2):
    """
    Plots a scatterplot of trip duration vs. trip_id for a Pandas DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data to be plotted.
    time_duration_col (str): The name of the column containing the time duration values.
    trip_id_col (str): The name of the column containing the trip ID values.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df[col_1], df[col_2])
    ax.set_title(f'{col_1} vs. {col_2}')
    ax.set_xlabel(f"{col_2}")
    ax.set_ylabel(f"{col_2}")
    plt.show()


    import matplotlib.pyplot as plt

def plot_column_vs_column(df, x_col, y_col, title=None, x_label=None, y_label=None, figsize=(10, 6)):
    """
    Plots a scatterplot of one column vs. another column in a Pandas DataFrame.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing the data to be plotted.
    x_col (str): The name of the column to be plotted on the x-axis.
    y_col (str): The name of the column to be plotted on the y-axis.
    title (str, optional): The title of the plot. If not provided, a default title will be used.
    x_label (str, optional): The label for the x-axis. If not provided, the x_col name will be used.
    y_label (str, optional): The label for the y-axis. If not provided, the y_col name will be used.
    figsize (tuple, optional): The size of the figure, in inches. The default is (10, 6).
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(df[x_col], df[y_col])
    
    if title is None:
        title = f"{y_col} vs. {x_col}"
    ax.set_title(title)
    
    if x_label is None:
        x_label = x_col
    ax.set_xlabel(x_label)
    
    if y_label is None:
        y_label = y_col
    ax.set_ylabel(y_label)
    
    plt.show()
