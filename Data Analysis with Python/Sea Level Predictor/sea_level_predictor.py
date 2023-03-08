import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from 
    df = pd.read_csv(r'Data Analysis with Python\Sea Level Predictor\epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.figure()
    plt.scatter(x, y, label='Sea Level Data')
    

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    years_extended = np.arange(df['Year'][0], 2051, 1)

    line = [slope*xi + intercept for xi in years_extended]

    plt.plot(years_extended, line, 'r', label='Best Fit')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    recent_x = df_recent['Year']
    recent_y = df_recent['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(recent_x, recent_y)

    recent_years = np.arange(2000, 2051, 1)
    recent_line = [slope*xi + intercept for xi in recent_years]

    plt.plot(recent_years, recent_line, 'g', label=' 2000 Best Fit')


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')

    plt.legend()
    # plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()