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
    
   
    # Define Variables
    totalvotes = 0
    KhanVotes = 0
    CorreyVotes = 0 
    LiVotes = 0
    TooleyVotes = 0 

    # Create analysis output
    # Count total votes
    # Count votes per candidate
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
   
    # Calculate winner     

    winner = max(KhanVotes,CorreyVotes,LiVotes,TooleyVotes) 
    
    # Calculate percentages of votes
    KhanPercent = KhanVotes / totalvotes * 100
    CorreyPercent = CorreyVotes / totalvotes * 100
    LiPercent = LiVotes / totalvotes * 100
    TooleyPercent = TooleyVotes / totalvotes * 100

    # Conditional set to find winner
    if winner == KhanVotes: 
        winner_is = "Khan"
    elif winner == CorreyVotes:
        winner_is = "Correy"
    elif winner == LiVotes:
        winner_is = "Li"
    else:
        winner_is = "O'Tooley"
        
        

# print poll results 
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
# open output file
with open("output_file.txt", "w") as writer:  
    writer.write ("Election Results \n")
    writer.write ("---------------------------- \n")
    writer.write (f"Total votes: {totalvotes} \n")
    writer.write ("---------------------------- \n")
    writer.write (f"Khan: {round(KhanPercent)}% ({KhanVotes})\n")
    writer.write (f"Correy: {round(CorreyPercent)}% ({CorreyVotes})\n")
    writer.write (f"Li: {round(LiPercent)}% ({LiVotes})\n")
    writer.write (f"O'Tooley: {round(TooleyPercent)}% ({TooleyVotes})\n")
    writer.write ("---------------------------- \n")
    writer.write (f"Winner: {winner} \n")
    
