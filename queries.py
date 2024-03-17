import mysql.connector # to install this module > pip install mysql-connector-python

def createTables():
    # Create a connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="m!lesOv3rS4turN",
        database="crescent1"
        )

    # Create a cursor
    cursor = connection.cursor()

    # Read the SQL query from the file
    with open('sql/createTables.sql', 'r') as file:
        query = file.read() # stores the entire file in the query variable, contains multiple queries though, cannot be executed all at once yet

    # Execute the query
    queries = query.split(';') # seperate queries by the semicolon
    for q in queries:
        if q.strip(): # after removing whitespaes with strip(), checks if the string is not empty
            cursor.execute(q) # execute that single split query, the cursor.execute() can only execute one query at a time

    # Commit the changes
    connection.commit()
    # changes need to be committed when making changes like this to the database, it is good practice    

    # Close the cursor
    cursor.close()
    # Close the connection
    connection.close()
