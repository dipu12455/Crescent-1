from queries import initSql, closeSql, createTables

if __name__ == "__main__": # this is true when this script is run directly, used for main entry point
    initSql() # initializes the connection and cursor
    createTables() # creates the tables
    print("Tables created successfully")
    closeSql() # closes the connection and cursor

