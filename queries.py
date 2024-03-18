import mysql.connector # to install this module > pip install mysql-connector-python
import csv

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
    executeQuery(query)

def fillData():
    # fill Houses table
    header = "use crescent1;\ninsert into Houses (address, city, state, zipcode, construction_date)\n values"
    sendQueryFromCsv('data/Houses.csv', header)

    # fill Materials table
    header = "use crescent1;\ninsert into Materials (material_name)\n values"
    sendQueryFromCsv('data/Materials.csv', header)

    # fill Sales table
    header = "use crescent1;\ninsert into Sales (house_id, sale_date, sale_price)\n values"
    sendQueryFromCsv('data/Sales.csv', header)

    # fill SupplierMaterials table
    header = "use crescent1;\ninsert into SupplierMaterials (supplier_id, material_id, unit_price)\n values"
    sendQueryFromCsv('data/SupplierMaterials.csv', header)

    # fill Suppliers table
    header = "use crescent1;\ninsert into Suppliers (supplier_name, contact_person, phone_number)\n values"
    sendQueryFromCsv('data/Suppliers.csv', header)




def sendQueryFromCsv(_csvfile,_header):
    queryString = _header

    # read CSV file
    with open(_csvfile, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # skip the header row if it exists

        # iterate over each row in the CSV file
        for row in csvreader:
            # process the row and insert data into tables
            queryString += "("
            for i in range(0, len(row)):
                queryString += "'" + row[i] + "', "
            queryString = queryString[:-2] # removing the last comma and space
            queryString += "),\n"

    # remove the last two characters
    queryString = queryString[:-2]
    queryString += ";"

    # execute the query 
    executeQuery(queryString)

def executeQuery(_query):
    # Execute the query
    queries = _query.split(';') # separate queries by the semicolon
    for q in queries:
        if q.strip(): # after removing whitespaces with strip(), checks if the string is not empty
            cursor.execute(q) # execute that single split query, the cursor.execute() can only execute one query at a time

    # Commit the changes
    connection.commit()
    # changes need to be committed when making changes like this to the database, it is good practice