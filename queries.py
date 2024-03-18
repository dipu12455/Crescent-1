import mysql.connector # to install this module > pip install mysql-connector-python

# create a global connection variable
connection = None
cursor = None

# contains the setup for connection and cursor
def initSql():
    # Create a connection
    global connection
    global cursor
    # specify variables as global when trying to change their value inside a function, here we are initializing the global variables, so we need it
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="m!lesOv3rS4turN",
        database="crescent1"
        )
    # Create a cursor
    cursor = connection.cursor()

def closeSql():
    # Close the cursor
    cursor.close()
    # Close the connection
    connection.close()

def executeQueryFromFile(_sqlFilename):
    # Read the SQL query from the file
    with open(_sqlFilename, 'r') as file:
        query = file.read() # stores the entire file in the query variable, contains multiple queries though, cannot be executed all at once yet

    # Execute the query
    queries = query.split(';') # seperate queries by the semicolon
    for q in queries:
        if q.strip(): # after removing whitespaes with strip(), checks if the string is not empty
            cursor.execute(q) # execute that single split query, the cursor.execute() can only execute one query at a time

    # Commit the changes
    connection.commit()
    # changes need to be committed when making changes like this to the database, it is good practice