import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

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
    firstline = [x for x in itemsSubplot['year']]
    result = linregress(itemsSubplot['year'], itemsSubplot['CSIRO'])
    y_pred = [result.slope * xi + result.intercept for xi in itemsSubplot['year']]
    for xi in range(2014, 2051):
        firstline.append(xi)
        a = result.slope * xi + result.intercept
        y_pred.append(a)


    # Create second line of best fit
    # Filter the year list
    year_filter = []
    y_filter = []
    for a in zip(itemsSubplot['year'], itemsSubplot['CSIRO']):
        if a[0]>= 2000:
            year_filter.append(a[0])
            y_filter.append(a[1])
    result2 = linregress(year_filter, y_filter)
    new_y_pred = [result2.slope * xx + result2.intercept for xx in year_filter]

    # Add more year untul 2050
    for xi in range(2014, 2051):
        year_filter.append(xi)
        a = result2.slope * xi + result2.intercept
        new_y_pred.append(a)
    

    # We will start plotting
    # figure and axes
    # figure(variabel fig) --> Canvas
    # axes(variabel ax) ---> area tempat untuk gambar grafik di figure

    fig, ax = plt.subplots()

    # We will start making the plot:

    # 1. Scatter points
    ax.scatter(itemsSubplot['year'], itemsSubplot['CSIRO'])

    # 2. Add labels and title
    ax.plot(firstline, y_pred)
    ax.plot(year_filter, new_y_pred)

    

    # 3. Add title and the labels
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # actual = ax.get_lines()[0].get_ydata().tolist()
    # print(len(actual))



    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return ax