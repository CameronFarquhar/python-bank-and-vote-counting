import os
import csv

                    #candidate_names_1 = ["Khan", "Correy", "Li", "O'Tooley"]
khan_vote = 0
correy_vote = 0
li_vote = 0
o_tooley_vote = 0

total_votes = 0
                    #candidate_votes = [0,0,0,0]

# Path to collect data from the Resources folder
poll_csv_load = os.path.join('Resources','election_data.csv')

#poll_csv_output = os.path.join('Analysis','poll_analysis.csv')
with open(poll_csv_load, "r") as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile)
    
    #skip the header row
    header = next(csvreader)

    for row in csvreader:

        #capture total num of votes
        total_votes += 1

        #capture names of each candidate
        # if row['Candidate'] != (row['Candidate'] +1)
        #     candidate_name_1 = row['Candidate']

        # if row['Candidate'] != (row['Candidate'] +1)
        #     candidate_name_2 = row['Candidate']

        # if row['Candidate'] != (row['Candidate'] +1)
        #     candidate_name_3 = row['Candidate']

        # if row['Candidate'] != (row['Candidate'] +1)
        #     candidate_name_4 = row['Candidate']
    
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

print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

print(f"Khan: {round(khan_percent,2)}% ({khan_vote})")
print(f"Correy: {round(correy_percent,2)}% ({correy_vote})")
print(f"Li: {round(li_percent,2)}% ({li_vote})")
print(f"O'Tooley: {round(o_tooley_percent,2)}% ({o_tooley_vote})")

# print(f'{candidate_name[0]}: {percent_votes} ({candidate_votes})')
# print(f'{candidate_name[1]}: {percent_votes} ({candidate_votes})')
# print(f'{candidate_name[2]}: {percent_votes} ({candidate_votes})')
# print(f'{candidate_name[3]}: {percent_votes} ({candidate_votes})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')
