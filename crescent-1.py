from queries import initSql, closeSql, executeQueryFromFile, fillData
import matplotlib.pyplot as plt

if __name__ == "__main__": # this is true when this script is run directly, used for main entry point
    initSql() # initializes the connection and cursor

    # create tables
    # executeQueryFromFile('sql/createTables.sql')
    # print("Tables created successfully")

    # fill data
    # fillData()
    # print("Data filled successfully")

    # create foreign keys
    # executeQueryFromFile('sql/createAllForeignKeys.sql')
    # print("Foreign keys created successfully")

    

    # Data for x-axis (years)
    years = range(2014, 2025)

    # Data for y-axis (number of houses)
    houses = [100, 150, 200, 180, 220, 250, 300, 280, 320, 350, 400]

    # Create the line graph
    plt.plot(years, houses)

    # Set the labels for x-axis and y-axis
    plt.xlabel('Years')
    plt.ylabel('Number of Houses')

    # Set the title of the graph
    plt.title('Number of Houses Over Time')

    # Display the graph
    plt.show()








    # wait for user
    # input("Press Enter to continue..., all created tables will be deleted")

    # # drop all tables
    # executeQueryFromFile('sql/dropAllTables.sql')
    # print("Tables deleted successfully")
    closeSql() # closes the connection and cursor
