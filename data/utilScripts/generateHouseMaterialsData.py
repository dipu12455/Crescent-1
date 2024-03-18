import csv
import random

# Open the CSV file in write mode
with open('output300.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerow(['house_id', 'supplier_id', 'material_id', 'how_many'])
    
    for i in range(1, 49):
        random.seed()  # Reseed the random function in each iteration
        for j in range(1, 11):
            for k in range(1, 30):
                dice_roll = random.randint(1, 10)
                how_manys = random.randint(1, 30)
                if dice_roll == 1:
                    # Write the data row
                    writer.writerow([i, j, k, how_manys])
