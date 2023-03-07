
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r'time_series_visualizer\fcc-forum-pageviews.csv')
df.set_index('date')


# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) 
    & (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Create a draw_line_plot function that uses Matplotlib 
    # to draw a line chart similar to "examples/Figure_1.png". 
    # The title should be Daily freeCodeCamp Forum Page Views 
    # 5/2016-12/2019. The label on the x axis should be Date and 
    # the label on the y axis should be Page Views.
    df_line = df.copy()

    # Draw line plot
    # ax = df_line.plot(kind="line")
    # fig = ax.get_figure()
    # ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    # ax.set_xlabel('Date')
    # ax.set_ylabel('Page Views')

    plt.figure()
    ax = sns.lineplot(data = df_line, x='date', y='value')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig = ax.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
   
    df_bar = df.copy()
    df_bar['date'] = pd.to_datetime(df_bar['date'])
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.strftime('%B') for d in df_bar.date]

    months_ordered = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar.month = pd.Categorical(
        df_bar.month,
        categories=months_ordered,
        ordered=True
    )
    df_bar.sort_values('month')
    
    df_bar = df_bar.groupby([(df_bar.year), (df_bar.month)]).mean()

    # Draw bar plot
    # Create a draw_bar_plot function that draws a bar chart similar to 
    # "examples/Figure_2.png". It should show average daily page views 
    # for each month grouped by year. The legend should show month labels 
    # and have a title of Months. On the chart, the label on the x axis 
    # should be Years and the label on the y axis should be Average Page 
    # Views.

    df_pivot = pd.pivot_table(
        df_bar, 
        values="value",
        index="year",
        columns="month",
        # aggfunc=np.sum
    )
    

    ax = df_pivot.plot(kind="bar")
    fig = ax.get_figure()
    fig.set_size_inches(7, 6)
    ax.set_title('Months')
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # plt.show()

    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    # df_box[["year", "month", "day"]] = df_box["date"].str.split("-", expand = True)
    df_box['date'] = pd.to_datetime(df_box['date'])
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    months_ordered = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box.month = pd.Categorical(
        df_box.month,
        categories=months_ordered,
        ordered=True
    )
    df_box.sort_values('month')

    # Create a draw_box_plot function that uses Seaborn to draw two adjacent 
    # box plots similar to "examples/Figure_3.png". These box plots should 
    # show how the values are distributed within a given year or month and 
    # how it compares over time. The title of the first chart should be Year-
    # wise Box Plot (Trend) and the title of the second chart should be Month-wise 
    # Box Plot (Seasonality). Make sure the month labels on bottom start at Jan 
    # and the x and y axis are labeled correctly. The boilerplate includes 
    # commands to prepare the data

    # Draw box plots (using Seaborn)
    plt.figure()
    fig, (f1,f2) = plt.subplots(1,2)
    fig.set_figwidth(20)
    fig.set_figheight(10)

    f1 = sns.boxplot(x=df_box['year'], y = df_box['value'], data = df_box, ax = f1)
    
    f1.set_title("Year-wise Box Plot (Trend)")
    f1.set_xlabel("Year")
    f1.set_ylabel("Page Views")

    f2 = sns.boxplot(x=df_box['month'], y = df_box['value'], data = df_box, ax = f2)
    f2.set_title("Month-wise Box Plot (Seasonality)")
    f2.set_xlabel("Month")
    f2.set_ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
