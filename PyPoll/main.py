import os
import csv


khan_vote = 0
correy_vote = 0
li_vote = 0
o_tooley_vote = 0
total_votes = 0


# Path to collect data from the Resources folder
poll_csv_load = os.path.join('Resources','election_data.csv')


#poll_csv_output = os.path.join('Analysis','poll_analysis.csv')
with open(poll_csv_load, "r") as csvfile:

    # create a variable for the data to be read. DictReader
    csvreader = csv.reader(csvfile)
    
    #skip the header row
    header = next(csvreader)

    for row in csvreader:

        #capture total num of votes
        total_votes += 1
    
        #capture total number of votes for each candidate
        if str(row[2]) == "Khan":
            khan_vote += 1

        if str(row[2]) == "Correy":
            correy_vote += 1

        if str(row[2]) == "Li":
            li_vote += 1

        if str(row[2]) == "O'Tooley":
            o_tooley_vote += 1

        #determine the percentage of votes

        khan_percent = (khan_vote/total_votes) * 100

        correy_percent = (correy_vote/total_votes) * 100

        li_percent = (li_vote/total_votes) * 100

        o_tooley_percent = (o_tooley_vote/total_votes) * 100

        #calculate winner

        if khan_percent > correy_percent or li_percent or o_tooley_percent:
            winner = "Khan"

        elif correy_percent > khan_percent or li_percent or o_tooley_percent:
            winner = "Correy"

        elif li_percent > khan_percent or correy_percent or o_tooley_percent:
            winner = "Li"

        elif o_tooley_percent > khan_percent or correy_percent or li_percent:
            winner = "O'Tooley"

output = (
    'Election Results\n'
    '-------------------------\n'
    f'Total Votes: {total_votes}\n'
    '-------------------------\n'

f"Khan: {round(khan_percent,2)}% ({khan_vote})\n"
f"Correy: {round(correy_percent,2)}% ({correy_vote})\n"
f"Li: {round(li_percent,2)}% ({li_vote})\n"
f"O'Tooley: {round(o_tooley_percent,2)}% ({o_tooley_vote})\n"
'-------------------------\n'
f'Winner: {winner}\n'
'-------------------------\n'
)

print(output)

output_path = os.path.join("Analysis", "Analysis.txt")

with open(output_path, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(output)