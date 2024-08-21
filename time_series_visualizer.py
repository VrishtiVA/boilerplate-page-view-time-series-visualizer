import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#The modules seem to be out of date.

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    "fcc-forum-pageviews.csv", 
    index_col = ['date'], 
    parse_dates = True
)

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025) ) &
    (df['value'] <= df['value'].quantile(0.975) )
]

def draw_line_plot():
    # Draw line plot

    fig = plt.figure(figsize=(16,5))
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    plt.plot(df, c = 'r')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.strftime('%B')
    print(df_bar.head(), df_bar.dtypes)

    # Draw bar plot
    fig = plt.figure(figsize = (8,7), dpi = 300)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    sns.barplot(
        data = df_bar, x = 'Years', y = 'value',
        hue = 'Months', hue_order = months,
        #estimator = np.mean, 
        ci = None, palette = "tab10",
    )

    plt.legend(loc='upper left')
    plt.xticks(rotation = 90)
    plt.ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():

    #Working on fixing this one

    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace = True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2, figsize = (16, 5), dpi = 300)
    months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    sns.boxplot(
        data = df_box, x = 'year', y = 'value', ax = axs[0],
        hue = 'year', palette = 'tab10',
        #fliersize = 2, flierprops = dict(marker='d')
    )
    
    sns.boxplot(
        data = df_box, x = 'month', y = 'value' , ax = axs[1],
        order = months, hue_order = months, hue = 'month',
        #fliersize = 2, flierprops = dict(marker='d')
    )

    axs[0].set_title("Year-wise Box Plot (Trend)")
    axs[0].set_xlabel("Year")

    axs[1].set_title("Month-wise Box Plot (Seasonality)")
    axs[1].set_xlabel("Month")

    plt.tight_layout()

    plt.setp( 
        axs, 
        ylabel="Page Views", 
        ylim=(0,200000), yticks=[i for i in range(0, 200001, 20000)]
    )

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
