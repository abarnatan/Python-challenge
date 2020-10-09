# import modules 
import os 
import csv

# Read file 'budget_data.csv'

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    #skip header row
    next(csvreader, None)

    # Create analysis output
    #print("Financial Analysis")
    #print("-------------------------------")

    # Count number of months included in dataset
    #num_of_rows = sum(1 for line in csvfile)
    #print("Number of months:" ,num_of_rows)

    # Net total of profit/losses over period 
    month_count = 0
    total_value = 0
    for row in csvreader:
        month_count = month_count + 1
        total_value = total_value + int(row[1])
   

print("Financial Analysis")
print("-------------------------------")
print("Number of months:" ,month_count)
print("Total P/L:" ,total_value)