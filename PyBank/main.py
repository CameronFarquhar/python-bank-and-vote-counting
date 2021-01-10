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
    #set a value for total to grab all the values in the 2nd row
    total = 0
    #determine the amount of months
    months = len(list(csvreader))
    #create a loop that runs through the whole file
    for row in csvreader:
        #grab each value in the Total column
        total += float(row[1])
    #print the value with squigly brackets to contain the added total
    print(f'total: {total}')

