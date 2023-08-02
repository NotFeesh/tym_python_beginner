import csv

# Usage example:
file_path = 'waldo_spreadsheet.csv'
with open(file_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    data_2d_array = [row for row in csv_reader]

print(data_2d_array)
