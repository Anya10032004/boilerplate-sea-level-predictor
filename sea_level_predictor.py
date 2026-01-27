import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('/content/epa-sea-level.csv')

    # Create scatter plot
    itemsSubplot = {
    'year' : [],
    'CSIRO': []
    }
    for a in data['Year']:
        itemsSubplot['year'].append(a)
    for a in data['CSIRO Adjusted Sea Level']:
        itemsSubplot['CSIRO'].append(a)
    


    # Create first line of best fit
    result = linregress(itemsSubplot['year'], itemsSubplot['CSIRO'])
    y_pred = [result.slope * xi + result.intercept for xi in itemsSubplot['year']]
    



    # Create second line of best fit
    # Filter the year list
    new = []
    new_y_pred = []
    for a in zip(itemsSubplot['year'], y_pred):
        if a[0]>= 2000:
            new.append(a[0])
            new_y_pred.append(a[1])
    
    # Add more year untul 2050
    for xi in range(2013, 2050):
        new.append(xi)
        a = result.slope * xi + result.intercept
        new_y_pred.append(a)



    # Add labels and title
    plt.plot(new, new_y_pred)
    
    # Scatter points
    plt.scatter(itemsSubplot['year'], itemsSubplot['CSIRO'])
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.show()


    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

    