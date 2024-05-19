import random
import csv

def generateRandomDate(_year):
    newYear = _year + 2000
    newMonth = random.randint(1,12)
    if newMonth < 10:
        newMonth = "0" + str(newMonth)
    newDay = random.randint(1,28)
    if newDay < 10:
         newDay = "0" + str(newDay)
    newHour = random.randint(0,23)
    if newHour < 10:
        newHour = "0" + str(newHour)
    newMinute = random.randint(0,59)
    if newMinute < 10:
        newMinute = "0" + str(newMinute)
    newSecond = random.randint(0,59)
    if newSecond < 10:
        newSecond = "0" + str(newSecond)
    return str(newYear) + "-" + str(newMonth) + "-" + str(newDay) + " " + str(newHour) + ":" + str(newMinute) + ":" + str(newSecond)

# program that generates csv files that can be used by crescent-1 to populate its database
# allows a variety of data to be generated along with the volume of data desired like how many houses you want, etc.

# need to describe the criteria for the data first

def createSalesCSV(_upper, _lower, _noOfYears, _minSalesPrice, _maxSalesPrice):
    # make a random number of sales each year, upper and lower limit of sales defined as required

    # first csv file to generate is Sales.csv
    # columns: house_id, sale_date, sale_price
    # format: 3,2012-04-06 09:15:23,444720
    # there will also be a SN column, but that is added automatically by SQL

    # only one house per sale
    upperLimitHouseSalesPerYear = _upper
    lowerLimitHouseSalesPerYear = _lower
    numberOfYears = _noOfYears # how many years worth of data to make
    minimumHouseSalePrice = _minSalesPrice
    maximumHouseSalePrice = _maxSalesPrice
    house_id_checklist = [0]
    newHouse_id = 0

    # create a list of random numbers for house ids that don't repeat for each year
    once = False # to print the heading for the csv file
    with open('data/Sales.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        if once == False:
            csvwriter.writerow(["house_id", "sale_date", "sale_price"])
            once = True
        for year in range(0, numberOfYears):
            # decide how many houses sold in this year
            housesSoldThisYear = random.randint(lowerLimitHouseSalesPerYear, upperLimitHouseSalesPerYear)
            for i in range(0, housesSoldThisYear):
                # generate a unique house_id
                while newHouse_id in house_id_checklist:
                    newHouse_id = random.randint(1,9999)
                house_id_checklist.append(newHouse_id) # add it to list so it doesn't repeat
                
                # now generate a random date and time using this year
                newSale_date = generateRandomDate(year)
                
                # now generate a random sale price
                newSale_price = random.randint(minimumHouseSalePrice, maximumHouseSalePrice)
                csvwriter.writerow([newHouse_id, newSale_date, newSale_price])

def createHousesCSV(): # needs to be called after the Sales.csv file is created
    with open('data/Sales.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # skip the header row if it exists

        # open a csv file to write
        once = False # to print the heading for the csv file
        with open('data/Houses.csv', 'w', newline='') as outputfile:
            outputwriter = csv.writer(outputfile)
            if once == False:
                outputwriter.writerow(["house_id", "address", "city", "state", "zipcode", "construction_date"])
                once = True
            # iterate over each row in the CSV file
            for row in csvreader:
                # now you have the first field of the row as the house_id as row[0]
                newHouse_id = row[0]

                # next generate a random street address
                houseNumber = random.randint(1,9999)
                streetName = random.choice(["Main", "Elm", "Oak", "Pine", "Maple", "Cedar", "Hill", "Lake", "River", "Park", "Sunset", "Sunrise", "Meadow", "Forest", "Grove", "Valley", "Mountain", "Ocean", "Sea", "Bay", "Harbor", "Cove", "Beach", "Island", "Lagoon", "Pond", "Brook", "Stream", "Spring", "Creek", "Falls", "Ridge", "Bluff", "Cliff", "Mesa", "Butte", "Plateau", "Desert", "Canyon", "Garden", "Orchard", "Vineyard", "Farm", "Ranch", "Mansion", "Manor", "Castle", "Palace", "Tower", "Cottage", "Cabin", "Bungalow", "Chalet", "Lodge", "Inn", "Hotel", "Motel", "Resort", "Spa", "Club", "Court", "Terrace", "Place", "Square", "Circle", "Lane", "Road", "Drive", "Avenue", "Boulevard", "Way", "Trail", "Path", "Parkway", "Highway", "Freeway", "Expressway", "Turnpike", "Interstate", "Route", "Street"])
                streetType = random.choice(["St", "Ave", "Blvd", "Rd", "Dr", "Cir", "Ln", "Way", "Ct", "Pl", "Pkwy", "Hwy", "Fwy", "Expy", "Tpke", "I", "Rt"])
                newAddress = str(houseNumber) + " " + streetName + " " + streetType

                # now generate a random city
                newCity = random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "San Francisco", "Indianapolis", "Columbus", "Fort Worth", "Charlotte", "Seattle", "Denver", "El Paso", "Detroit", "Washington", "Boston", "Memphis", "Nashville", "Portland", "Oklahoma City", "Las Vegas", "Baltimore", "Louisville", "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Mesa", "Kansas City", "Atlanta", "Long Beach", "Omaha", "Raleigh", "Miami", "Oakland", "Minneapolis", "Tulsa", "Cleveland", "Wichita", "Arlington", "New Orleans", "Bakersfield", "Tampa", "Honolulu", "Anaheim", "Aurora", "Santa Ana", "St. Louis", "Riverside", "Corpus Christi", "Lexington", "Pittsburgh", "Anchorage", "Stockton", "Cincinnati", "St. Paul", "Toledo", "Greensboro", "Newark", "Plano", "Henderson", "Lincoln", "Buffalo", "Jersey City", "Chula Vista", "Fort Wayne", "Orlando", "St. Petersburg", "Chandler", "Laredo", "Norfolk", "Durham", "Madison", "Lubbock", "Irvine", "Winston-Salem", "Glendale", "Garland", "Hialeah", "Reno", "Chesapeake", "Gilbert", "Baton Rouge", "Irving", "Scottsdale", "North Las Vegas", "Fremont", "Boise", "Richmond", "San Bernardino", "Birmingham", "Spokane", "Rochester", "Des Moines", "Modesto", "Fayetteville", "Tacoma", "Oxnard", "Fontana", "Columbus", "Montgomery", "Moreno Valley", "Shreveport", "Aurora", "Yonkers", "Akron", "Huntington Beach", "Little Rock", "Augusta", "Amarillo"])

                # now generate a random state
                newState = random.choice(["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"])

                # now generate a random zip code
                newZip = random.randint(10000, 99999)

                # now generate a random construction date that is only a few months behind the sale date
                sale_date = row[1]
                sale_month = int(sale_date[5:7])
                construction_month = sale_month - random.randint(1,6)
                if construction_month < 1: # if received negative, round it out
                    construction_month = 12 + construction_month
                if construction_month < 10: # add a zero for single digit months
                    construction_month = "0" + str(construction_month)

                construction_year = int(sale_date[0:4]) - 1 # just to make sure construction date is always behind sale date
                newConstruction_date = str(construction_year) + "-" + str(construction_month) + "-01 00:00:00"
                outputwriter.writerow([newHouse_id, newAddress, newCity, newState, newZip, newConstruction_date])


def generateRandomCSVData():
    createSalesCSV(13, 9, 10, 250000, 5000000)
    createHousesCSV()

if __name__ == "__main__":
    generateRandomCSVData()
    print("Data generation complete.")





