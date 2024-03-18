from queries import initSql, closeSql, executeQueryFromFile

if __name__ == "__main__": # this is true when this script is run directly, used for main entry point
    initSql() # initializes the connection and cursor
    executeQueryFromFile('sql/createTables.sql')
    print("Tables created successfully")
    executeQueryFromFile('sql/createAllForeignKeys.sql')
    print("Foreign keys created successfully")
    input("Press Enter to continue..., all created tables will be deleted")
    executeQueryFromFile('sql/dropAllTables.sql')
    print("Tables deleted successfully")
    closeSql() # closes the connection and cursor

