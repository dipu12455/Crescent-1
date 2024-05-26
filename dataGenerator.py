import random
import csv
import math

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

# function to read the csv file and store the data in a two dimensional array
def getSupplierMaterials(_filename):
    with open(_filename, 'r') as SMcsvFile:
        SMcsvreader = csv.reader(SMcsvFile)
        next(SMcsvreader) # skip the header row
        unitPriceArray = [] # a two dimensional array to store the unit prices
        for i in range(0,10): 
            unitPriceArray.append([]) # create 10 sublists for 10 suppliers
        for row in SMcsvreader:
            unitPriceArray[int(row[0])-1].append(float(row[2])) # append the unit price to the supplier's sublist
    return unitPriceArray

def getRandomCost(_sale_price):
    # the cost is most likely supposed to be 46% to 67% of the sales price, and probability of sales price
    # being above 67% tends to zero as it approaches 100%.
    # Likewise, the probability of sales price being below 46% tends to zero as it approaches 0%.
    # calculate the ranges for the cost of construction
    lower_limit = int(0.46 * _sale_price)
    upper_limit = int(0.67 * _sale_price)
    probability = 0 # set a probability starter value
    saikoro = 0 # dice
    while True:
        # now generate a random cost for construction
        randomCost = random.randint(60000,4000000)
        # now determine probability of choosing this random value
        if randomCost < lower_limit:
            difference = lower_limit - randomCost # the larger the difference, the less the probability
            normalized = difference / lower_limit # i dont understand this part, but it is necassary
            # a larger difference gives a larger value between 0 and 1
            probability = 1 - normalized # because the probability is flipped for some reason
        elif randomCost > upper_limit:
            difference = randomCost - upper_limit
            normalized = difference / randomCost # the denominator needs to be the larger value of the difference, i don't know why. this is to prevent the normalized value to stay within 0 and 1
            probability = 1 - normalized
        else:
            probability = 1
            return randomCost # no dice roll needed, use the value directly
        # now roll the dice to see if the probability is met
        try:
            saikoro = random.randint(1,int((1-probability)*100)) # you have to reflip the probability to use it as a dice roll
        except:
            continue # if bad value, just go to next loop for a fresh value
        if saikoro == 1: # if dice roll is 1, probability happened, so use this value
            return randomCost

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

def createHouseMaterialsCSV(): # Sales.csv must exist before this function is called
    # this csv determines how much it cost to build each house
    # firstly the construction cost of a house is dependent on its sales price.
    # a house cannot be constructed for $0 and sold for $3 million, so proper randomization is necessary

    # read the SupplierMaterials.csv file and store it in a two dimensional array array[supplier_id][material_id]
    unitPriceArray = getSupplierMaterials('data/presets/SupplierMaterials.csv')
    # use (index-1) to get array value, unitPriceArray index starts at 0, SupplierMaterials.csv starts at 1
    with open('data/HouseMaterials.csv', 'w', newline='') as outputfile:
        outputwriter = csv.writer(outputfile)
        # we don't have a loop here, so printing heading won't be repeated, no control required
        outputwriter.writerow(["house_id", "supplier_id", "material_id", "howMany"])
        # first get sale_price from Sales.csv
        with open('data/Sales.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # skip the header row
            for row in csvreader:
                sale_price = int(row[2])
                construction_cost = getRandomCost(sale_price) # get the random cost of construction

                # now we generate the supplier_id and material_id that were used to construct this house.
                # choose how many different materials were used to contruct this house
                # divide the construction cost by this number to get the cost share of each material
                # randomize the cost share, then divide it by their unit price to get a random quantity of
                # each material. This yields a cost of construction that is close to the randomCost as much as
                # possible

                # decide how many materials for the house to have, from 9 to 30 materials
                counter = random.randint(9,29)
                materialCostShare = math.ceil(construction_cost / counter)
                material_id_checklist = [0]
                newMaterial_id = 0
                for i in range(1, counter+2):
                    # generate a unique material_id, needs to be between 1 and 30 since there are 30 materials
                    while newMaterial_id in material_id_checklist:
                        newMaterial_id = random.randint(1,30)
                    material_id_checklist.append(newMaterial_id) # add it to list so it doesn't repeat

                    # generate a random supplier_id
                    newSupplier_id = random.randint(1,10)

                    randomizedMaterialCostShare = materialCostShare + random.randint(int(-0.2*materialCostShare), int(0.2*materialCostShare))
                    # now get the unitPrice for this material from unitPriceArray
                    unitPrice = unitPriceArray[newSupplier_id-1][newMaterial_id-1]
                    # now get the quantity (howMany) of this material needed
                    newHowMany = math.ceil(randomizedMaterialCostShare / unitPrice)
                    outputwriter.writerow([row[0], newSupplier_id, newMaterial_id, newHowMany])
        

# CSV for Materials.csv, Suppliers.csv, and SupplierMaterials.csv doesn't need to be generated, the preset data is enough

def generateRandomCSVData():
    createSalesCSV(13, 9, 10, 250000, 5000000)
    print("Sales.csv created.")
    createHousesCSV()
    print("Houses.csv created.")
    createHouseMaterialsCSV()
    print("HouseMaterials.csv created.")

if __name__ == "__main__":
    print("Generating random data...")
    generateRandomCSVData()
    print("Data generation complete.")







