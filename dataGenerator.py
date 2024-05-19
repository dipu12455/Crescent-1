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

# make a random number of sales each year, upper and lower limit of sales defined as required

# first csv file to generate is Sales.csv
# columns: house_id, sale_date, sale_price
# format: 3,2012-04-06 09:15:23,444720
# there will also be a SN column, but that is added automatically by SQL

# only one house per sale
upperLimitHouseSalesPerYear = 13
lowerLimitHouseSalesPerYear = 9
numberOfYears = 10 # how many years worth of data to make
minimumHouseSalePrice = 250000
maximumHouseSalePrice = 5000000
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





