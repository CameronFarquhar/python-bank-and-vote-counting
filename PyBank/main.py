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
    csv_list = list(csvreader)

    #loop through the list and calculate the sume of row 1
    total = sum(int(row[1]) for row in csv_list)

    #create a variable to hold a list of each profit/loss value
    total_list = []

    #create a loop to grab each profit/loss value
    for row in csv_list:
        total_list.append(row[1])

    #create a variable to hold the difference in profits between each month
    diff_list = []

    #create a loop that starts at the second value in the list so we can subtract from the first.
    for i in range(1,len(total_list)):
        #create a varable (x) to grabe current minus previous value and store it in diff_list
        x = int(total_list[i]) - int(total_list[i-1])
        diff_list.append(x)

    #find the average and round it to the nearest 2 decimal points
    average = round(sum(diff_list)/len(diff_list),2)

    print("Financial Analysis")
    print('----------------------------')
    print(f'Total Months: {len(csv_list)}')
    print(f'Total: ${total}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: ')
    print(f'Greatest Decrease in Profits: ')