from queries import initSql, closeSql, executeQueryFromFile, fillData
import csv

if __name__ == "__main__": # this is true when this script is run directly, used for main entry point
    initSql() # initializes the connection and cursor

    # create tables
    executeQueryFromFile('sql/createTables.sql')
    print("Tables created successfully")

    # create foreign keys

    fillData()
    
    


    # wait for user
    # input("Press Enter to continue..., all created tables will be deleted")

    # drop all tables
    # executeQueryFromFile('sql/dropAllTables.sql')
    # print("Tables deleted successfully")
    closeSql() # closes the connection and cursor

