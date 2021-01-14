import os
import csv

budget_csv = os.path.join('Resources','budget_data.csv')

#set variables
total = 0
rev = 0
prev_rev = 0
total_change = 0
month_count = 0
inc = ['',0]
dec = ['', 9999999999]

#initialize path
with open(budget_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #loop through data
    for i,row in enumerate(csvreader):
        rev = int(row[1])
        month_count += 1
        total += rev
        
        #create a variable for change in profit/loss
        change = rev - prev_rev

        if i == 0:
            change = 0

        total_change += change
        prev_rev = rev

        #determine max and min witth the associated month
        if change > inc[1]:
            inc[0] = row[0]
            inc[1] = change

        if change < dec[1]:
            dec[0] = row[0]
            dec[1] = change
        #total_list.append(row[1])

output = (
    "Financial Analysis\n"
    '----------------------------\n'
    f'Total Months: {month_count}\n'
    f'Total: ${total}\n'
    f'Average Change: ${round(total_change/month_count - 1)}\n'
    f'Greatest Increase in Profits: {inc[0]}: ${inc[1]}\n'
    f'Greatest Decrease in Profits: {dec[0]}: ${dec[1]}\n'
)
print(output)

#Initialize output path
output_path = os.path.join("Analysis", "Analysis.txt")

with open(output_path, "w") as datafile:
    writer = csv.writer(datafile)

    #write to txt file
    datafile.write(output)