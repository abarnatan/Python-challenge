# import modules 
import os 
import csv

# Read file 'budget_data.csv'

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Create analysis output
    print("Financial Analysis")
    print("-------------------------------")
    # Count number of months included in dataset
    num_of_rows = sum(1 for line in csvfile) - 1

    print("Number of months:" ,num_of_rows)



    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # for row in csvreader:
     #     print(row)
