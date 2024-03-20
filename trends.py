import matplotlib.pyplot as plt
from queries import getTrendOfHouseSales 

def drawPlotOfHouseSales():
    # Data for x-axis (years)
    years = range(2014, 2024)

    # Data for y-axis (number of houses)
    houses = getTrendOfHouseSales()

    # Create the line graph
    plt.plot(years, houses)

    # Set the labels for x-axis and y-axis
    plt.xlabel('Years')
    plt.ylabel('Number of Houses')

    # Set the title of the graph
    plt.title('Number of Houses Over Time')

    # Display the graph
    plt.show()