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
   
    # Define Variables
    month_count = []
    total_value = []
    old_month = int(first_row[1]) 
    new_month = 0
    PLchange = [] 
    monthList = []
    Sum_Month_List = 0
    Len_Month_List = 0
    # Create analysis output
    # Count number of months included in dataset
    # Net total of profit/losses over period 
    for row in csvreader:
        month_count.append(row[0])

        total_value.append(int(row[1]) 
        
    for x in range (len(total_value)-1):
        PLchange.append(total_value[x+1]- total_value[x])
    
    totalmonths = len(month_count)
    totalProfit = sum(total_value)
    AvgChange = sum(PLchange) / len(PLchange)
    print(totalmonths,totalProfit,AvgChange)
        # Calculate Avg change in P/L
        # store previous value
        # store current value 
        # subtract current - previous 
        # loop through and average 
       
# sum of month list / length of month list 

   

#print("Financial Analysis")
#print("-------------------------------")
# print("Number of months:" ,month_count)
# print("Total P/L:" ,total_value)
# print("Average change in P/L:" ,Avg_PL)