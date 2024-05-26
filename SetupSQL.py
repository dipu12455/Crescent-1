# script to enter csv data into sql database
from queries import initSql, closeSql, executeQueryFromFile, fillData

def dataInit():
    # create tables
    executeQueryFromFile('sql/createTables.sql')
    print("Tables created successfully")

    # fill data
    fillData()
    print("Data filled successfully")

    # create foreign keys
    executeQueryFromFile('sql/createAllForeignKeys.sql')
    print("Foreign keys created successfully")

def cleanup():
    # wait for user
    input("Press Enter to continue..., all created tables will be deleted")

    # # drop all tables
    executeQueryFromFile('sql/dropAllTables.sql')
    print("Tables deleted successfully")

if __name__ == "__main__": # this is true when this script is run directly, used for main entry point
    initSql() # initializes the connection and cursor
    dataInit() # creates tables, fills data, creates foreign keys


    # cleanup() # drops all tables
    closeSql() # closes the connection and cursor
