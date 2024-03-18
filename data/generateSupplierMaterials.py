import csv
import random

# Open the CSV file in write mode
with open('output400.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerow(['supplier_id', 'material_id', 'unit_price'])
    
    for i in range(1, 11):
        random.seed()  # Reseed the random function in each iteration
        for j in range(1, 30):
            unit_price = round(random.uniform(1, 30), 2)
            writer.writerow([i, j, unit_price])
