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
    # first_row = next(csvreader)
   
    # Define Variables
    month_count = []
    total_value = []
    PLchange = [] 
   
    
    # Create analysis output
    # Count number of months included in dataset
    # Net total of profit/losses over period 
    for row in csvreader:
        month_count.append(row[0])

        total_value.append(int(row[1])) 
        
    for x in range (1,len(total_value)):
        PLchange.append(int(total_value[x])-int(total_value[x-1]))
   
    # print(PLchange)    

    totalmonths = len(month_count)
    totalProfit = sum(total_value)
    AvgChange = sum(PLchange) / len(PLchange)
    GreatestIncrease = max(PLchange)
    GreatestDecrease = min(PLchange)
    GreatestIncreaseDate = month_count[PLchange.index(GreatestIncrease)+1] 
    GreatestDecreaseDate = month_count[PLchange.index(GreatestDecrease)+1]



print("Financial Analysis")
print("-------------------------------")
print("Number of months:" + str(totalmonths))
print(f"Total: ${totalProfit}")
print(f"Average Change: ${AvgChange}")
print(f"Greates Increase in Profits: {GreatestIncreaseDate} ${GreatestIncrease}")
print(f"Greates Decrease in Profits: {GreatestDecreaseDate} ${GreatestDecrease}")