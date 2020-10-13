# import modules 
import os 
import csv

# Read file 'budget_data.csv'

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    #skip header row
    next(csvreader, None)
    # first_row = next(csvreader)
   
    # Define Variables
    totalvotes = 0
    KhanVotes = 0
    CorreyVotes = 0 
    LiVotes = 0
    TooleyVotes = 0 

    # Create analysis output
    # Count number of months included in dataset
    # Net total of profit/losses over period 
    for row in csvreader:
        totalvotes = totalvotes + 1
        if row[2] == "Khan": 
            KhanVotes = KhanVotes + 1
        elif row[2] == "Correy":
            CorreyVotes = CorreyVotes + 1 
        elif row[2] == "Li":
            LiVotes = LiVotes + 1 
        else:
            TooleyVotes = TooleyVotes + 1
    # print(KhanVotes,CorreyVotes,LiVotes,TooleyVotes)       

    winner = max(KhanVotes,CorreyVotes,LiVotes,TooleyVotes) 
    # print(winner)

    KhanPercent = KhanVotes / totalvotes * 100
    CorreyPercent = CorreyVotes / totalvotes * 100
    LiPercent = LiVotes / totalvotes * 100
    TooleyPercent = TooleyVotes / totalvotes * 100

    if winner == KhanVotes: 
        winner_is = "Khan"
    elif winner == CorreyVotes:
        winner_is = "Correy"
    elif winner == LiVotes:
        winner_is = "Li"
    else:
        winner_is = "O'Tooley"
        
    #print(KhanPercent,winner)        

print("Election Results")
print("-------------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------------")
print(f"Khan: {round(KhanPercent)}% ({KhanVotes})")
print(f"Correy: {round(CorreyPercent)}% ({CorreyVotes})")
print(f"Li: {round(LiPercent)}% ({LiVotes})")
print(f"O'Tooley: {round(TooleyPercent)}% ({TooleyVotes})")
print("-------------------------------")
print(f"Winner: {winner_is}")
print("-------------------------------")


output_file = os.path.join("Analysis.txt")

with open(output_file.txt) as text_file:  
    text_file.write ("Election Results \n")
    text_file.write ("---------------------------- \n")
    text_file.write (f"Total votes: {totalvotes} \n")
    text_file.write ("---------------------------- \n")
    text_file.write (f"Khan: {round(KhanPercent)}% ({KhanVotes})\n")
    text_file.write (f"Correy: {round(CorreyPercent)}% ({CorreyVotes})\n")
    text_file.write (f"Li: {round(LiPercent)}% ({LiVotes})\n")
    text_file.write (f"O'Tooley: {round(TooleyPercent)}% ({TooleyVotes})\n")
    text_file.write ("---------------------------- \n")
    text_file.write (f"Winner: {winner} \n")
    
