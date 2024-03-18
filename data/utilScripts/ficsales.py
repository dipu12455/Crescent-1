import csv

# Specify the input and output file paths
input_file = 'Sales.csv'
output_file = 'output500.csv'

# Open the input and output files
with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
    reader = csv.reader(file_in)
    writer = csv.writer(file_out)

    # Write the header row to the output file
    header = next(reader)
    writer.writerow(header)

    # Iterate over each row in the input file
    for row in reader:
        house_id = int(row[0])  # Assuming house_id is in the first column

        # Check if house_id is greater than 48
        if house_id <= 48:
            writer.writerow(row)