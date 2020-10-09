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
    print("Financial Analysis")
    print("-------------------------------")
    
    # Count number of months included in dataset
    num_of_rows = sum(1 for line in csvfile)
    print("Number of months:" ,num_of_rows)

    # Net otal of profit/losses over period 

    
