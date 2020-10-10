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
    first_row = next(csvreader)
    print(first_row)
    # Define Variables
    month_count = 1
    total_value = int(first_row[1]) 
    old_month = int(first_row[1]) 
    new_month = 0
    PLchange = 0 
    monthList = []
    # Create analysis output
    # Count number of months included in dataset
    # Net total of profit/losses over period 
    for row in csvreader:
        month_count = month_count + 1
        total_value = total_value + int(row[1])
        
        
        # Calculate Avg change in P/L
        # store previous value
        # store current value 
        # subtract current - previous 
        # loop through and average 
        new_month = int(row[1]) 
        PLchange = new_month - old_month
        monthList.append(PLchange)
        old_month = new_month

# sum of month list / length of month list 
print(monthList)

   

print("Financial Analysis")
print("-------------------------------")
print("Number of months:" ,month_count)
print("Total P/L:" ,total_value)
print("Average change in P/L")