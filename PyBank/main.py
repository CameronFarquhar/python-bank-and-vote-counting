# import modules
import os
import csv

#create a path leading to the CSV file
budget_csv = os.path.join('Resources','budget_data.csv')

#open the CSV file in this project
with open(budget_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip the header row
    header = next(csvreader)

    #create a list variable for csvreader
    whole_list = list(csvreader)


    #loop through the list and calculate the sume of row 1
    total = sum(int(row[1]) for row in whole_list)

    print("Financial Analysis")
    print('----------------------------')
    print(f'Total Months: {len(whole_list)}')
    print(f'Total: ${total}')
    print(f'Average Change: $')
    print(f'Greatest Increase in Profits: ')
    print(f'Greatest Decrease in Profits: ')