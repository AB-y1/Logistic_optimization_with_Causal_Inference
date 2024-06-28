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

def rm_outliers_using_IQR(col_name, df):
    """
    Removes outliers from a dataframe column using the IQR method.
    
    Args:
        col_name (str): The name of the column to apply the IQR method on.
        df (pandas.DataFrame): The dataframe containing the column.
        
    Returns:
        pandas.DataFrame: The dataframe with outliers removed.
    """
    Q1 = df[col_name].quantile(0.25)
    Q3 = df[col_name].quantile(0.75)
    
    IQR = Q3 - Q1
    
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    
    df_cleaned = df[(df[col_name] >= lower_limit) & (df[col_name] <= upper_limit)]

    return df_cleaned




def plot_histogram(df, x_col, y_col):
    """
    Plots a histogram to visualize the relationship between two columns in a Pandas DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    x_col (str): The name of the column to be plotted on the x-axis.
    y_col (str): The name of the column to be plotted on the y-axis.
    """
    plt.figure(figsize=(12, 6))
    sns.histplot(data=df, x=x_col, y=y_col, kde=True, bins=20)
    plt.title(f"Histogram of {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()


def calculate_speed(df, distance_col, duration_col):
    """
    calculate the speed by dividing the trip distance on the trip duration

    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    distance_col (float): The name of the distance column.
    duration_col (float): The name of the duration column.

    """
    # Calculate the speed per hour and handle division by zero
    df['speed_km/h'] = np.where(df[duration_col] > 0, 
                                df[distance_col] / (df[duration_col]/60), 
                                0)

    return df['speed_km/h']